// Simulates the n8n pipeline locally with fake upstream data, using the exact
// jsCode strings from n8n-blog-automation-workflow.json, so we catch logic
// bugs (not just syntax errors) before handing the workflow to the user.
const fs = require('fs');
const path = require('path');

const wf = JSON.parse(fs.readFileSync(path.join(__dirname, 'n8n-blog-automation-workflow.json'), 'utf8'));
const codeByName = {};
for (const n of wf.nodes) {
  if (n.type === 'n8n-nodes-base.code') codeByName[n.name] = n.parameters.jsCode;
}

// Minimal n8n expression-context shims -------------------------------------------------
function makeInput(items) {
  return { first: () => items[0] };
}

const nodeOutputs = {};
function nodeRef(name) {
  if (!nodeOutputs[name]) throw new Error('Simulation error: node "' + name + '" has not run yet.');
  return { first: () => nodeOutputs[name][0] };
}

function runCode(name, code, inputItems) {
  const $input = makeInput(inputItems);
  const $ = (refName) => nodeRef(refName);
  const fn = new Function('$input', '$', 'Buffer', 'console', `return (function(){\n${code}\n})();`);
  const result = fn($input, $, Buffer, console);
  nodeOutputs[name] = result;
  return result;
}

// 1. Config & Content Bank ------------------------------------------------------
const configOut = runCode('Config & Content Bank', codeByName['Config & Content Bank'], [{ json: {} }]);
console.log('--- Config & Content Bank ---');
console.log('githubOwner:', configOut[0].json.githubOwner);
console.log('services count:', configOut[0].json.services.length);
console.log('towns count:', configOut[0].json.towns.length);
console.log('inspiration count:', configOut[0].json.inspiration.length);
console.log('chosenImageFile:', configOut[0].json.chosenImageFile);

// 2. Fake "GitHub - Get blog index" response, with two already-published titles ------
const fakeBlogIndexHtml = `<!doctype html><html><body>
<div class="blog-grid">
  <!-- NEXT_ARTICLE_CARD -->
  <article class="blog-card"><h3><a href="mudanzas-sin-ascensor-mallorca.html">Mudanzas sin ascensor en Mallorca: soluciones prácticas paso a paso</a></h3></article>
  <article class="blog-card"><h3><a href="ahorrar-dinero-mudanza-mallorca.html">Cómo ahorrar dinero en tu mudanza en Mallorca sin perder calidad</a></h3></article>
</div>
</body></html>`;
const fakeGetBlogIndexEarly = [{ json: { content: Buffer.from(fakeBlogIndexHtml, 'utf8').toString('base64'), sha: 'BLOGINDEXSHA1' } }];

// 3. Build OpenAI Prompt ------------------------------------------------------
const promptOut = runCode('Build OpenAI Prompt', codeByName['Build OpenAI Prompt'], fakeGetBlogIndexEarly);
console.log('\n--- Build OpenAI Prompt ---');
console.log('publishedTitleCount:', promptOut[0].json.publishedTitleCount);
const userMsg = promptOut[0].json.openaiBody.messages[1].content;
console.log('user prompt mentions both published titles:',
  userMsg.includes('Mudanzas sin ascensor en Mallorca') && userMsg.includes('Cómo ahorrar dinero en tu mudanza'));
console.log('system prompt has anti-repeat instruction:', promptOut[0].json.openaiBody.messages[0].content.includes('NUNCA elijas un tema'));
console.log('blogIndexSha carried forward:', promptOut[0].json.blogIndexSha === 'BLOGINDEXSHA1');

// 4. Fake OpenAI response ------------------------------------------------------
const fakeArticleJson = {
  title: 'Mudanzas de estudiantes en Palma: qué necesitas saber',
  slug: 'mudanzas-estudiantes-palma-test',
  meta_description: 'Consejos para mudanzas de estudiantes en Palma de Mallorca, con presupuestos ajustados y plazos cortos.',
  tags: ['Mudanzas estudiantes', 'Palma', 'Consejos útiles'],
  body_html: '<p>Texto de prueba con Mallorca y Palma mencionados.</p>\n<h2>Un apartado</h2>\n<ul><li>Punto uno</li><li>Punto dos "con comillas"</li></ul>\n<p>Cierre con <strong>negrita</strong> y una `comilla invertida` suelta.</p>',
  faq: [
    { question: '¿Cuánto cuesta una mudanza de estudiante en Palma?', answer: 'Depende del volumen, pero suele ser más económica que una mudanza completa de vivienda.' },
    { question: '¿Puedo mudarme en un fin de semana?', answer: 'Sí, ofrecemos disponibilidad de fin de semana según agenda.' },
  ],
};
const fakeOpenAiResponse = [{
  json: {
    choices: [{ message: { content: JSON.stringify(fakeArticleJson) } }],
  },
}];

