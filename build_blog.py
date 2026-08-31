# -*- coding: utf-8 -*-
import os

BASE = r"C:\Users\ray\Downloads\Transportes Mallorca-20260831T124637Z-1-001\website"
BLOG_DIR = os.path.join(BASE, "blog")
os.makedirs(BLOG_DIR, exist_ok=True)

SITE_URL = "https://mallorcatransportes.com"

WHATSAPP_HREF = "https://wa.me/34659924515?text=Hola%2C%20me%20gustar%C3%ADa%20pedir%20presupuesto%20para%20una%20mudanza%2Ftransporte%20en%20Mallorca"

PHONE_ICON = '<svg class="icon" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.3 1.1L6.6 10.8z"/></svg>'
WHATSAPP_ICON = '<svg class="icon" viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.7-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5C10 9 9.4 7.6 9.2 7c-.2-.5-.4-.5-.6-.5h-.5c-.2 0-.5.1-.7.3-.2.3-1 1-1 2.4s1 2.8 1.1 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.5-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.5-.3z"/><path d="M12 2C6.5 2 2 6.5 2 12c0 1.9.5 3.7 1.5 5.3L2 22l4.8-1.5c1.5.8 3.3 1.3 5.2 1.3 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.1c-1.7 0-3.3-.5-4.7-1.3l-.3-.2-3.2 1 1-3.1-.2-.3C3.7 14.7 3.2 13.4 3.2 12c0-4.8 3.9-8.7 8.8-8.7s8.8 3.9 8.8 8.7-4 8.1-8.8 8.1z"/></svg>'


def head(title, description, canonical_path, og_image, extra_schema=""):
    return """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="index, follow">
<meta name="author" content="Mallorca Transportes - Carrefusta, SLU">
<link rel="canonical" href="{canonical}">

<meta property="og:type" content="article">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Mallorca Transportes">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{og_image}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">

<link rel="icon" type="image/png" sizes="32x32" href="{rel}img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{rel}img/favicon-192.png">
<link rel="apple-touch-icon" href="{rel}img/apple-touch-icon.png">
<meta name="theme-color" content="#FF7300">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}css/styles.css">
{extra_schema}""".format(title=title, description=description, canonical=canonical_path, og_image=og_image, rel="../", extra_schema=extra_schema)


def header(rel, active="", breadcrumb_html=""):
    def h(path, anchor=""):
        if path == "index" and anchor:
            return (rel + "index.html#" + anchor) if rel else ("#" + anchor)
        if path == "index":
            return (rel + "index.html") if rel else "#top"
        if path == "blog":
            return "index.html" if rel else "blog/index.html"
        return path

    nav_links = [
        ("Servicios", h("index", "servicios")),
        ("Cobertura", h("index", "cobertura")),
        ("Trabajos", h("index", "trabajos")),
        ("Opiniones", h("index", "opiniones")),
        ("Blog", h("blog")),
        ("FAQ", h("index", "faq")),
        ("Contacto", h("index", "contacto")),
    ]
    nav_html = "\n      ".join('<a href="{}">{}</a>'.format(href, label) for label, href in nav_links)

    return """<a class="skip-link" href="#contenido">Saltar al contenido</a>

<header class="site-header" id="top">
  <div class="container header-inner">
    <a href="{home}" class="brand" aria-label="Mallorca Transportes - Inicio">
      <img src="{rel}img/logo.svg" alt="Mallorca Transportes" class="brand-logo" width="220" height="50">
    </a>

    <nav class="main-nav" id="main-nav" aria-label="Navegación principal">
      {nav_html}
    </nav>

    <div class="header-actions">
      <a href="tel:+34659924515" class="btn btn-ghost btn-sm header-call">
        {phone_icon}
        <span>659 924 515</span>
      </a>
      <a href="{wa}" class="btn btn-primary btn-sm" target="_blank" rel="noopener">
        {wa_icon}
        <span>WhatsApp</span>
      </a>
      <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="main-nav" aria-label="Abrir menú">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
""".format(home=h("index"), rel=rel, nav_html=nav_html, phone_icon=PHONE_ICON, wa=WHATSAPP_HREF, wa_icon=WHATSAPP_ICON)


