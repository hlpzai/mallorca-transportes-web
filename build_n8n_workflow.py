# -*- coding: utf-8 -*-
"""Generates n8n-blog-automation-workflow.json — a weekly OpenAI -> GitHub
blog-publishing workflow for the Mallorca Transportes static site.
"""
import json
import os

OUT = r"C:\Users\ray\Downloads\Transportes Mallorca-20260831T124637Z-1-001\website\n8n-blog-automation-workflow.json"

PHONE_ICON = '<svg class="icon" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.3 1.1L6.6 10.8z"/></svg>'
WHATSAPP_ICON = '<svg class="icon" viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.7-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5C10 9 9.4 7.6 9.2 7c-.2-.5-.4-.5-.6-.5h-.5c-.2 0-.5.1-.7.3-.2.3-1 1-1 2.4s1 2.8 1.1 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.5-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.5-.3z"/><path d="M12 2C6.5 2 2 6.5 2 12c0 1.9.5 3.7 1.5 5.3L2 22l4.8-1.5c1.5.8 3.3 1.3 5.2 1.3 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.1c-1.7 0-3.3-.5-4.7-1.3l-.3-.2-3.2 1 1-3.1-.2-.3C3.7 14.7 3.2 13.4 3.2 12c0-4.8 3.9-8.7 8.8-8.7s8.8 3.9 8.8 8.7-4 8.1-8.8 8.1z"/></svg>'
WHATSAPP_ICON_BIG = WHATSAPP_ICON.replace('class="icon" ', '')
WHATSAPP_HREF = "https://wa.me/34659924515?text=Hola%2C%20me%20gustar%C3%ADa%20pedir%20presupuesto%20para%20una%20mudanza%2Ftransporte%20en%20Mallorca"

# ---------------------------------------------------------------------------
# JS source for each Code node. Kept as plain Python strings so json.dump()
# handles all the escaping for us — never hand-escape this into the JSON.
# ---------------------------------------------------------------------------