// 5. Parse OpenAI Response ------------------------------------------------------
const parseOut = runCode('Parse OpenAI Response', codeByName['Parse OpenAI Response'], fakeOpenAiResponse);
console.log('\n--- Parse OpenAI Response ---');
console.log('slug:', parseOut[0].json.slug);
console.log('readMin:', parseOut[0].json.readMin);
console.log('blogIndexContent carried forward:', typeof parseOut[0].json.blogIndexContent === 'string' && parseOut[0].json.blogIndexContent.includes('NEXT_ARTICLE_CARD'));

// 6. Build HTML ------------------------------------------------------
const buildOut = runCode('Build HTML', codeByName['Build HTML'], parseOut);
const built = buildOut[0].json;
console.log('\n--- Build HTML ---');
console.log('articlePath:', built.articlePath);
console.log('blogIndexPath:', built.blogIndexPath);
console.log('sitemapPath:', built.sitemapPath);
console.log('articleHtml length:', Buffer.from(built.articleHtmlBase64, 'base64').toString('utf8').length);

const articleHtml = Buffer.from(built.articleHtmlBase64, 'base64').toString('utf8');
function checkBalance(html, tag) {
  const openRe = new RegExp('<' + tag + '(?![a-zA-Z-])', 'g');
  const closeRe = new RegExp('</' + tag + '>', 'g');
  const opens = (html.match(openRe) || []).length;
  const closes = (html.match(closeRe) || []).length;
  return { opens, closes, ok: opens === closes };
}
let allBalanced = true;
for (const tag of ['div', 'section', 'header', 'footer', 'html', 'body', 'ul']) {
  const r = checkBalance(articleHtml, tag);
  if (!r.ok) allBalanced = false;
  console.log(`  balance <${tag}>: ${r.opens} open / ${r.closes} close -> ${r.ok ? 'OK' : 'MISMATCH'}`);
}
console.log('  contains "undefined":', articleHtml.includes('undefined'));
console.log('  contains FAQPage schema:', articleHtml.includes('"@type": "FAQPage"'));
console.log('  contains BlogPosting schema:', articleHtml.includes('"@type": "BlogPosting"'));

// 7. Splice card into blog index (now reads blogIndexContent/sha carried in $input, no fresh GET) ---
const spliceCardOut = runCode('Splice card into blog index', codeByName['Splice card into blog index'], buildOut);
const splicedIndex = Buffer.from(spliceCardOut[0].json.githubPutBodyBlogIndex.content, 'base64').toString('utf8');
console.log('\n--- Splice card into blog index ---');
console.log('  marker still present:', splicedIndex.includes('<!-- NEXT_ARTICLE_CARD -->'));
console.log('  new card inserted:', splicedIndex.includes(built.slug + '.html'));
console.log('  old cards preserved:', splicedIndex.includes('mudanzas-sin-ascensor-mallorca.html') && splicedIndex.includes('ahorrar-dinero-mudanza-mallorca.html'));
console.log('  sha carried through from early fetch (not a second GET):', spliceCardOut[0].json.githubPutBodyBlogIndex.sha === 'BLOGINDEXSHA1');

// 8. Splice sitemap entry (still does its own late GET for sitemap.xml) ------------------------------------------------------
const fakeSitemapXml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://mallorcatransportes.com/</loc></url>\n</urlset>\n`;
const fakeGetSitemap = [{ json: { content: Buffer.from(fakeSitemapXml, 'utf8').toString('base64'), sha: 'SITEMAPSHA1' } }];
const spliceSitemapOut = runCode('Splice sitemap entry', codeByName['Splice sitemap entry'], fakeGetSitemap);
const splicedSitemap = Buffer.from(spliceSitemapOut[0].json.githubPutBodySitemap.content, 'base64').toString('utf8');
console.log('\n--- Splice sitemap entry ---');
console.log('  new loc inserted:', splicedSitemap.includes(built.slug + '.html'));
console.log('  well-formed (ends with </urlset>):', splicedSitemap.trim().endsWith('</urlset>'));
console.log('  article PUT body has no sha (create, not update):', !('sha' in spliceSitemapOut[0].json.githubPutBodyArticle));

console.log('\nAll simulated steps completed without throwing.');