def footer(rel):
    def h(anchor):
        return (rel + "index.html#" + anchor) if rel else ("#" + anchor)
    blog_href = "index.html" if rel else "blog/index.html"
    home_href = (rel + "index.html") if rel else "#top"

    return """<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img src="{rel}img/logo.svg" alt="Mallorca Transportes" class="footer-logo" width="200" height="46">
      <p>Especialistas en mudanzas y transporte de muebles en Mallorca desde hace más de 15 años. Servicio para particulares y empresas en toda la isla.</p>
    </div>
    <div class="footer-col">
      <h4>Servicios</h4>
      <ul>
        <li><a href="{servicios}">Mudanzas de hogar</a></li>
        <li><a href="{servicios}">Mudanzas de empresa</a></li>
        <li><a href="{servicios}">Transporte de muebles</a></li>
        <li><a href="{servicios}">Desmontaje y montaje</a></li>
        <li><a href="{servicios}">Transporte entre islas</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Contacto</h4>
      <ul>
        <li><a href="tel:+34659924515">+34 659 924 515</a></li>
        <li><a href="mailto:info@mallorcatransportes.com">info@mallorcatransportes.com</a></li>
        <li>Isla de Mallorca, España</li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Empresa</h4>
      <ul>
        <li><a href="{cobertura}">Cobertura</a></li>
        <li><a href="{trabajos}">Trabajos realizados</a></li>
        <li><a href="{opiniones}">Opiniones</a></li>
        <li><a href="{blog}">Blog</a></li>
        <li><a href="{faq}">Preguntas frecuentes</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>© 2026 Mallorca Transportes. Todos los derechos reservados. Carrefusta, SLU.</p>
  </div>
</footer>

<a href="{wa}" class="whatsapp-float" target="_blank" rel="noopener" aria-label="Contactar por WhatsApp">
  {wa_icon_big}
</a>

<div class="mobile-cta-bar">
  <a href="tel:+34659924515" class="mobile-cta-btn call">
    {phone_icon}
    Llamar
  </a>
  <a href="{wa}" class="mobile-cta-btn whatsapp" target="_blank" rel="noopener">
    {wa_icon}
    WhatsApp
  </a>
  <a href="{contacto}" class="mobile-cta-btn quote">Presupuesto</a>
</div>

<script src="{rel}js/main.js"></script>
</body>
</html>
""".format(
        rel=rel, wa=WHATSAPP_HREF,
        wa_icon_big=WHATSAPP_ICON.replace('class="icon" ', ''),
        wa_icon=WHATSAPP_ICON, phone_icon=PHONE_ICON,
        servicios=h("servicios"), cobertura=h("cobertura"), trabajos=h("trabajos"),
        opiniones=h("opiniones"), faq=h("faq"), contacto=h("contacto"),
        blog=blog_href,
    )