CONFIG_CODE = r"""
// =========================================================================
// EDIT THIS BLOCK with your own values before turning the workflow on.
// =========================================================================
const CONFIG = {
  // GitHub repo where the site lives (must already contain website/index.html,
  // website/blog/index.html and website/sitemap.xml at basePath below)
  githubOwner: 'hlpzai',
  githubRepo: 'mallorca-transportes-web',
  githubBranch: 'main',
  // '' if index.html/blog/sitemap.xml sit at the repo root, otherwise the
  // folder prefix, e.g. 'website/' (note the trailing slash)
  basePath: '',

  siteUrl: 'https://mallorcatransportes.com',
  companyName: 'Mallorca Transportes',
  companyPhone: '+34 659 924 515',
  companyEmail: 'info@mallorcatransportes.com',

  // Any OpenAI chat-completions model that supports response_format json_object
  openaiModel: 'gpt-4.1',
};

// -------------------------------------------------------------------------
// Real services and coverage area, used to ground the model's topic choice.
// Keep in sync with the actual site if either list changes.
// -------------------------------------------------------------------------
const SERVICES = [
  'Mudanzas de hogar',
  'Mudanzas de empresas y oficinas',
  'Transporte de muebles y electrodomésticos',
  'Desmontaje y montaje de muebles',
  'Mudanzas express',
  'Transporte entre Islas Baleares (Mallorca, Menorca, Ibiza, Formentera)',
];

const TOWNS = [
  'Palma de Mallorca', 'Calvià', 'Marratxí', 'Llucmajor', 'Inca', 'Manacor',
  'Sóller', 'Andratx', 'Alcúdia', 'Pollença', 'Felanitx', 'Santa Ponsa',
  'Sa Pobla', 'Campos', 'Artà',
];

// -------------------------------------------------------------------------
// Inspiration only — NOT a fixed rotation any more. The next node passes
// this to the model together with the list of already-published titles, and
// explicitly tells it not to limit itself to these examples and to never
// repeat something already covered. Add more any time.
// -------------------------------------------------------------------------
const INSPIRATION = [
  { topic: 'Mudanzas de estudiantes en Palma: qué necesitas saber' },
  { topic: 'Transporte de electrodomésticos grandes en Mallorca: nevera, lavadora y horno' },
  { topic: 'Mudanzas en Sóller y la Serra de Tramuntana: accesos y particularidades' },
  { topic: 'Cómo transportar un piano de forma segura en Mallorca' },
  { topic: 'Guardamuebles en Mallorca: cuándo tiene sentido y cómo funciona' },
  { topic: 'Mudanzas de última hora en Mallorca: qué esperar y cómo organizarte' },
  { topic: 'Transporte de obras de arte y antigüedades en Mallorca' },
  { topic: 'Mudanzas de temporada alta en Mallorca: julio y agosto' },
  { topic: 'Cómo elegir empresa de mudanzas en Mallorca sin sorpresas' },
  { topic: 'Mudanzas de negocios de hostelería en Mallorca: bares y restaurantes' },
  { topic: 'Transporte de maquinaria ligera y herramientas de trabajo en Mallorca' },
  { topic: 'Mudanzas en Manacor y la comarca de Llevant' },
  { topic: 'Seguro de transporte en las mudanzas: qué cubre realmente' },
  { topic: 'Mudanzas en Inca y el Raiguer: accesos y horarios recomendados' },
  { topic: 'Cómo embalar la vajilla y objetos frágiles para una mudanza' },
  { topic: 'Mudanzas en Alcúdia y Pollença: zonas turísticas y temporada' },
  { topic: 'Transporte de gimnasios y equipamiento deportivo en Mallorca' },
  { topic: 'Mudanzas en Calvià y la Costa de Ponent: viviendas de temporada' },
  { topic: 'Cómo reducir el plástico y el cartón en tu mudanza en Mallorca' },
  { topic: 'Transporte de mobiliario de jardín y exterior en Mallorca' },
  { topic: 'Mudanzas en Llucmajor y Campos: zona sur de Mallorca' },
  { topic: 'Qué hacer si tu mudanza en Mallorca coincide con obras o reforma' },
  { topic: 'Transporte de bicicletas y equipamiento náutico en Mallorca' },
  { topic: 'Mudanzas en Felanitx y Migjorn: qué tener en cuenta' },
];

// -------------------------------------------------------------------------
// Rotating hero-image pool (reuses real photos already on the site so every
// post looks on-brand — no image generation needed). Repeating an image is
// fine, it's just cosmetic; only the CONTENT must never repeat.
// -------------------------------------------------------------------------
const IMAGES = [
  { file: 'trabajo-mudanza-01.jpg', alt: 'Mudanza de vivienda con cajas embaladas en Mallorca' },
  { file: 'trabajo-mudanza-02.jpg', alt: 'Embalaje profesional de electrodomésticos para mudanza en Mallorca' },
  { file: 'trabajo-mudanza-03.jpg', alt: 'Transporte de muebles protegidos en Mallorca' },
  { file: 'trabajo-mudanza-04.jpg', alt: 'Desmontaje y embalaje de mobiliario en mudanza de Mallorca' },
  { file: 'trabajo-mudanza-05.jpg', alt: 'Instalación de mobiliario tras mudanza en Mallorca' },
  { file: 'trabajo-mudanza-06.jpg', alt: 'Montaje de mobiliario de madera en Mallorca' },
  { file: 'equipo-mudanzas-mallorca.jpg', alt: 'Equipo de Mallorca Transportes cargando una furgoneta' },
  { file: 'camion-transporte-mallorca.jpg', alt: 'Camión de Mallorca Transportes para transporte de muebles' },
];

function isoWeekNumber(date) {
  const d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
  d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
  const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
  return Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
}

const now = new Date();
const weekNumber = isoWeekNumber(now);
const chosenImage = IMAGES[weekNumber % IMAGES.length];

return [{
  json: {
    ...CONFIG,
    weekNumber,
    todayIso: now.toISOString().slice(0, 10),
    chosenImageFile: chosenImage.file,
    chosenImageAlt: chosenImage.alt,
    services: SERVICES,
    towns: TOWNS,
    inspiration: INSPIRATION,
  },
}];
""".strip("\n")

