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

// 1. Config & Pick Topic ------------------------------------------------------
const configOut = runCode('Config & Pick Topic', codeByName['Config & Pick Topic'], [{ json: {} }]);
console.log('--- Config & Pick Topic ---');
console.log('weekNumber:', configOut[0].json.weekNumber);
console.log('githubOwner (placeholder expected):', configOut[0].json.githubOwner);
console.log('openaiBody.messages count:', configOut[0].json.openaiBody.messages.length);
console.log('chosenImageFile:', configOut[0].json.chosenImageFile);

// 2. Fake OpenAI response ------------------------------------------------------
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

// 3. Parse OpenAI Response ------------------------------------------------------
const parseOut = runCode('Parse OpenAI Response', codeByName['Parse OpenAI Response'], fakeOpenAiResponse);
console.log('\n--- Parse OpenAI Response ---');
console.log('slug:', parseOut[0].json.slug);
console.log('readMin:', parseOut[0].json.readMin);

// 4. Build HTML ------------------------------------------------------
const buildOut = runCode('Build HTML', codeByName['Build HTML'], parseOut);
const built = buildOut[0].json;
console.log('\n--- Build HTML ---');
console.log('articlePath:', built.articlePath);
console.log('blogIndexPath:', built.blogIndexPath);
console.log('sitemapPath:', built.sitemapPath);
console.log('articleHtml length:', Buffer.from(built.articleHtmlBase64, 'base64').toString('utf8').length);
console.log('cardHtml snippet:', built.cardHtml.slice(0, 120).replace(/\n/g, ' '));

const articleHtml = Buffer.from(built.articleHtmlBase64, 'base64').toString('utf8');
fs.writeFileSync(path.join(__dirname, '_test_output_article.html'), articleHtml, 'utf8');

// sanity checks on the generated article HTML
function checkBalance(html, tag) {
  const openRe = new RegExp('<' + tag + '(?![a-zA-Z-])', 'g');
  const closeRe = new RegExp('</' + tag + '>', 'g');
  const opens = (html.match(openRe) || []).length;
  const closes = (html.match(closeRe) || []).length;
  return { opens, closes, ok: opens === closes };
}
for (const tag of ['div', 'section', 'header', 'footer', 'html', 'body', 'ul']) {
  const r = checkBalance(articleHtml, tag);
  console.log(`  balance <${tag}>: ${r.opens} open / ${r.closes} close -> ${r.ok ? 'OK' : 'MISMATCH'}`);
}
console.log('  contains "undefined":', articleHtml.includes('undefined'));
console.log('  contains "[object Object]":', articleHtml.includes('[object Object]'));
console.log('  contains FAQPage schema:', articleHtml.includes('"@type": "FAQPage"'));
console.log('  contains BlogPosting schema:', articleHtml.includes('"@type": "BlogPosting"'));

// 5. Splice card into blog index ------------------------------------------------------
const fakeBlogIndexHtml = `<!doctype html><html><body>
<div class="blog-grid">
  <!-- NEXT_ARTICLE_CARD -->
  <article>old card</article>
</div>
</body></html>`;
const fakeGetBlogIndex = [{ json: { content: Buffer.from(fakeBlogIndexHtml, 'utf8').toString('base64'), sha: 'FAKESHA123' } }];
const spliceCardOut = runCode('Splice card into blog index', codeByName['Splice card into blog index'], fakeGetBlogIndex);
const splicedIndex = Buffer.from(spliceCardOut[0].json.githubPutBodyBlogIndex.content, 'base64').toString('utf8');
console.log('\n--- Splice card into blog index ---');
console.log('  marker still present:', splicedIndex.includes('<!-- NEXT_ARTICLE_CARD -->'));
console.log('  new card inserted:', splicedIndex.includes(built.slug + '.html'));
console.log('  old card preserved:', splicedIndex.includes('old card'));
console.log('  sha passed through:', spliceCardOut[0].json.githubPutBodyBlogIndex.sha === 'FAKESHA123');

// 6. Splice sitemap entry ------------------------------------------------------
const fakeSitemapXml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://mallorcatransportes.com/</loc></url>\n</urlset>\n`;
const fakeGetSitemap = [{ json: { content: Buffer.from(fakeSitemapXml, 'utf8').toString('base64'), sha: 'FAKESHA456' } }];
const spliceSitemapOut = runCode('Splice sitemap entry', codeByName['Splice sitemap entry'], fakeGetSitemap);
const splicedSitemap = Buffer.from(spliceSitemapOut[0].json.githubPutBodySitemap.content, 'base64').toString('utf8');
console.log('\n--- Splice sitemap entry ---');
console.log('  new loc inserted:', splicedSitemap.includes(built.slug + '.html'));
console.log('  well-formed (ends with </urlset>):', splicedSitemap.trim().endsWith('</urlset>'));
console.log('  article PUT body message:', spliceSitemapOut[0].json.githubPutBodyArticle.message);
console.log('  article PUT body has no sha (create, not update):', !('sha' in spliceSitemapOut[0].json.githubPutBodyArticle));

console.log('\nAll simulated steps completed without throwing.');