ARTICLES = [
    dict(
        slug="transporte-empresas-mallorca",
        title="Transporte profesional para empresas en Mallorca: soluciones a medida para tu negocio",
        description="Descubre cómo Mallorca Transportes ayuda a empresas de todos los sectores a mover mobiliario, equipos y material de oficina en Mallorca con rapidez y seguridad.",
        tags=["Transporte para empresas Mallorca", "Logística de mobiliario profesional", "Transporte comercial"],
        image="equipo-mudanzas-mallorca.jpg",
        image_alt="Equipo de Mallorca Transportes cargando material para una empresa",
        date="2026-08-28",
        read_min=4,
        body="""
<p><strong>¿Tienes un negocio en Mallorca y necesitas mover mobiliario, equipos o material de trabajo?</strong> En Mallorca Transportes ofrecemos un servicio especializado para empresas que buscan soluciones logísticas rápidas, cuidadosas y adaptadas a sus necesidades, sin interrumpir la actividad diaria.</p>

<h2>Transporte para empresas de cualquier sector</h2>
<p>En los últimos años hemos ayudado a decenas de empresas en Mallorca a realizar mudanzas y traslados internos sin frenar su facturación. Algunos de los sectores con los que trabajamos habitualmente:</p>
<ul>
  <li>Oficinas y despachos profesionales</li>
  <li>Clínicas y centros médicos</li>
  <li>Tiendas y comercios</li>
  <li>Restaurantes y cafeterías</li>
  <li>Empresas de reformas e interiorismo</li>
  <li>Inmobiliarias y promotoras</li>
</ul>
<p>Sabemos que el tiempo es oro para tu negocio, por eso priorizamos la puntualidad y la eficiencia en cada servicio.</p>

<h2>¿Qué incluye nuestro servicio de transporte profesional?</h2>
<ul>
  <li>Embalaje y protección de mobiliario y material sensible</li>
  <li>Carga y descarga segura, con personal especializado</li>
  <li>Transporte en vehículos adaptados</li>
  <li>Refuerzo con operarios extra cuando el volumen lo requiere</li>
  <li>Posibilidad de trabajar fuera del horario comercial</li>
  <li>Seguro incluido en cada servicio</li>
</ul>
<p>También ofrecemos <strong>servicios recurrentes o puntuales</strong>, según lo que necesite tu empresa.</p>

<h2>¿Tienes una reforma o un cambio de local?</h2>
<p>Si vas a renovar tu oficina o trasladar tu tienda a otro punto de la isla, nuestro equipo se encarga de todo el proceso logístico para que tú puedas centrarte en tu negocio. Incluso podemos ayudarte a desmontar y volver a montar el mobiliario si así lo solicitas.</p>

<h2>Cobertura en toda Mallorca</h2>
<p>Damos servicio a empresas en Palma, Marratxí, Inca, Manacor, Calvià, Llucmajor y el resto de municipios de la isla. Nos desplazamos hasta donde estés, adaptándonos a la logística de tu edificio, local o almacén.</p>
""",
    ),
    dict(
        slug="consejos-transporte-muebles-mallorca",
        title="Consejos clave para organizar el transporte de tus muebles en Mallorca",
        description="Consejos prácticos para organizar un transporte de muebles eficiente, seguro y sin sorpresas en Mallorca, tanto para hogares como para empresas.",
        tags=["Transporte en Mallorca", "Logística profesional", "Mudanzas"],
        image="trabajo-mudanza-03.jpg",
        image_alt="Mueble embalado y protegido para transporte en Mallorca",
        date="2026-08-20",
        read_min=4,
        body="""
<p>¿Planeas mover muebles en Mallorca? En este artículo te damos consejos prácticos para organizar un transporte eficiente, seguro y sin sorpresas. Ideal para hogares, empresas o reformas.</p>

<h2>1. Mide antes de mover</h2>
<p>Antes de contratar el servicio, mide los muebles grandes y compáralos con los accesos: puertas, pasillos, ascensor y escaleras. Así podremos avisarte con antelación si hace falta desmontar alguna pieza.</p>

<h2>2. Protege lo frágil</h2>
<p>Cristales, espejos, electrodomésticos y piezas de madera noble necesitan protección específica. Utilizamos mantas de embalaje, film y esquineras para que lleguen a destino en perfecto estado.</p>

<h2>3. Vacía cajones y armarios</h2>
<p>Los muebles pesan menos y se manipulan con más seguridad si están vacíos. Además, evitas que el contenido se mueva o se dañe durante el trayecto.</p>

<h2>4. Planifica el horario</h2>
<p>En zonas con tráfico o calles estrechas, como el centro de Palma o los cascos antiguos de algunos pueblos, elegir bien la franja horaria facilita mucho la carga y descarga.</p>

<h2>5. Cuenta con profesionales para las piezas grandes</h2>
<p>Sofás, armarios, cocinas o electrodomésticos voluminosos requieren técnica y, a veces, desmontaje. Un equipo con experiencia reduce el riesgo de golpes en paredes, marcos de puertas y en el propio mueble.</p>

<h2>6. Pide un presupuesto cerrado</h2>
<p>Así evitas sorpresas de última hora. En Mallorca Transportes valoramos el volumen, la distancia y el acceso para darte un precio claro desde el primer momento.</p>

<p>Cada vez más personas y empresas confían en Mallorca Transportes para sus traslados de muebles en la isla. Si tienes dudas sobre tu caso concreto, escríbenos y te asesoramos sin compromiso.</p>
""",
    ),
    dict(
        slug="mudanza-por-donde-empezar",
        title="¿Te vas a mudar y no sabes por dónde empezar?",
        description="Checklist paso a paso para organizar tu mudanza en Mallorca: qué hacer semanas antes, los días previos y el mismo día del traslado.",
        tags=["Mudanzas", "Transporte de muebles", "Consejos útiles"],
        image="trabajo-mudanza-01.jpg",
        image_alt="Cajas de mudanza embaladas y listas para el transporte",
        date="2026-08-10",
        read_min=5,
        body="""
<p>Organiza tu mudanza en Mallorca paso a paso con este checklist práctico. Desde el embalaje hasta el transporte, te damos las claves para una mudanza sin estrés ni contratiempos.</p>

<h2>Entre 3 y 4 semanas antes</h2>
<ul>
  <li>Haz inventario de lo que te llevas y lo que vas a donar o tirar</li>
  <li>Pide presupuesto a la empresa de mudanzas con la fecha aproximada</li>
  <li>Reserva material de embalaje: cajas, film, papel burbuja y cinta</li>
  <li>Si hay muebles grandes, confirma si necesitarán desmontaje</li>
</ul>

<h2>La semana previa</h2>
<ul>
  <li>Empieza a embalar lo que menos usas: libros, decoración, ropa de temporada</li>
  <li>Etiqueta cada caja con la habitación de destino y el contenido</li>
  <li>Separa una "caja esencial" con lo que necesitarás el primer día en la nueva casa</li>
  <li>Confirma horario, acceso y disponibilidad de ascensor con la empresa de transporte</li>
</ul>

<h2>El día de la mudanza</h2>
<ul>
  <li>Ten las cajas cerradas y accesibles antes de que llegue el equipo</li>
  <li>Señala los muebles que necesitan más cuidado (frágiles, antigüedades)</li>
  <li>Revisa que no quede nada en armarios, cajones o el trastero</li>
  <li>Haz una última revisión de la vivienda antes de cerrar la puerta</li>
</ul>

<h2>Al llegar al nuevo hogar</h2>
<ul>
  <li>Indica al equipo dónde va cada mueble para evitar mover cosas dos veces</li>
  <li>Comprueba que no falte ni se haya dañado nada durante el traslado</li>
  <li>Empieza a desembalar por las habitaciones que más vas a usar: cocina y dormitorio</li>
</ul>

<p>Si prefieres no ocuparte de todo esto, en Mallorca Transportes nos encargamos del proceso completo, desde el embalaje hasta la colocación en destino. Pide tu presupuesto gratuito y empieza tu mudanza con buen pie.</p>
""",
    ),
    dict(
        slug="ahorrar-dinero-mudanza-mallorca",
        title="Cómo ahorrar dinero en tu mudanza en Mallorca sin perder calidad",
        description="7 consejos reales para ahorrar en tu mudanza en Mallorca sin renunciar a un servicio profesional y seguro.",
        tags=["Mudanzas", "Consejos útiles", "Mallorca"],
        image="trabajo-mudanza-02.jpg",
        image_alt="Cajas de mudanza organizadas para reducir costes de transporte",
        date="2026-07-30",
        read_min=4,
        body="""
<p>¿Quieres mudarte en Mallorca sin gastar de más? Aquí tienes 7 consejos reales para ahorrar en tu mudanza sin renunciar a un servicio profesional y seguro.</p>

<h2>1. Reserva con antelación</h2>
<p>Las fechas de última hora suelen ser más caras y con menos disponibilidad, sobre todo en temporada alta. Reservar con unas semanas de margen te da más flexibilidad de horario y, normalmente, mejor precio.</p>

<h2>2. Aligera antes de mudarte</h2>
<p>Cuanto menos volumen transportes, menos pagas. Aprovecha para vender, donar o reciclar lo que ya no usas antes de pedir presupuesto.</p>

<h2>3. Compara presupuestos cerrados</h2>
<p>Desconfía de precios "orientativos" que luego suben. Pide siempre un presupuesto cerrado que incluya carga, transporte y descarga, para comparar de forma justa.</p>

<h2>4. Evita las fechas punta</h2>
<p>Los fines de semana y los últimos días de mes suelen tener más demanda. Si tu situación lo permite, mudarte entre semana puede abaratar el servicio.</p>

<h2>5. Embala tú lo que puedas</h2>
<p>Si tienes tiempo, embalar ropa, libros y objetos no frágiles por tu cuenta reduce horas de trabajo del equipo, lo que se traduce en ahorro.</p>

<h2>6. Agrupa servicios</h2>
<p>Si necesitas desmontaje, transporte y montaje, contratarlo todo junto suele salir más económico que pedirlo por separado.</p>

<h2>7. Pregunta por mudanzas compartidas</h2>
<p>Para trayectos entre islas o traslados de poco volumen, compartir vehículo con otro cliente que va en la misma ruta puede reducir bastante el coste.</p>

<p>En Mallorca Transportes te asesoramos para encontrar el equilibrio entre precio y calidad, sin sorpresas en la factura final. Pide tu presupuesto gratuito y cuéntanos qué necesitas.</p>
""",
    ),
    dict(
        slug="transporte-muebles-empresas-puntualidad-seguridad",
        title="Transporte de muebles para empresas en Mallorca: puntualidad, seguridad y trato profesional",
        description="Por qué la puntualidad y la seguridad son claves en el transporte de muebles y equipamiento para empresas en Mallorca, y cómo lo resolvemos en Mallorca Transportes.",
        tags=["Empresas y oficinas", "Transporte de muebles", "Logística profesional"],
        image="camion-transporte-mallorca.jpg",
        image_alt="Camión de Mallorca Transportes para reparto de mobiliario a empresas",
        date="2026-07-18",
        read_min=4,
        body="""
<p>¿Necesitas transportar muebles o equipamiento de tu empresa en Mallorca? Descubre nuestro servicio profesional, rápido y adaptado a negocios.</p>

<h2>Por qué la puntualidad importa en el transporte para empresas</h2>
<p>Cuando el transporte forma parte de la operativa de un negocio —una tienda que recibe mobiliario nuevo, un restaurante que renueva su sala, una oficina que amplía puestos de trabajo— cada hora de retraso tiene un coste. Por eso trabajamos con horarios cerrados y confirmamos la franja de entrega con antelación.</p>

<h2>Seguridad en cada entrega</h2>
<p>El mobiliario de empresa suele ser una inversión importante: mesas de oficina, mostradores, estanterías a medida, maquinaria ligera o equipamiento de hostelería. Cada envío se embala y sujeta según el tipo de material, y todos nuestros servicios incluyen seguro de transporte.</p>

<h2>Un trato profesional, de principio a fin</h2>
<p>Nuestro equipo se coordina directamente contigo o con la persona responsable en destino, confirma accesos y horarios, y se adapta a las normas del edificio o centro comercial si es necesario (muelles de carga, horarios restringidos, permisos de acceso).</p>

<h2>Casos habituales que resolvemos</h2>
<ul>
  <li>Reparto e instalación de mobiliario nuevo en oficinas y locales comerciales</li>
  <li>Traslado de mobiliario entre distintas sedes de una misma empresa</li>
  <li>Transporte de material desde fábrica o proveedor hasta almacén</li>
  <li>Entregas puntuales de equipamiento para eventos o ferias</li>
</ul>

<p>Si tu empresa necesita un proveedor de transporte de confianza en Mallorca, contáctanos y te preparamos una propuesta ajustada a tu actividad.</p>
""",
    ),
    dict(
        slug="mudanzas-sin-ascensor-mallorca",
        title="Mudanzas sin ascensor en Mallorca: soluciones prácticas paso a paso",
        description="¿Tu mudanza en Mallorca es en un edificio sin ascensor? Te contamos cómo lo resolvemos de forma segura, sin dañar tus muebles ni las paredes.",
        tags=["Mudanzas", "Consejos útiles", "Mallorca"],
        image="trabajo-mudanza-06.jpg",
        image_alt="Desmontaje de mueble de madera para facilitar una mudanza sin ascensor",
        date="2026-07-05",
        read_min=4,
        body="""
<p>¿Tienes que mudarte en Mallorca pero tu edificio no tiene ascensor? Descubre cómo resolvemos este tipo de mudanzas de forma rápida, segura y sin dañar tus muebles.</p>

<h2>El reto de los edificios sin ascensor</h2>
<p>Es habitual en cascos antiguos como el centro de Palma, Sóller o Pollença: edificios con escaleras estrechas, sin ascensor o con accesos complicados. En estos casos, la planificación previa marca la diferencia entre una mudanza rápida y una llena de contratiempos.</p>

<h2>Cómo lo resolvemos</h2>
<ul>
  <li><strong>Visita o consulta previa:</strong> valoramos el acceso, el ancho de las escaleras y los muebles más voluminosos antes del día del traslado.</li>
  <li><strong>Desmontaje de piezas grandes:</strong> armarios, sofás y camas se desmontan cuando es necesario para poder subirlos o bajarlos con seguridad.</li>
  <li><strong>Refuerzo de personal:</strong> en pisos altos sin ascensor añadimos operarios extra para agilizar la carga y reducir el tiempo de trabajo.</li>
  <li><strong>Material de protección:</strong> mantas y esquineras para proteger paredes, barandillas y marcos de puertas durante la subida o bajada.</li>
  <li><strong>Uso de poleas o grúa cuando es necesario:</strong> para muebles muy grandes que no caben por la escalera, valoramos alternativas de acceso por ventana o balcón cuando el edificio lo permite.</li>
</ul>

<h2>Consejos si tu mudanza no tiene ascensor</h2>
<ul>
  <li>Avisa del número de plantas y de si hay ascensor al pedir presupuesto</li>
  <li>Prioriza aligerar cajas pesadas: reparte libros y objetos densos en varias cajas pequeñas</li>
  <li>Consulta si el mueble más grande cabe realmente por hueco de escalera antes del día D</li>
</ul>

<p>En Mallorca Transportes tenemos experiencia con este tipo de mudanzas en toda la isla. Cuéntanos los detalles de tu edificio y te preparamos un presupuesto gratuito, sin sorpresas el día del traslado.</p>
""",
    ),
]