BUILD_PROMPT_CODE = r"""
const cfg = $('Config & Content Bank').first().json;
const getResp = $input.first().json;

const blogIndexContent = Buffer.from(getResp.content.replace(/\n/g, ''), 'base64').toString('utf8');

// Pull out every already-published article title straight from the live
// blog index, so the model has the real, current history — not a snapshot
// that could drift out of date.
const titleMatches = [...blogIndexContent.matchAll(/<h3><a[^>]*>([^<]+)<\/a><\/h3>/g)];
const publishedTitles = titleMatches.map((m) => m[1].trim());

const servicesList = cfg.services.map((s) => '- ' + s).join('\n');
const townsList = cfg.towns.join(', ');
const inspirationList = cfg.inspiration.map((t) => '- ' + t.topic).join('\n');
const publishedList = publishedTitles.length
  ? publishedTitles.map((t) => '- ' + t).join('\n')
  : '(todavía no hay artículos publicados)';

const systemPrompt = `Eres un redactor SEO y estratega de contenidos experto en el sector de mudanzas y transporte en Mallorca, escribiendo para la empresa ${cfg.companyName}.
Escribes en español de España, tono cercano y profesional, sin exagerar ni prometer cosas que no se puedan garantizar.
Optimizas el contenido tanto para buscadores tradicionales (SEO) como para que motores de IA tipo ChatGPT, Perplexity o Google AI Overviews puedan citarlo con facilidad (GEO): frases claras y autocontenidas, datos concretos, listas, y una sección final de preguntas frecuentes con respuestas directas de 1-2 frases.
No inventes datos de la empresa que no se te den (precios exactos, número de empleados, premios, cifras de clientes, testimonios).

Antes de escribir, ELIGE tú mismo el tema del artículo de esta semana, razonando como un estratega SEO: qué suele buscar de verdad alguien que necesita una mudanza o transporte en Mallorca, cruzando los servicios reales de la empresa con los municipios donde opera. Prioriza ángulos específicos con intención de búsqueda clara (una duda concreta, una situación concreta, un municipio concreto) por encima de títulos genéricos.

Regla más importante: NUNCA elijas un tema igual o muy parecido a los que ya están publicados en el blog (lista más abajo). Si las ideas de inspiración ya están cubiertas, combina servicio + municipio + situación real de una forma que todavía no se haya tratado.

Devuelve SIEMPRE un único objeto JSON válido, sin texto fuera del JSON, con exactamente estas claves:
- title (string, atractivo y con la palabra clave principal, sin comillas)
- slug (string, en minúsculas, separado por guiones, sin acentos ni caracteres especiales)
- meta_description (string, máx. 155 caracteres)
- tags (array de exactamente 3 strings cortos, estilo etiqueta)
- body_html (string HTML usando solo <h2>, <p>, <ul><li>, <strong>; sin <h1>; sin markdown; entre 550 y 800 palabras; menciona de forma natural al menos un municipio real de Mallorca)
- faq (array de hasta 3 objetos {"question": "...", "answer": "..."}, respuestas de 1-2 frases, directas)
- image_keywords (string, en INGLÉS, 2-4 palabras, describe una escena real y fotografiable relacionada con el tema del artículo — para buscar una foto de stock que encaje. Ejemplos: "moving boxes apartment", "office relocation team", "family unpacking new home". Nunca uses el nombre de la empresa ni de un municipio en este campo, solo la escena visual)`;

const userPrompt = `Servicios reales de la empresa:
${servicesList}

Municipios de Mallorca donde opera:
${townsList}

Ideas de inspiración (no te limites a esta lista, puedes combinar servicio + municipio + situación libremente):
${inspirationList}

Artículos YA PUBLICADOS en el blog — no repitas ninguno de estos temas ni nada muy similar:
${publishedList}

Datos de contacto que puedes mencionar si aporta valor: teléfono ${cfg.companyPhone}, email ${cfg.companyEmail}.
No inventes testimonios, cifras de clientes ni premios.`;

return [{
  json: {
    ...cfg,
    blogIndexContent,
    blogIndexSha: getResp.sha,
    publishedTitleCount: publishedTitles.length,
    openaiBody: {
      model: cfg.openaiModel,
      response_format: { type: 'json_object' },
      temperature: 0.8,
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt },
      ],
    },
  },
}];
""".strip("\n")

PARSE_OPENAI_CODE = r"""
const item = $input.first().json;
const raw = item.choices && item.choices[0] && item.choices[0].message
  ? item.choices[0].message.content
  : null;

if (!raw) {
  throw new Error('La respuesta de OpenAI no trae contenido. Revisa la salida completa del nodo "OpenAI - Generate Article".');
}

let parsed;
try {
  parsed = JSON.parse(raw);
} catch (e) {
  throw new Error('OpenAI no devolvió un JSON válido: ' + e.message + '\n\nContenido recibido (primeros 500 caracteres):\n' + raw.slice(0, 500));
}

const required = ['title', 'slug', 'meta_description', 'tags', 'body_html'];
for (const key of required) {
  if (!parsed[key]) throw new Error('Falta el campo "' + key + '" en el JSON devuelto por OpenAI.');
}

function slugify(s) {
  return s.toString().toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-+|-+$)/g, '');
}

const slug = slugify(parsed.slug || parsed.title);
const words = parsed.body_html.replace(/<[^>]+>/g, ' ').split(/\s+/).filter(Boolean).length;
const readMin = Math.max(2, Math.round(words / 200));

const cfg = $('Build OpenAI Prompt').first().json;

return [{
  json: {
    ...cfg,
    ...parsed,
    slug,
    readMin,
  },
}];
""".strip("\n")