MONTHS_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fmt_date(iso):
    y, m, d = iso.split("-")
    return "{} de {} de {}".format(int(d), MONTHS_ES[int(m) - 1], y)


def tag_row(tags):
    return "\n            ".join('<span class="tag-pill">{}</span>'.format(t) for t in tags)


def build_index():
    cards = []
    for a in ARTICLES:
        cards.append("""
        <article class="blog-card">
          <a href="{slug}.html" class="blog-card-image">
            <img src="../img/{image}" alt="{image_alt}" loading="lazy" width="900" height="563">
          </a>
          <div class="blog-card-body">
            <div class="tag-row">
              {tags}
            </div>
            <h3><a href="{slug}.html">{title}</a></h3>
            <p>{description}</p>
            <div class="blog-card-meta">
              <span>{date}</span>
              <a href="{slug}.html">Leer más →</a>
            </div>
          </div>
        </article>""".format(
            slug=a["slug"], image=a["image"], image_alt=a["image_alt"],
            tags=tag_row(a["tags"]), title=a["title"], description=a["description"],
            date=fmt_date(a["date"]),
        ))

    title = "Blog de Mudanzas y Transporte en Mallorca | Mallorca Transportes"
    description = "Consejos, guías y novedades sobre mudanzas, transporte de muebles y logística en Mallorca. Todo lo que necesitas saber antes de tu próximo traslado."
    canonical = SITE_URL + "/blog/"

    html = """<!doctype html>
<html lang="es">
<head>
""" + head(title, description, canonical, SITE_URL + "/img/og-image.jpg") + """
</head>
<body>

""" + header("../") + """

<main id="contenido">
  <section class="page-header">
    <div class="container">
      <p class="breadcrumb"><a href="../index.html">Inicio</a> <span aria-hidden="true">/</span> Blog</p>
      <h1>Blog de mudanzas y transporte en Mallorca</h1>
      <p class="section-lead">Consejos prácticos, guías paso a paso y novedades sobre mudanzas, transporte de muebles y logística en toda la isla.</p>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="blog-grid">
        <!-- NEXT_ARTICLE_CARD --><!-- automated weekly posts are inserted right after this comment, do not remove it -->""" + "".join(cards) + """
      </div>
    </div>
  </section>
</main>

""" + footer("../")

    with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def build_article(a, prev_a, next_a):
    title_tag = a["title"] + " | Blog Mallorca Transportes"
    canonical = SITE_URL + "/blog/" + a["slug"] + ".html"
    og_image = SITE_URL + "/img/" + a["image"]

    schema = """<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
  "description": "{description}",
  "image": "{image}",
  "datePublished": "{date}",
  "author": {{"@type": "Organization", "name": "Mallorca Transportes"}},
  "publisher": {{
    "@type": "Organization",
    "name": "Mallorca Transportes",
    "logo": {{"@type": "ImageObject", "url": "{site}/img/favicon-512.png"}}
  }},
  "mainEntityOfPage": "{canonical}"
}}
</script>""".format(title=a["title"].replace('"', '\\"'), description=a["description"].replace('"', '\\"'),
                     image=og_image, date=a["date"], canonical=canonical, site=SITE_URL)

    related = [x for x in ARTICLES if x["slug"] != a["slug"]][:3]
    related_cards = []
    for r in related:
        related_cards.append("""
        <article class="blog-card">
          <a href="{slug}.html" class="blog-card-image">
            <img src="../img/{image}" alt="{image_alt}" loading="lazy" width="900" height="563">
          </a>
          <div class="blog-card-body">
            <div class="tag-row">
              {tags}
            </div>
            <h3><a href="{slug}.html">{title}</a></h3>
            <div class="blog-card-meta">
              <span>{date}</span>
              <a href="{slug}.html">Leer más →</a>
            </div>
          </div>
        </article>""".format(
            slug=r["slug"], image=r["image"], image_alt=r["image_alt"],
            tags=tag_row(r["tags"]), title=r["title"], date=fmt_date(r["date"]),
        ))

    main_content = """<main id="contenido">
  <section class="page-header">
    <div class="container">
      <p class="breadcrumb"><a href="../index.html">Inicio</a> <span aria-hidden="true">/</span> <a href="index.html">Blog</a> <span aria-hidden="true">/</span> Artículo</p>
      <h1>{title}</h1>
      <div class="tag-row">
        {tags}
      </div>
      <div class="article-meta-row">
        <span>Mallorca Transportes</span>
        <span aria-hidden="true">·</span>
        <span>{date}</span>
        <span aria-hidden="true">·</span>
        <span>{read_min} min de lectura</span>
      </div>
    </div>
  </section>

  <div class="article-hero">
    <img src="../img/{image}" alt="{image_alt}" width="1600" height="700" fetchpriority="high">
  </div>

  <section class="section">
    <div class="container article-layout">
      <div class="article-body">
        {body}

        <div class="article-cta">
          <p>¿Quieres un presupuesto gratuito para tu mudanza o transporte en Mallorca?</p>
          <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <a href="tel:+34659924515" class="btn btn-primary">Llamar ahora</a>
            <a href="../index.html#contacto" class="btn btn-outline">Pedir presupuesto</a>
          </div>
        </div>

        <div class="related-articles">
          <h2>Artículos relacionados</h2>
          <div class="blog-grid">{related}
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
""".format(
        title=a["title"], tags=tag_row(a["tags"]), date=fmt_date(a["date"]),
        read_min=a["read_min"], image=a["image"], image_alt=a["image_alt"],
        body=a["body"], related="".join(related_cards),
    )

    html = ("""<!doctype html>
<html lang="es">
<head>
""" + head(title_tag, a["description"], canonical, og_image, extra_schema=schema) + """
</head>
<body>

""" + header("../") + "\n\n" + main_content + "\n" + footer("../"))

    with open(os.path.join(BLOG_DIR, a["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(html)


build_index()
for i, a in enumerate(ARTICLES):
    build_article(a, ARTICLES[i - 1] if i > 0 else None, ARTICLES[i + 1] if i < len(ARTICLES) - 1 else None)

print("Built blog/index.html +", len(ARTICLES), "articles")