BUILD_HTML_CODE = r"""
const d = $input.first().json;

const PHONE_ICON = '__PHONE_ICON__';
const WHATSAPP_ICON = '__WHATSAPP_ICON__';
const WHATSAPP_ICON_BIG = '__WHATSAPP_ICON_BIG__';
const WHATSAPP_HREF = '__WHATSAPP_HREF__';

function escAttr(s) {
  return String(s).replace(/"/g, '&quot;');
}

const MONTHS_ES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
function fmtDate(iso) {
  const [y, m, day] = iso.split('-').map(Number);
  return day + ' de ' + MONTHS_ES[m - 1] + ' de ' + y;
}

const tagRow = (d.tags || []).map((t) => '<span class="tag-pill">' + t + '</span>').join('\n            ');

// Prefer the Unsplash photo picked for this article's topic; fall back to
// the rotating local pool only if the search failed or returned nothing.
const usingStockPhoto = Boolean(d.heroImageUrl);
const finalImageSrc = usingStockPhoto ? d.heroImageUrl : ('../img/' + d.chosenImageFile);
const finalImageSrcAbsolute = usingStockPhoto ? d.heroImageUrl : (d.siteUrl + '/img/' + d.chosenImageFile);
const finalImageAlt = usingStockPhoto ? d.heroImageAlt : d.chosenImageAlt;
const photoCredit = (usingStockPhoto && d.photographerName)
  ? `<p class="photo-credit">Foto: <a href="${escAttr(d.photographerLink || '#')}" target="_blank" rel="noopener nofollow">${d.photographerName}</a> en <a href="https://unsplash.com" target="_blank" rel="noopener nofollow">Unsplash</a></p>`
  : '';

const header = `<a class="skip-link" href="#contenido">Saltar al contenido</a>

<header class="site-header" id="top">
  <div class="container header-inner">
    <a href="../index.html" class="brand" aria-label="${d.companyName} - Inicio">
      <img src="../img/logo.svg" alt="${d.companyName}" class="brand-logo" width="220" height="50">
    </a>

    <nav class="main-nav" id="main-nav" aria-label="Navegación principal">
      <a href="../index.html#servicios">Servicios</a>
      <a href="../index.html#opiniones">Opiniones</a>
      <a href="index.html">Blog</a>
      <a href="../index.html#contacto">Contacto</a>
    </nav>

    <div class="header-actions">
      <a href="tel:${d.companyPhone.replace(/\s+/g, '')}" class="btn btn-ghost btn-sm header-call">
        ${PHONE_ICON}
        <span>${d.companyPhone.replace('+34 ', '')}</span>
      </a>
      <a href="${WHATSAPP_HREF}" class="btn btn-primary btn-sm" target="_blank" rel="noopener">
        ${WHATSAPP_ICON}
        <span>WhatsApp</span>
      </a>
      <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="main-nav" aria-label="Abrir menú">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
`;

const footer = `<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img src="../img/logo.svg" alt="${d.companyName}" class="footer-logo" width="200" height="46">
      <p>Especialistas en mudanzas y transporte de muebles en Mallorca desde hace más de 15 años. Servicio para particulares y empresas en toda la isla.</p>
    </div>
    <div class="footer-col">
      <h4>Servicios</h4>
      <ul>
        <li><a href="../index.html#servicios">Mudanzas de hogar</a></li>
        <li><a href="../index.html#servicios">Mudanzas de empresa</a></li>
        <li><a href="../index.html#servicios">Transporte de muebles</a></li>
        <li><a href="../index.html#servicios">Desmontaje y montaje</a></li>
        <li><a href="../index.html#servicios">Transporte entre islas</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Contacto</h4>
      <ul>
        <li><a href="tel:${d.companyPhone.replace(/\s+/g, '')}">${d.companyPhone}</a></li>
        <li><a href="mailto:${d.companyEmail}">${d.companyEmail}</a></li>
        <li>Isla de Mallorca, España</li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Empresa</h4>
      <ul>
        <li><a href="../index.html#cobertura">Cobertura</a></li>
        <li><a href="../index.html#trabajos">Trabajos realizados</a></li>
        <li><a href="../index.html#opiniones">Opiniones</a></li>
        <li><a href="index.html">Blog</a></li>
        <li><a href="../index.html#faq">Preguntas frecuentes</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>© ${new Date().getFullYear()} ${d.companyName}. Todos los derechos reservados.</p>
  </div>
</footer>

<a href="${WHATSAPP_HREF}" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Contactar por WhatsApp">
  ${WHATSAPP_ICON_BIG}
</a>

<div class="mobile-cta-bar">
  <a href="tel:${d.companyPhone.replace(/\s+/g, '')}" class="mobile-cta-btn call">
    ${PHONE_ICON}
    Llamar
  </a>
  <a href="${WHATSAPP_HREF}" class="mobile-cta-btn whatsapp" target="_blank" rel="noopener">
    ${WHATSAPP_ICON}
    WhatsApp
  </a>
  <a href="../index.html#contacto" class="mobile-cta-btn quote">Presupuesto</a>
</div>

<script src="../js/main.js"></script>
</body>
</html>
`;

const canonical = d.siteUrl + '/blog/' + d.slug + '.html';
const ogImage = finalImageSrcAbsolute;

const faqHtml = (d.faq || []).length
  ? '\n<h2>Preguntas frecuentes</h2>\n' + d.faq.map((f) => '<p><strong>' + f.question + '</strong><br>' + f.answer + '</p>').join('\n')
  : '';

const faqSchema = (d.faq || []).length
  ? `,
  "mainEntity": [${d.faq.map((f) => `{"@type": "Question", "name": ${JSON.stringify(f.question)}, "acceptedAnswer": {"@type": "Answer", "text": ${JSON.stringify(f.answer)}}}`).join(', ')}]`
  : '';

const schema = `<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": ${JSON.stringify(d.title)},
  "description": ${JSON.stringify(d.meta_description)},
  "image": ${JSON.stringify(ogImage)},
  "datePublished": ${JSON.stringify(d.todayIso)},
  "author": {"@type": "Organization", "name": ${JSON.stringify(d.companyName)}},
  "publisher": {
    "@type": "Organization",
    "name": ${JSON.stringify(d.companyName)},
    "logo": {"@type": "ImageObject", "url": ${JSON.stringify(d.siteUrl + '/img/favicon-512.png')}}
  },
  "mainEntityOfPage": ${JSON.stringify(canonical)}
}
</script>
${(d.faq || []).length ? `<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage"${faqSchema}
}
</script>` : ''}`;

const head = `<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${d.title} | Blog ${d.companyName}</title>
<meta name="description" content="${escAttr(d.meta_description)}">
<meta name="robots" content="index, follow">
<meta name="author" content="${d.companyName}">
<link rel="canonical" href="${canonical}">

<meta property="og:type" content="article">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="${d.companyName}">
<meta property="og:title" content="${escAttr(d.title)}">
<meta property="og:description" content="${escAttr(d.meta_description)}">
<meta property="og:image" content="${ogImage}">
<meta property="og:url" content="${canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${escAttr(d.title)}">
<meta name="twitter:description" content="${escAttr(d.meta_description)}">
<meta name="twitter:image" content="${ogImage}">

<link rel="icon" type="image/png" sizes="32x32" href="../img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="../img/favicon-192.png">
<link rel="apple-touch-icon" href="../img/apple-touch-icon.png">
<meta name="theme-color" content="#FF7300">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/styles.css">
${schema}`;

const articleHtml = `<!doctype html>
<html lang="es">
<head>
${head}
</head>
<body>

${header}

<main id="contenido">
  <section class="page-header">
    <div class="container">
      <p class="breadcrumb"><a href="../index.html">Inicio</a> <span aria-hidden="true">/</span> <a href="index.html">Blog</a> <span aria-hidden="true">/</span> Artículo</p>
      <h1>${d.title}</h1>
      <div class="tag-row">
        ${tagRow}
      </div>
      <div class="article-meta-row">
        <span>${d.companyName}</span>
        <span aria-hidden="true">·</span>
        <span>${fmtDate(d.todayIso)}</span>
        <span aria-hidden="true">·</span>
        <span>${d.readMin} min de lectura</span>
      </div>
    </div>
  </section>

  <div class="article-hero">
    <img src="${finalImageSrc}" alt="${escAttr(finalImageAlt)}" width="1600" height="700" fetchpriority="high">
    ${photoCredit}
  </div>

  <section class="section">
    <div class="container article-layout">
      <div class="article-body">
        ${d.body_html}
        ${faqHtml}

        <div class="article-cta">
          <p>¿Quieres un presupuesto gratuito para tu mudanza o transporte en Mallorca?</p>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a href="tel:${d.companyPhone.replace(/\s+/g, '')}" class="btn btn-primary">Llamar ahora</a>
            <a href="../index.html#contacto" class="btn btn-outline">Pedir presupuesto</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

${footer}`;

const cardHtml = `
        <article class="blog-card">
          <a href="${d.slug}.html" class="blog-card-image">
            <img src="${finalImageSrc}" alt="${escAttr(finalImageAlt)}" loading="lazy" width="900" height="563">
          </a>
          <div class="blog-card-body">
            <div class="tag-row">
              ${tagRow}
            </div>
            <h3><a href="${d.slug}.html">${d.title}</a></h3>
            <p>${d.meta_description}</p>
            <div class="blog-card-meta">
              <span>${fmtDate(d.todayIso)}</span>
              <a href="${d.slug}.html">Leer más →</a>
            </div>
          </div>
        </article>`;

const sitemapEntry = `  <url>
    <loc>${canonical}</loc>
    <lastmod>${d.todayIso}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
`;

return [{
  json: {
    ...d,
    articlePath: d.basePath + 'blog/' + d.slug + '.html',
    blogIndexPath: d.basePath + 'blog/index.html',
    sitemapPath: d.basePath + 'sitemap.xml',
    articleHtmlBase64: Buffer.from(articleHtml, 'utf8').toString('base64'),
    cardHtml,
    sitemapEntry,
  },
}];
""".strip("\n")

PICK_PHOTO_CODE = r"""
const parsed = $input.first().json;
const searchResp = $('Unsplash - Search Photo').first().json;

const result = searchResp && Array.isArray(searchResp.results) ? searchResp.results[0] : null;

let heroImageUrl = null;
let heroImageAlt = null;
let photographerName = null;
let photographerLink = null;
let downloadTrackUrl = null;

if (result && result.urls && result.urls.regular) {
  heroImageUrl = result.urls.regular;
  heroImageAlt = parsed.title; // Spanish, SEO-relevant alt text, not Unsplash's own (often English/generic)
  photographerName = result.user && result.user.name ? result.user.name : null;
  photographerLink = result.user && result.user.links ? result.user.links.html : null;
  downloadTrackUrl = result.links ? result.links.download_location : null;
}

return [{
  json: {
    ...parsed,
    heroImageUrl,
    heroImageAlt,
    photographerName,
    photographerLink,
    downloadTrackUrl,
  },
}];
""".strip("\n")

SPLICE_CARD_CODE = r"""
const build = $input.first().json;

const marker = '<!-- NEXT_ARTICLE_CARD -->';
const currentContent = build.blogIndexContent;

if (!currentContent || !currentContent.includes(marker)) {
  throw new Error('No se encontró el marcador "' + marker + '" en blog/index.html. Añádelo manualmente una vez, justo dentro de <div class="blog-grid">, y vuelve a ejecutar.');
}

const updatedContent = currentContent.replace(marker, marker + build.cardHtml);

return [{
  json: {
    ...build,
    githubPutBodyBlogIndex: {
      message: 'Blog: publica "' + build.title + '" (automático)',
      content: Buffer.from(updatedContent, 'utf8').toString('base64'),
      sha: build.blogIndexSha,
      branch: build.githubBranch,
    },
  },
}];
""".strip("\n")

SPLICE_SITEMAP_CODE = r"""
const build = $('Splice card into blog index').first().json;
const getResp = $input.first().json;

const closeTag = '</urlset>';
const currentContent = Buffer.from(getResp.content.replace(/\n/g, ''), 'base64').toString('utf8');

if (!currentContent.includes(closeTag)) {
  throw new Error('No se encontró "</urlset>" en sitemap.xml. Revisa el fichero manualmente.');
}

const updatedContent = currentContent.replace(closeTag, build.sitemapEntry + closeTag);

return [{
  json: {
    ...build,
    githubPutBodySitemap: {
      message: 'Sitemap: añade ' + build.slug + ' (automático)',
      content: Buffer.from(updatedContent, 'utf8').toString('base64'),
      sha: getResp.sha,
      branch: build.githubBranch,
    },
    githubPutBodyArticle: {
      message: 'Blog: crea articulo ' + build.slug + ' (automático)',
      content: build.articleHtmlBase64,
      branch: build.githubBranch,
    },
  },
}];
""".strip("\n")

code_map = {
    "__PHONE_ICON__": PHONE_ICON,
    "__WHATSAPP_ICON__": WHATSAPP_ICON,
    "__WHATSAPP_ICON_BIG__": WHATSAPP_ICON_BIG,
    "__WHATSAPP_HREF__": WHATSAPP_HREF,
}
for k, v in code_map.items():
    BUILD_HTML_CODE = BUILD_HTML_CODE.replace(k, v.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${"))


def http_headers(pairs):
    return {"parameters": [{"name": n, "value": v} for n, v in pairs]}


nodes = []
connections = {}


def add_node(name, ntype, type_version, parameters, position, credentials=None, disabled=False):
    node = {
        "parameters": parameters,
        "id": name.lower().replace(" ", "-").replace("(", "").replace(")", "").replace("&", "and").replace("/", "-").replace(".", ""),
        "name": name,
        "type": ntype,
        "typeVersion": type_version,
        "position": position,
    }
    if credentials:
        node["credentials"] = credentials
    if disabled:
        node["disabled"] = True
    nodes.append(node)
    return name


def connect(src, dst, src_output=0):
    connections.setdefault(src, {"main": []})
    while len(connections[src]["main"]) <= src_output:
        connections[src]["main"].append([])
    connections[src]["main"][src_output].append({"node": dst, "type": "main", "index": 0})


X = 0
STEP = 260

n1 = add_node(
    "Weekly Trigger", "n8n-nodes-base.scheduleTrigger", 1.2,
    {"rule": {"interval": [{"field": "cronExpression", "expression": "0 9 * * 1"}]}},
    [X, 300],
)
X += STEP

n2 = add_node(
    "Config & Content Bank", "n8n-nodes-base.code", 2,
    {"mode": "runOnceForAllItems", "jsCode": CONFIG_CODE},
    [X, 300],
)
X += STEP

GITHUB_HEADERS = [("Accept", "application/vnd.github+json"), ("X-GitHub-Api-Version", "2022-11-28")]
GH_CRED = {"githubApi": {"id": "REPLACE_ME", "name": "GitHub API Token"}}

n3 = add_node(
    "GitHub - Get blog index", "n8n-nodes-base.httpRequest", 4.2,
    {
        "method": "GET",
        "url": "=https://api.github.com/repos/{{$json.githubOwner}}/{{$json.githubRepo}}/contents/{{$json.basePath}}blog/index.html?ref={{$json.githubBranch}}",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "githubApi",
        "sendHeaders": True,
        "headerParameters": http_headers(GITHUB_HEADERS),
        "options": {},
    },
    [X, 300], credentials=GH_CRED,
)
X += STEP

n4 = add_node(
    "Build OpenAI Prompt", "n8n-nodes-base.code", 2,
    {"mode": "runOnceForAllItems", "jsCode": BUILD_PROMPT_CODE},
    [X, 300],
)
X += STEP

n5 = add_node(
    "OpenAI - Generate Article", "n8n-nodes-base.httpRequest", 4.2,
    {
        "method": "POST",
        "url": "https://api.openai.com/v1/chat/completions",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": True,
        "headerParameters": http_headers([("Content-Type", "application/json")]),
        "sendBody": True,
        "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify($json.openaiBody) }}",
        "options": {},
    },
    [X, 300],
    credentials={"httpHeaderAuth": {"id": "REPLACE_ME", "name": "OpenAI API Key"}},
)
X += STEP

n6 = add_node(
    "Parse OpenAI Response", "n8n-nodes-base.code", 2,
    {"mode": "runOnceForAllItems", "jsCode": PARSE_OPENAI_CODE},
    [X, 300],
)
X += STEP

n_search_photo = add_node(
    "Unsplash - Search Photo", "n8n-nodes-base.httpRequest", 4.2,
    {
        "method": "GET",
        "url": "=https://api.unsplash.com/search/photos?query={{encodeURIComponent($json.image_keywords || 'moving boxes')}}&per_page=1&orientation=landscape",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": True,
        "headerParameters": http_headers([("Accept-Version", "v1")]),
        "options": {},
        "onError": "continueRegularOutput",
    },
    [X, 300],
    credentials={"httpHeaderAuth": {"id": "REPLACE_ME", "name": "Unsplash Access Key"}},
)
X += STEP

n_pick_photo = add_node(
    "Pick Photo", "n8n-nodes-base.code", 2,
    {"mode": "runOnceForAllItems", "jsCode": PICK_PHOTO_CODE},
    [X, 300],
)
X += STEP

n_track_download = add_node(
    "Unsplash - Track Download", "n8n-nodes-base.httpRequest", 4.2,
    {
        "method": "GET",
        "url": "={{ $json.downloadTrackUrl || 'https://api.unsplash.com' }}",
        "authentication": "genericCredentialType",
        "genericAuthType": "httpHeaderAuth",
        "sendHeaders": True,
        "headerParameters": http_headers([("Accept-Version", "v1")]),
        "options": {},
        "onError": "continueRegularOutput",
    },
    [X, 460],
    credentials={"httpHeaderAuth": {"id": "REPLACE_ME", "name": "Unsplash Access Key"}},
)
X += STEP

n7 = add_node(
    "Build HTML", "n8n-nodes-base.code", 2,
    {"mode": "runOnceForAllItems", "jsCode": BUILD_HTML_CODE},
    [X, 300],
)
X += STEP

n8 = add_node(
    "Splice card into blog index", "n8n-nodes-base.code", 2,
    {"mode": "runOnceForAllItems", "jsCode": SPLICE_CARD_CODE},
    [X, 300],
)
X += STEP

n9 = add_node(
    "GitHub - Update blog index", "n8n-nodes-base.httpRequest", 4.2,
    {
        "method": "PUT",
        "url": "=https://api.github.com/repos/{{$json.githubOwner}}/{{$json.githubRepo}}/contents/{{$json.blogIndexPath}}",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "githubApi",
        "sendHeaders": True,
        "headerParameters": http_headers(GITHUB_HEADERS),
        "sendBody": True,
        "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify($json.githubPutBodyBlogIndex) }}",
        "options": {},
    },
    [X, 300], credentials=GH_CRED,
)
X += STEP

n10 = add_node(
    "GitHub - Get sitemap", "n8n-nodes-base.httpRequest", 4.2,
    {
        "method": "GET",
        # NOTE: this node runs right after a GitHub PUT (an HTTP node), so
        # $json here is GitHub's PUT response, not our own data — it has no
        # githubOwner/sitemapPath fields. Reach back explicitly to a node
        # that still carries them instead of using bare $json.
        "url": "=https://api.github.com/repos/{{$('Build HTML').first().json.githubOwner}}/{{$('Build HTML').first().json.githubRepo}}/contents/{{$('Build HTML').first().json.sitemapPath}}?ref={{$('Build HTML').first().json.githubBranch}}",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "githubApi",
        "sendHeaders": True,
        "headerParameters": http_headers(GITHUB_HEADERS),
        "options": {},
    },
    [X, 300], credentials=GH_CRED,
)
X += STEP

n11 = add_node(
    "Splice sitemap entry", "n8n-nodes-base.code", 2,
    {"mode": "runOnceForAllItems", "jsCode": SPLICE_SITEMAP_CODE},
    [X, 300],
)
X += STEP

n12 = add_node(
    "GitHub - Update sitemap", "n8n-nodes-base.httpRequest", 4.2,
    {
        "method": "PUT",
        "url": "=https://api.github.com/repos/{{$json.githubOwner}}/{{$json.githubRepo}}/contents/{{$json.sitemapPath}}",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "githubApi",
        "sendHeaders": True,
        "headerParameters": http_headers(GITHUB_HEADERS),
        "sendBody": True,
        "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify($json.githubPutBodySitemap) }}",
        "options": {},
    },
    [X, 300], credentials=GH_CRED,
)
X += STEP

n13 = add_node(
    "GitHub - Create article file", "n8n-nodes-base.httpRequest", 4.2,
    {
        "method": "PUT",
        # Same reasoning as "GitHub - Get sitemap" above: this runs right
        # after the "GitHub - Update sitemap" PUT, so $json is that PUT's
        # response, not our data. Reach back to "Splice sitemap entry".
        "url": "=https://api.github.com/repos/{{$('Splice sitemap entry').first().json.githubOwner}}/{{$('Splice sitemap entry').first().json.githubRepo}}/contents/{{$('Splice sitemap entry').first().json.articlePath}}",
        "authentication": "predefinedCredentialType",
        "nodeCredentialType": "githubApi",
        "sendHeaders": True,
        "headerParameters": http_headers(GITHUB_HEADERS),
        "sendBody": True,
        "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify($('Splice sitemap entry').first().json.githubPutBodyArticle) }}",
        "options": {},
    },
    [X, 300], credentials=GH_CRED,
)
X += STEP

n14 = add_node(
    "Notify (optional - configure and enable)", "n8n-nodes-base.httpRequest", 4.2,
    {
        "method": "POST",
        "url": "https://hooks.slack.com/services/REPLACE/WITH/YOUR_WEBHOOK",
        "sendBody": True,
        "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify({ text: 'Nuevo articulo publicado: ' + $('Build HTML').first().json.title + ' -> ' + $('Build HTML').first().json.siteUrl + '/blog/' + $('Build HTML').first().json.slug + '.html' }) }}",
        "options": {},
    },
    [X, 300], disabled=True,
)

for a, b in [
    (n1, n2), (n2, n3), (n3, n4), (n4, n5), (n5, n6),
    (n6, n_search_photo), (n_search_photo, n_pick_photo), (n_pick_photo, n7),
    (n_pick_photo, n_track_download),  # side branch, does not gate the main chain
    (n7, n8), (n8, n9), (n9, n10), (n10, n11), (n11, n12), (n12, n13), (n13, n14),
]:
    connect(a, b)

workflow = {
    "name": "Blog semanal Mallorca Transportes (OpenAI + GitHub)",
    "nodes": nodes,
    "connections": connections,
    "active": False,
    "settings": {"executionOrder": "v1"},
    "versionId": "1",
    "meta": {"instanceId": "mallorca-transportes-blog-automation"},
    "tags": [],
}

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(workflow, f, ensure_ascii=False, indent=2)

print("Written:", OUT)
print("Nodes:", len(nodes))

# sanity: reparse
with open(OUT, encoding="utf-8") as f:
    json.load(f)
print("JSON re-parses OK")
