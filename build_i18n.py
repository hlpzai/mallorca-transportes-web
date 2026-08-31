# -*- coding: utf-8 -*-
"""Generates the homepage in 4 languages (es/en/de/zh) with proper hreflang
SEO tagging. es/ = site root, others live under /en/, /de/, /zh/.
"""
import json
import os

BASE = r"C:\Users\ray\Downloads\Transportes Mallorca-20260831T124637Z-1-001\website"
SITE_URL = "https://mallorcatransportes.com"

PHONE_E164 = "+34659924515"
PHONE_DISPLAY = "659 924 515"
EMAIL = "info@mallorcatransportes.com"

PHONE_ICON = '<svg class="icon" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.3 1.1L6.6 10.8z"/></svg>'
WHATSAPP_ICON = '<svg class="icon" viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.7-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5C10 9 9.4 7.6 9.2 7c-.2-.5-.4-.5-.6-.5h-.5c-.2 0-.5.1-.7.3-.2.3-1 1-1 2.4s1 2.8 1.1 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.5-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.5-.3z"/><path d="M12 2C6.5 2 2 6.5 2 12c0 1.9.5 3.7 1.5 5.3L2 22l4.8-1.5c1.5.8 3.3 1.3 5.2 1.3 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.1c-1.7 0-3.3-.5-4.7-1.3l-.3-.2-3.2 1 1-3.1-.2-.3C3.7 14.7 3.2 13.4 3.2 12c0-4.8 3.9-8.7 8.8-8.7s8.8 3.9 8.8 8.7-4 8.1-8.8 8.1z"/></svg>'
WHATSAPP_ICON_BIG = WHATSAPP_ICON.replace('class="icon" ', '')

CHECK_ICON_LI = None  # check-list bullets are pure CSS, no markup needed

LANG_META = {
    "es": {"path": "", "locale": "es_ES", "label": "ES"},
    "en": {"path": "en/", "locale": "en_GB", "label": "EN"},
    "de": {"path": "de/", "locale": "de_DE", "label": "DE"},
    "zh": {"path": "zh/", "locale": "zh_CN", "label": "中文"},
}
LANG_ORDER = ["es", "en", "de", "zh"]


def wa_url(text):
    import urllib.parse
    return "https://wa.me/34659924515?text=" + urllib.parse.quote(text, safe='')


ARIA = {
    "es": dict(nav="Navegación principal", menu="Abrir menú", prev="Opinión anterior", next="Siguiente opinión",
               service_link="Pedir presupuesto", whatsapp_float="Contactar por WhatsApp", home_suffix=" - Inicio"),
    "en": dict(nav="Main navigation", menu="Open menu", prev="Previous review", next="Next review",
               service_link="Get a quote", whatsapp_float="Contact us on WhatsApp", home_suffix=" - Home"),
    "de": dict(nav="Hauptnavigation", menu="Menü öffnen", prev="Vorherige Bewertung", next="Nächste Bewertung",
               service_link="Angebot anfordern", whatsapp_float="Über WhatsApp kontaktieren", home_suffix=" - Startseite"),
    "zh": dict(nav="主导航", menu="打开菜单", prev="上一条评价", next="下一条评价",
               service_link="获取报价", whatsapp_float="通过WhatsApp联系我们", home_suffix=" - 首页"),
}


# =============================================================================
# TRANSLATIONS
# =============================================================================
T = {}

# ---------------------------------------------------------------- SPANISH --
T["es"] = dict(
    meta_title="Mudanzas y Transporte de Muebles en Mallorca | Mallorca Transportes",
    meta_description="Empresa de mudanzas y transporte de muebles en Mallorca con más de 15 años de experiencia. Servicio rápido, seguro y económico para particulares y empresas. Presupuesto gratis en 24h. ☎ 659 924 515",
    meta_keywords="mudanzas Mallorca, transporte de muebles Mallorca, logística Mallorca, mudanzas Palma de Mallorca, empresa de mudanzas Mallorca, transporte entre islas Baleares, desmontaje de muebles Mallorca",
    og_description="Mudanzas y transporte de muebles en toda Mallorca. Más de 15 años de experiencia, servicio seguro y presupuesto gratuito. Llama o escribe por WhatsApp.",
    skip_link="Saltar al contenido",
    nav=dict(servicios="Servicios", opiniones="Opiniones", blog="Blog", contacto="Contacto"),
    header_whatsapp="WhatsApp",
    wa_generic="Hola, me gustaría pedir presupuesto para una mudanza/transporte en Mallorca",
    hero=dict(
        eyebrow="Empresa de mudanzas y transporte en Mallorca",
        h1_pre="Mudanzas y transporte de muebles en ", h1_accent="Mallorca", h1_post=", sin complicaciones",
        subtitle="Más de 15 años ayudando a familias y empresas a mudarse en toda la isla. Servicio rápido, seguro y con presupuesto gratuito, sin compromiso.",
        cta_call="Llamar ahora", cta_whatsapp="WhatsApp directo", cta_quote="Pedir presupuesto gratis →",
        stats=[("15+", "Años de experiencia"), ("1.500+", "Clientes satisfechos"), ("100+", "Servicios al mes"), ("100%", "Cobertura en Mallorca")],
    ),
    trust=["Transporte asegurado", "Presupuesto en 24h", "Cobertura en toda Mallorca", "Equipo propio y cualificado"],
    services_section=dict(eyebrow="Nuestros servicios", h2="Servicios de mudanzas y transporte en Mallorca",
                           lead="Soluciones de mudanza y logística adaptadas a cada necesidad, desde traslados completos de vivienda hasta transporte urgente de muebles y electrodomésticos."),
    services=[
        dict(title="Mudanzas de hogar", desc="Traslado completo de pisos, casas y apartamentos en Mallorca. Incluye muebles, cajas, electrodomésticos y objetos personales.", wa="Hola, me gustaría pedir presupuesto para una mudanza de hogar en Mallorca"),
        dict(title="Mudanzas de empresas y oficinas", desc="Traslado de oficinas, despachos, comercios y locales sin interrumpir tu actividad. Trabajamos fuera de horario si lo necesitas.", wa="Hola, me gustaría pedir presupuesto para una mudanza de empresa u oficina en Mallorca"),
        dict(title="Transporte de muebles y electrodomésticos", desc="Envíos puntuales de sofás, camas, armarios, cocinas y electrodomésticos con embalaje y protección profesional.", wa="Hola, me gustaría pedir presupuesto para transporte de muebles y electrodomésticos en Mallorca"),
        dict(title="Desmontaje y montaje de muebles", desc="Equipo especializado en desmontaje de armarios, cocinas y electrodomésticos, con montaje en el destino incluido.", wa="Hola, me gustaría pedir presupuesto para desmontaje y montaje de muebles en Mallorca"),
        dict(title="Mudanzas express", desc="Para traslados urgentes, pequeños o de última hora. Servicio ágil pensado para estudiantes y entregas puntuales.", wa="Hola, me gustaría pedir presupuesto para una mudanza express en Mallorca"),
        dict(title="Transporte entre Islas Baleares", desc="Rutas frecuentes entre Mallorca, Menorca, Ibiza y Formentera para mudanzas, cajas y mercancía.", wa="Hola, me gustaría pedir presupuesto para transporte entre islas Baleares en Mallorca"),
        dict(title="Alquiler de elevadores", desc="Elevador de muebles para plantas altas sin ascensor o con accesos complicados, con operario incluido.", wa="Hola, me gustaría pedir presupuesto para alquilar un elevador de muebles en Mallorca"),
        dict(title="Guardamuebles", desc="Almacenamos tus muebles y enseres el tiempo que necesites, en un espacio seguro y controlado.", wa="Hola, me gustaría pedir presupuesto para un guardamuebles en Mallorca"),
        dict(title="Mudanzas a o desde Península", desc="Traslados completos entre Mallorca y cualquier punto de la Península, puerta a puerta.", wa="Hola, me gustaría pedir presupuesto para una mudanza a o desde la Península en Mallorca"),
        dict(title="Alquiler de trasteros", desc="Espacios de almacenaje flexibles por días, meses o de forma indefinida, del tamaño que necesites.", wa="Hola, me gustaría pedir presupuesto para alquilar un trastero en Mallorca"),
        dict(title="Vaciado de naves y locales", desc="Desalojo completo de naves industriales, locales comerciales o almacenes, con gestión de residuos.", wa="Hola, me gustaría pedir presupuesto para el vaciado de una nave o local en Mallorca"),
        dict(title="Alquiler de camiones", desc="Camiones con y sin conductor para transportes puntuales de gran volumen.", wa="Hola, me gustaría pedir presupuesto para alquilar un camión en Mallorca"),
        dict(title="Alquiler de furgonetas", desc="Furgonetas de distintos tamaños disponibles por horas o días para tus propios traslados.", wa="Hola, me gustaría pedir presupuesto para alquilar una furgoneta en Mallorca"),
        dict(title="Embalaje profesional", desc="Material y técnica de embalaje para proteger tus objetos más delicados durante el transporte.", wa="Hola, me gustaría pedir presupuesto para servicio de embalaje profesional en Mallorca"),
    ],
    process=dict(eyebrow="Así trabajamos", h2="Fácil, rápido y profesional", cta="¿Listo para tu transporte? Solicita presupuesto",
                 steps=[("Solicita tu presupuesto", "Rellena el formulario o escríbenos por WhatsApp con los detalles de tu mudanza."),
                        ("Confirmación del servicio", "Acordamos fecha, horario y detalles del transporte contigo."),
                        ("Recogida y traslado seguro", "Recogemos tus objetos y los transportamos con cuidado y protección."),
                        ("Entrega en el punto acordado", "Todo llega a su destino en tiempo y forma, listo para colocar.")]),
    whyus=dict(eyebrow="Por qué elegirnos", h2="Tu mudanza en Mallorca, en manos de profesionales",
               lead="Somos una empresa local con más de 15 años de experiencia en mudanzas y transporte en Mallorca. Cuidamos cada detalle para que tu traslado sea rápido y sin sorpresas.",
               items=["Más de 15 años de experiencia en la isla", "Equipo propio, uniformado y con material de protección profesional",
                      "Transporte asegurado en cada servicio", "Presupuesto gratuito y sin compromiso",
                      "Puntualidad garantizada, también fuera de horario", "Atención cercana y personalizada, de principio a fin"],
               cta="Solicita tu presupuesto gratis", img_alt="Equipo de mudanzas cargando cajas en furgoneta en Mallorca"),
    coverage=dict(eyebrow="Zona de servicio", h2="Cobertura en toda Mallorca y las Islas Baleares",
                  lead="Realizamos mudanzas y transportes en todos los municipios de Mallorca, desde Palma hasta los pueblos más pequeños. También operamos rutas frecuentes entre islas.",
                  towns_h3="Municipios de Mallorca",
                  towns=["Palma de Mallorca", "Calvià", "Marratxí", "Llucmajor", "Inca", "Manacor", "Sóller", "Andratx", "Alcúdia", "Pollença", "Felanitx", "Y el resto de la isla"],
                  islands_h3="Transporte entre islas", routes=["Mallorca ⇄ Menorca", "Mallorca ⇄ Ibiza", "Mallorca ⇄ Formentera"],
                  islands_p="¿Necesitas enviar algo entre islas? Lo gestionamos por ti de principio a fin.", islands_cta="Consultar disponibilidad",
                  map_alt="Mapa de las Islas Baleares con las rutas de transporte entre Mallorca, Menorca, Ibiza y Formentera"),
    fleet=dict(eyebrow="Nuestra flota", h2="Vehículos adaptados a cada mudanza",
               lead="Disponemos de furgonetas y camiones de distintos tamaños para adaptarnos al volumen de tu mudanza o transporte, desde un envío puntual hasta una vivienda completa.",
               items=["Vehículos cerrados con protección para muebles y cajas", "Plataforma elevadora para cargas pesadas", "Flota propia disponible en toda la isla"],
               img_alt="Camión y furgoneta de la flota de Mallorca Transportes"),
    gallery=dict(eyebrow="Casos reales", h2="Mudanzas y transportes realizados en Mallorca",
                 lead="Algunos ejemplos de servicios de mudanza, embalaje y transporte de muebles realizados en toda la isla.",
                 alts=["Mudanza de vivienda con cajas embaladas en Mallorca", "Embalaje profesional de electrodomésticos para mudanza en Mallorca",
                       "Transporte de muebles de cocina en Mallorca", "Desmontaje y embalaje de mobiliario en mudanza de Mallorca",
                       "Instalación y montaje de cocina tras mudanza en Mallorca", "Montaje de mobiliario de madera en reforma en Mallorca"]),
    testimonials_section=dict(eyebrow="Opiniones", h2="Lo que dicen nuestros clientes"),
    testimonials=[
        dict(name="Alice Klein", role="Mudanza particular", quote="Excelente servicio de principio a fin. Contraté su servicio para mi mudanza y no puedo estar más satisfecha. Fueron puntuales, cuidadosos con cada mueble y muy organizados durante todo el proceso."),
        dict(name="David Romero", role="Transporte a empresa", quote="Necesitábamos trasladar mobiliario de oficina y documentación desde Manacor a nuestro nuevo local. El equipo fue rápido, eficiente y muy profesional. Todo el proceso fue fluido."),
        dict(name="Juan Pérez", role="Desmontaje y montaje de cocina", quote="Muy profesionales y rápidos en el desmontaje y traslado de muebles. Además de entregarme mi nueva cocina, desmontaron la cocina antigua que tenía para que yo no tuviera que preocuparme por tirarlos."),
        dict(name="Marc Vidal", role="Transporte de muebles", quote="Compré un sofá y una mesa en una tienda de segunda mano y ellos se encargaron de recogerlos y traerlos hasta casa. Todo sin una sola marca. Muy profesionales y cuidadosos."),
        dict(name="Sonia Mestre", role="Servicio entre islas", quote="Solicité el transporte de varios electrodomésticos desde Mallorca a Ibiza. Me mantuvieron informado en todo momento y cumplieron con los plazos. Muy recomendable si necesitas transporte interinsular."),
        dict(name="Lucía Fernández", role="Mudanza particular", quote="Contraté el servicio para una mudanza desde Inca a Palma. Fueron súper puntuales, muy cuidadosos con mis muebles y todo llegó en perfecto estado. Se nota que tienen experiencia. ¡Repetiría sin dudarlo!"),
        dict(name="Clara Ríos", role="Mudanza particular", quote="Tuve que hacer una mudanza urgente por cambio de piso. A pesar del poco tiempo, se adaptaron y me ayudaron con todo. Rápidos, eficaces y con muy buen trato. ¡Un 10!"),
        dict(name="Patricia Navarro", role="Mudanza particular", quote="Era la primera vez que contrataba un servicio de transporte y tenía muchas dudas. Me asesoraron desde el primer momento, fueron claros con el presupuesto y muy atentos durante todo el proceso. Recogieron mis cosas en Palma y las llevaron hasta mi nuevo piso en Alcúdia sin problemas. ¡Gracias por hacerlo tan fácil!"),
        dict(name="Javier Morales", role="Mudanza particular", quote="Contraté el servicio de transporte para mi mudanza y fue una experiencia excelente. Me ayudaron a mover todas mis cajas y muebles de forma segura y puntual. El conductor fue muy amable. ¡Muy recomendable para quien tiene que mudarse!"),
        dict(name="Carlos Hernández", role="Transporte a empresa", quote="Contraté el servicio de transporte para el traslado de muebles desde la fábrica a mi almacén, y la experiencia fue excelente. Fueron puntuales, cuidadosos y todo llegó en perfectas condiciones. Sin duda, los volveré a elegir para futuras entregas."),
    ],
    faq_section=dict(eyebrow="Preguntas frecuentes", h2="Resolvemos tus dudas"),
    faq=[
        ("¿Qué incluye el servicio de transporte o mudanza?", "Incluye la recogida, traslado y entrega de tus pertenencias en el destino acordado. También nos encargamos de la carga y descarga del vehículo."),
        ("¿Debo embalar mis objetos antes del transporte?", "No es obligatorio. Si lo prefieres, nuestro equipo puede encargarse del embalaje y protección de tus muebles y objetos frágiles."),
        ("¿Cómo se calcula el precio del servicio?", "El precio depende del volumen a transportar, la distancia, el acceso (ascensor, plantas) y si se necesita desmontaje. Te damos un presupuesto cerrado y sin sorpresas."),
        ("¿Pueden desmontar mis muebles grandes?", "Sí, contamos con un equipo especializado en desmontaje y montaje de armarios, cocinas y electrodomésticos."),
        ("¿Cuánto tiempo antes debo reservar?", "Recomendamos avisar con unos días de antelación, pero también ofrecemos mudanzas express para necesidades urgentes."),
        ("¿Puedo transportar cosas entre islas?", "Sí, operamos rutas entre Mallorca, Menorca, Ibiza y Formentera para mudanzas y mercancía."),
    ],
    final_cta=dict(h2="¿Listo para tu mudanza en Mallorca?", p="Pide tu presupuesto gratuito ahora mismo. Sin compromiso, respuesta rápida."),
    contact=dict(eyebrow="Contacto", h2="Pide tu presupuesto gratuito",
                 lead="Cuéntanos qué necesitas transportar y te responderemos lo antes posible. También puedes llamarnos o escribirnos directamente.",
                 call_label="Llámanos", email_label="Escríbenos", whatsapp_label="WhatsApp", whatsapp_sub="Respuesta rápida",
                 hours_label="Horario", hours1="Lunes a viernes: 8:00 – 20:00", hours2="Sábados y domingos: nos adaptamos en casos excepcionales",
                 form=dict(name="Nombre", phone="Teléfono", email="Correo electrónico", service_type="Tipo de servicio",
                           options=["Mudanza de hogar", "Mudanza de empresa/oficina", "Transporte de muebles", "Desmontaje y montaje", "Mudanza express", "Transporte entre islas", "Otro"],
                           message_label="Cuéntanos qué necesitas transportar", message_placeholder="Origen, destino, fecha aproximada, tipo de objetos...",
                           submit="Enviar solicitud de presupuesto"),
                 note_pre="Al enviar se abrirá tu aplicación de correo con los datos ya rellenados. Si lo prefieres, llámanos directamente al ", note_post="."),
    footer=dict(blurb="Especialistas en mudanzas y transporte de muebles en Mallorca desde hace más de 15 años. Servicio para particulares y empresas en toda la isla.",
                services_h4="Servicios", services_links=["Mudanzas de hogar", "Mudanzas de empresa", "Transporte de muebles", "Desmontaje y montaje", "Transporte entre islas"],
                contact_h4="Contacto", address="Isla de Mallorca, España",
                company_h4="Empresa", company_links=dict(coverage="Cobertura", jobs="Trabajos realizados", reviews="Opiniones", blog="Blog", faq="Preguntas frecuentes"),
                copyright="© 2026 Mallorca Transportes. Todos los derechos reservados. Carrefusta, SLU."),
)

# ----------------------------------------------------------------- ENGLISH --
T["en"] = dict(
    meta_title="Removals & Furniture Transport in Mallorca | Mallorca Transportes",
    meta_description="Removals and furniture transport company in Mallorca with over 15 years of experience. Fast, safe and affordable service for individuals and businesses. Free quote within 24h. ☎ +34 659 924 515",
    meta_keywords="removals Mallorca, furniture transport Mallorca, moving company Mallorca, movers Palma de Mallorca, logistics Mallorca, inter-island transport Balearic Islands, furniture dismantling Mallorca",
    og_description="Removals and furniture transport across Mallorca. Over 15 years of experience, insured service and a free quote. Call us or message on WhatsApp.",
    skip_link="Skip to content",
    nav=dict(servicios="Services", opiniones="Reviews", blog="Blog", contacto="Contact"),
    header_whatsapp="WhatsApp",
    wa_generic="Hi, I'd like to request a quote for a removal/transport in Mallorca",
    hero=dict(
        eyebrow="Removals and transport company in Mallorca",
        h1_pre="Removals and furniture transport in ", h1_accent="Mallorca", h1_post=", without the hassle",
        subtitle="Over 15 years helping families and businesses move across the island. Fast, safe service with a free, no-obligation quote.",
        cta_call="Call now", cta_whatsapp="WhatsApp direct", cta_quote="Get a free quote →",
        stats=[("15+", "Years of experience"), ("1,500+", "Satisfied clients"), ("100+", "Services per month"), ("100%", "Coverage in Mallorca")],
    ),
    trust=["Insured transport", "Quote within 24h", "Coverage across Mallorca", "Own, qualified team"],
    services_section=dict(eyebrow="Our services", h2="Removals and transport services in Mallorca",
                           lead="Removal and logistics solutions tailored to every need, from full home moves to urgent furniture and appliance transport."),
    services=[
        dict(title="Home removals", desc="Complete removal of flats, houses and apartments in Mallorca. Includes furniture, boxes, appliances and personal belongings.", wa="Hi, I'd like a quote for a home removal in Mallorca"),
        dict(title="Business & office removals", desc="Office, practice, shop and premises relocation without interrupting your activity. We can work outside business hours if needed.", wa="Hi, I'd like a quote for a business or office removal in Mallorca"),
        dict(title="Furniture & appliance transport", desc="One-off deliveries of sofas, beds, wardrobes, kitchens and appliances with professional packing and protection.", wa="Hi, I'd like a quote for furniture and appliance transport in Mallorca"),
        dict(title="Furniture dismantling & assembly", desc="Specialist team for dismantling wardrobes, kitchens and appliances, with assembly at the destination included.", wa="Hi, I'd like a quote for furniture dismantling and assembly in Mallorca"),
        dict(title="Express removals", desc="For urgent, small or last-minute moves. An agile service designed for students and time-critical deliveries.", wa="Hi, I'd like a quote for an express removal in Mallorca"),
        dict(title="Transport between the Balearic Islands", desc="Frequent routes between Mallorca, Menorca, Ibiza and Formentera for removals, boxes and goods.", wa="Hi, I'd like a quote for transport between the Balearic Islands"),
        dict(title="Furniture lift rental", desc="Furniture lift for upper floors with no lift or difficult access, operator included.", wa="Hi, I'd like a quote to rent a furniture lift in Mallorca"),
        dict(title="Furniture storage", desc="We store your furniture and belongings for as long as you need, in a secure, controlled space.", wa="Hi, I'd like a quote for furniture storage in Mallorca"),
        dict(title="Removals to/from mainland Spain", desc="Full door-to-door moves between Mallorca and anywhere on mainland Spain.", wa="Hi, I'd like a quote for a removal to or from mainland Spain"),
        dict(title="Storage unit rental", desc="Flexible storage spaces by the day, month or indefinitely, in the size you need.", wa="Hi, I'd like a quote to rent a storage unit in Mallorca"),
        dict(title="Warehouse & premises clearance", desc="Full clearance of industrial units, shops or warehouses, including waste management.", wa="Hi, I'd like a quote for warehouse or premises clearance in Mallorca"),
        dict(title="Truck rental", desc="Trucks with or without a driver for one-off, large-volume transport.", wa="Hi, I'd like a quote to rent a truck in Mallorca"),
        dict(title="Van rental", desc="Vans of different sizes available by the hour or day for your own moves.", wa="Hi, I'd like a quote to rent a van in Mallorca"),
        dict(title="Professional packing", desc="Packing materials and technique to protect your most delicate belongings during transport.", wa="Hi, I'd like a quote for a professional packing service in Mallorca"),
    ],
    process=dict(eyebrow="How we work", h2="Easy, fast and professional", cta="Ready for your move? Request a quote",
                 steps=[("Request your quote", "Fill in the form or message us on WhatsApp with your removal details."),
                        ("Service confirmation", "We agree the date, time and transport details with you."),
                        ("Safe pickup and transport", "We collect your belongings and transport them with care and protection."),
                        ("Delivery at the agreed location", "Everything arrives on time and ready to be set up.")]),
    whyus=dict(eyebrow="Why choose us", h2="Your move in Mallorca, in professional hands",
               lead="We're a local company with over 15 years of experience in removals and transport in Mallorca. We take care of every detail so your move is fast and hassle-free.",
               items=["Over 15 years of experience on the island", "Own, uniformed team with professional protective equipment",
                      "Insured transport on every service", "Free, no-obligation quote",
                      "Punctuality guaranteed, even outside business hours", "Close, personal attention from start to finish"],
               cta="Get your free quote", img_alt="Mallorca Transportes team loading boxes into a van"),
    coverage=dict(eyebrow="Service area", h2="Coverage across all of Mallorca and the Balearic Islands",
                  lead="We carry out removals and transport in every municipality of Mallorca, from Palma to the smallest villages. We also run frequent inter-island routes.",
                  towns_h3="Municipalities of Mallorca",
                  towns=["Palma de Mallorca", "Calvià", "Marratxí", "Llucmajor", "Inca", "Manacor", "Sóller", "Andratx", "Alcúdia", "Pollença", "Felanitx", "And the rest of the island"],
                  islands_h3="Transport between islands", routes=["Mallorca ⇄ Menorca", "Mallorca ⇄ Ibiza", "Mallorca ⇄ Formentera"],
                  islands_p="Need to send something between islands? We handle it for you from start to finish.", islands_cta="Check availability",
                  map_alt="Map of the Balearic Islands with transport routes between Mallorca, Menorca, Ibiza and Formentera"),
    fleet=dict(eyebrow="Our fleet", h2="Vehicles suited to every move",
               lead="We have vans and trucks of different sizes to match the volume of your move or transport, from a single item to a full house.",
               items=["Enclosed vehicles with protection for furniture and boxes", "Lifting platform for heavy loads", "Own fleet available across the island"],
               img_alt="Truck and van from the Mallorca Transportes fleet"),
    gallery=dict(eyebrow="Real cases", h2="Removals and transport jobs completed in Mallorca",
                 lead="Some examples of removal, packing and furniture transport services carried out across the island.",
                 alts=["Home move with packed boxes in Mallorca", "Professional appliance packing for a move in Mallorca",
                       "Kitchen furniture transport in Mallorca", "Furniture dismantling and packing for a move in Mallorca",
                       "Kitchen installation and assembly after a move in Mallorca", "Wooden furniture assembly during a renovation in Mallorca"]),
    testimonials_section=dict(eyebrow="Reviews", h2="What our clients say"),
    testimonials=[
        dict(name="Alice Klein", role="Private removal", quote="Excellent service from start to finish. I hired them for my move and couldn't be happier. They were punctual, careful with every piece of furniture and very organised throughout."),
        dict(name="David Romero", role="Business transport", quote="We needed to move office furniture and documents from Manacor to our new premises. The team was fast, efficient and very professional. The whole process was smooth."),
        dict(name="Juan Pérez", role="Kitchen dismantling and assembly", quote="Very professional and fast dismantling and moving furniture. On top of delivering my new kitchen, they dismantled the old one so I didn't have to worry about disposing of it."),
        dict(name="Marc Vidal", role="Furniture transport", quote="I bought a sofa and a table from a second-hand shop and they picked them up and brought them home. No brand of their own involved. Very professional and careful."),
        dict(name="Sonia Mestre", role="Inter-island service", quote="I requested transport of several appliances from Mallorca to Ibiza. They kept me informed the whole time and met the deadlines. Highly recommended for inter-island transport."),
        dict(name="Lucía Fernández", role="Private removal", quote="I hired the service for a move from Inca to Palma. They were super punctual, very careful with my furniture and everything arrived in perfect condition. You can tell they have experience. I'd repeat without hesitation!"),
        dict(name="Clara Ríos", role="Private removal", quote="I had to move urgently because of a change of flat. Despite the short notice, they adapted and helped with everything. Fast, efficient and very friendly. A 10 out of 10!"),
        dict(name="Patricia Navarro", role="Private removal", quote="It was my first time hiring a transport service and I had a lot of doubts. They advised me from the very first moment, were clear about the price and very attentive throughout. They picked up my things in Palma and took them to my new flat in Alcúdia without any issues. Thanks for making it so easy!"),
        dict(name="Javier Morales", role="Private removal", quote="I hired the transport service for my move and it was an excellent experience. They helped me move all my boxes and furniture safely and on time. The driver was very kind. Highly recommended for anyone moving house!"),
        dict(name="Carlos Hernández", role="Business transport", quote="I hired the transport service to move furniture from the factory to my warehouse, and it was an excellent experience. They were punctual, careful and everything arrived in perfect condition. I'll definitely choose them again for future deliveries."),
    ],
    faq_section=dict(eyebrow="FAQ", h2="We answer your questions"),
    faq=[
        ("What does the transport or removal service include?", "It includes pickup, transport and delivery of your belongings to the agreed destination. We also handle loading and unloading the vehicle."),
        ("Do I need to pack my belongings before transport?", "It's not compulsory. If you prefer, our team can take care of packing and protecting your furniture and fragile items."),
        ("How is the price of the service calculated?", "The price depends on the volume to be transported, the distance, access (lift, floors) and whether dismantling is required. We give you a fixed quote with no surprises."),
        ("Can you dismantle my large furniture?", "Yes, we have a team specialised in dismantling and assembling wardrobes, kitchens and appliances."),
        ("How far in advance should I book?", "We recommend booking a few days in advance, but we also offer express removals for urgent needs."),
        ("Can I transport things between islands?", "Yes, we operate routes between Mallorca, Menorca, Ibiza and Formentera for removals and goods."),
    ],
    final_cta=dict(h2="Ready for your move in Mallorca?", p="Get your free quote right now. No obligation, fast response."),
    contact=dict(eyebrow="Contact", h2="Get your free quote",
                 lead="Tell us what you need to transport and we'll get back to you as soon as possible. You can also call or message us directly.",
                 call_label="Call us", email_label="Email us", whatsapp_label="WhatsApp", whatsapp_sub="Fast response",
                 hours_label="Opening hours", hours1="Monday to Friday: 8:00 – 20:00", hours2="Saturdays and Sundays: we accommodate exceptional cases",
                 form=dict(name="Name", phone="Phone", email="Email", service_type="Type of service",
                           options=["Home removal", "Business/office removal", "Furniture transport", "Dismantling and assembly", "Express removal", "Inter-island transport", "Other"],
                           message_label="Tell us what you need transported", message_placeholder="Origin, destination, approximate date, type of items...",
                           submit="Send quote request"),
                 note_pre="By submitting, your email app will open with the details already filled in. If you prefer, call us directly on ", note_post="."),
    footer=dict(blurb="Removals and furniture transport specialists in Mallorca for over 15 years. Service for individuals and businesses across the island.",
                services_h4="Services", services_links=["Home removals", "Business removals", "Furniture transport", "Dismantling and assembly", "Inter-island transport"],
                contact_h4="Contact", address="Island of Mallorca, Spain",
                company_h4="Company", company_links=dict(coverage="Coverage", jobs="Completed jobs", reviews="Reviews", blog="Blog", faq="FAQ"),
                copyright="© 2026 Mallorca Transportes. All rights reserved. Carrefusta, SLU."),
)

# ------------------------------------------------------------------ GERMAN --
T["de"] = dict(
    meta_title="Umzüge & Möbeltransport auf Mallorca | Mallorca Transportes",
    meta_description="Umzugsunternehmen und Möbeltransport auf Mallorca mit über 15 Jahren Erfahrung. Schneller, sicherer und günstiger Service für Privat- und Geschäftskunden. Kostenloses Angebot innerhalb von 24 Std. ☎ +34 659 924 515",
    meta_keywords="Umzug Mallorca, Möbeltransport Mallorca, Umzugsunternehmen Mallorca, Umzugsfirma Palma de Mallorca, Logistik Mallorca, Transport zwischen den Balearen, Möbelmontage Mallorca",
    og_description="Umzüge und Möbeltransport auf ganz Mallorca. Über 15 Jahre Erfahrung, versicherter Service und kostenloses Angebot. Rufen Sie an oder schreiben Sie uns per WhatsApp.",
    skip_link="Zum Inhalt springen",
    nav=dict(servicios="Leistungen", opiniones="Bewertungen", blog="Blog", contacto="Kontakt"),
    header_whatsapp="WhatsApp",
    wa_generic="Hallo, ich hätte gerne ein Angebot für einen Umzug/Transport auf Mallorca",
    hero=dict(
        eyebrow="Umzugs- und Transportunternehmen auf Mallorca",
        h1_pre="Umzüge und Möbeltransport auf ", h1_accent="Mallorca", h1_post=" – ganz ohne Stress",
        subtitle="Seit über 15 Jahren helfen wir Familien und Unternehmen beim Umzug auf der ganzen Insel. Schneller, sicherer Service mit kostenlosem, unverbindlichem Angebot.",
        cta_call="Jetzt anrufen", cta_whatsapp="Direkt per WhatsApp", cta_quote="Kostenloses Angebot anfordern →",
        stats=[("15+", "Jahre Erfahrung"), ("1.500+", "Zufriedene Kunden"), ("100+", "Aufträge pro Monat"), ("100%", "Abdeckung auf Mallorca")],
    ),
    trust=["Versicherter Transport", "Angebot in 24 Std.", "Abdeckung auf ganz Mallorca", "Eigenes, qualifiziertes Team"],
    services_section=dict(eyebrow="Unsere Leistungen", h2="Umzugs- und Transportdienstleistungen auf Mallorca",
                           lead="Umzugs- und Logistiklösungen für jeden Bedarf – vom kompletten Wohnungsumzug bis zum dringenden Transport von Möbeln und Elektrogeräten."),
    services=[
        dict(title="Privatumzüge", desc="Kompletter Umzug von Wohnungen, Häusern und Apartments auf Mallorca. Inklusive Möbel, Kartons, Elektrogeräte und persönliche Gegenstände.", wa="Hallo, ich hätte gerne ein Angebot für einen Privatumzug auf Mallorca"),
        dict(title="Firmen- und Büroumzüge", desc="Umzug von Büros, Praxen, Geschäften und Gewerberäumen, ohne Ihren Betrieb zu unterbrechen. Auf Wunsch auch außerhalb der Geschäftszeiten.", wa="Hallo, ich hätte gerne ein Angebot für einen Firmen- oder Büroumzug auf Mallorca"),
        dict(title="Möbel- und Elektrogerätetransport", desc="Einzeltransporte von Sofas, Betten, Schränken, Küchen und Elektrogeräten mit professioneller Verpackung und Schutz.", wa="Hallo, ich hätte gerne ein Angebot für den Transport von Möbeln und Elektrogeräten auf Mallorca"),
        dict(title="Möbelmontage und -demontage", desc="Spezialisiertes Team für die Demontage von Schränken, Küchen und Elektrogeräten, inklusive Montage am Zielort.", wa="Hallo, ich hätte gerne ein Angebot für Möbelmontage und -demontage auf Mallorca"),
        dict(title="Express-Umzüge", desc="Für dringende, kleine oder kurzfristige Umzüge. Flexibler Service, ideal für Studenten und termingebundene Lieferungen.", wa="Hallo, ich hätte gerne ein Angebot für einen Express-Umzug auf Mallorca"),
        dict(title="Transport zwischen den Balearen-Inseln", desc="Regelmäßige Verbindungen zwischen Mallorca, Menorca, Ibiza und Formentera für Umzüge, Kartons und Waren.", wa="Hallo, ich hätte gerne ein Angebot für Transport zwischen den Balearen-Inseln"),
        dict(title="Möbellift-Vermietung", desc="Möbellift für obere Stockwerke ohne Aufzug oder mit schwierigem Zugang, inklusive Bedienpersonal.", wa="Hallo, ich hätte gerne ein Angebot zur Miete eines Möbellifts auf Mallorca"),
        dict(title="Möbeleinlagerung", desc="Wir lagern Ihre Möbel und Gegenstände so lange Sie möchten, sicher und klimatisiert.", wa="Hallo, ich hätte gerne ein Angebot für die Einlagerung von Möbeln auf Mallorca"),
        dict(title="Umzüge von/auf das spanische Festland", desc="Kompletter Umzug zwischen Mallorca und jedem Ort auf dem spanischen Festland, Tür zu Tür.", wa="Hallo, ich hätte gerne ein Angebot für einen Umzug von oder zum spanischen Festland"),
        dict(title="Lagerraum-Vermietung", desc="Flexible Lagerflächen tage-, monatsweise oder unbefristet, in der Größe, die Sie benötigen.", wa="Hallo, ich hätte gerne ein Angebot zur Miete eines Lagerraums auf Mallorca"),
        dict(title="Räumung von Hallen und Gewerberäumen", desc="Komplette Räumung von Lagerhallen, Geschäften oder Gewerberäumen inklusive Entsorgung.", wa="Hallo, ich hätte gerne ein Angebot für die Räumung einer Halle oder eines Gewerberaums auf Mallorca"),
        dict(title="LKW-Vermietung", desc="LKW mit oder ohne Fahrer für einmalige Transporte mit großem Volumen.", wa="Hallo, ich hätte gerne ein Angebot zur Miete eines LKW auf Mallorca"),
        dict(title="Transporter-Vermietung", desc="Transporter in verschiedenen Größen, stunden- oder tageweise, für Ihren eigenen Umzug.", wa="Hallo, ich hätte gerne ein Angebot zur Miete eines Transporters auf Mallorca"),
        dict(title="Professionelle Verpackung", desc="Verpackungsmaterial und -technik zum Schutz Ihrer empfindlichsten Gegenstände während des Transports.", wa="Hallo, ich hätte gerne ein Angebot für einen professionellen Verpackungsservice auf Mallorca"),
    ],
    process=dict(eyebrow="So arbeiten wir", h2="Einfach, schnell und professionell", cta="Bereit für Ihren Transport? Jetzt Angebot anfordern",
                 steps=[("Angebot anfordern", "Füllen Sie das Formular aus oder schreiben Sie uns per WhatsApp mit den Details Ihres Umzugs."),
                        ("Auftragsbestätigung", "Wir vereinbaren mit Ihnen Datum, Uhrzeit und Details des Transports."),
                        ("Sichere Abholung und Transport", "Wir holen Ihre Gegenstände ab und transportieren sie mit Sorgfalt und Schutz."),
                        ("Lieferung am vereinbarten Ort", "Alles kommt pünktlich und einsatzbereit an.")]),
    whyus=dict(eyebrow="Warum wir?", h2="Ihr Umzug auf Mallorca in professionellen Händen",
               lead="Wir sind ein lokales Unternehmen mit über 15 Jahren Erfahrung in Umzügen und Transporten auf Mallorca. Wir kümmern uns um jedes Detail, damit Ihr Umzug schnell und ohne Überraschungen verläuft.",
               items=["Über 15 Jahre Erfahrung auf der Insel", "Eigenes, uniformiertes Team mit professioneller Schutzausrüstung",
                      "Versicherter Transport bei jedem Auftrag", "Kostenloses, unverbindliches Angebot",
                      "Garantierte Pünktlichkeit, auch außerhalb der Geschäftszeiten", "Persönliche und aufmerksame Betreuung von Anfang bis Ende"],
               cta="Kostenloses Angebot anfordern", img_alt="Team von Mallorca Transportes lädt Kartons in einen Transporter"),
    coverage=dict(eyebrow="Servicegebiet", h2="Abdeckung auf ganz Mallorca und den Balearen",
                  lead="Wir führen Umzüge und Transporte in allen Gemeinden Mallorcas durch, von Palma bis zu den kleinsten Dörfern. Außerdem bieten wir regelmäßige Verbindungen zwischen den Inseln.",
                  towns_h3="Gemeinden auf Mallorca",
                  towns=["Palma de Mallorca", "Calvià", "Marratxí", "Llucmajor", "Inca", "Manacor", "Sóller", "Andratx", "Alcúdia", "Pollença", "Felanitx", "Und der Rest der Insel"],
                  islands_h3="Transport zwischen den Inseln", routes=["Mallorca ⇄ Menorca", "Mallorca ⇄ Ibiza", "Mallorca ⇄ Formentera"],
                  islands_p="Müssen Sie etwas zwischen den Inseln verschicken? Wir kümmern uns von Anfang bis Ende darum.", islands_cta="Verfügbarkeit anfragen",
                  map_alt="Karte der Balearen mit den Transportrouten zwischen Mallorca, Menorca, Ibiza und Formentera"),
    fleet=dict(eyebrow="Unser Fuhrpark", h2="Fahrzeuge für jeden Umzug",
               lead="Wir verfügen über Transporter und LKW in verschiedenen Größen, passend zum Volumen Ihres Umzugs oder Transports – vom Einzelstück bis zur kompletten Wohnung.",
               items=["Geschlossene Fahrzeuge mit Schutz für Möbel und Kartons", "Hebebühne für schwere Lasten", "Eigener Fuhrpark auf der ganzen Insel verfügbar"],
               img_alt="LKW und Transporter der Mallorca-Transportes-Flotte"),
    gallery=dict(eyebrow="Reale Einsätze", h2="Umzüge und Transporte, die wir auf Mallorca durchgeführt haben",
                 lead="Einige Beispiele für Umzugs-, Verpackungs- und Möbeltransportdienste, die wir auf der ganzen Insel durchgeführt haben.",
                 alts=["Wohnungsumzug mit verpackten Kartons auf Mallorca", "Professionelle Verpackung von Elektrogeräten für einen Umzug auf Mallorca",
                       "Transport von Küchenmöbeln auf Mallorca", "Demontage und Verpackung von Möbeln bei einem Umzug auf Mallorca",
                       "Installation und Montage einer Küche nach einem Umzug auf Mallorca", "Montage von Holzmöbeln bei einer Renovierung auf Mallorca"]),
    testimonials_section=dict(eyebrow="Bewertungen", h2="Das sagen unsere Kunden"),
    testimonials=[
        dict(name="Alice Klein", role="Privatumzug", quote="Ausgezeichneter Service von Anfang bis Ende. Ich habe sie für meinen Umzug engagiert und bin mehr als zufrieden. Pünktlich, sorgfältig mit jedem Möbelstück und sehr gut organisiert während des gesamten Prozesses."),
        dict(name="David Romero", role="Firmentransport", quote="Wir mussten Büromöbel und Unterlagen von Manacor in unsere neuen Räume bringen. Das Team war schnell, effizient und sehr professionell. Der gesamte Ablauf war reibungslos."),
        dict(name="Juan Pérez", role="Küchendemontage und -montage", quote="Sehr professionell und schnell bei der Demontage und beim Transport der Möbel. Sie haben nicht nur meine neue Küche geliefert, sondern auch die alte demontiert, sodass ich mich nicht um die Entsorgung kümmern musste."),
        dict(name="Marc Vidal", role="Möbeltransport", quote="Ich habe ein Sofa und einen Tisch in einem Second-Hand-Laden gekauft, und sie haben alles abgeholt und nach Hause gebracht. Alles ohne eigene Marke. Sehr professionell und sorgfältig."),
        dict(name="Sonia Mestre", role="Inselverbindung", quote="Ich habe den Transport mehrerer Elektrogeräte von Mallorca nach Ibiza beauftragt. Ich wurde durchgehend informiert und die Termine wurden eingehalten. Sehr empfehlenswert für Transporte zwischen den Inseln."),
        dict(name="Lucía Fernández", role="Privatumzug", quote="Ich habe den Service für einen Umzug von Inca nach Palma beauftragt. Sie waren superpünktlich, sehr sorgfältig mit meinen Möbeln und alles kam in perfektem Zustand an. Man merkt die Erfahrung. Ich würde jederzeit wieder buchen!"),
        dict(name="Clara Ríos", role="Privatumzug", quote="Ich musste wegen eines Wohnungswechsels kurzfristig umziehen. Trotz der kurzen Vorlaufzeit haben sie sich angepasst und bei allem geholfen. Schnell, effizient und sehr freundlich. Eine glatte 10!"),
        dict(name="Patricia Navarro", role="Privatumzug", quote="Es war das erste Mal, dass ich einen Transportservice beauftragt habe, und ich hatte viele Fragen. Sie haben mich von Anfang an beraten, waren transparent beim Preis und während des gesamten Prozesses sehr aufmerksam. Sie haben meine Sachen in Palma abgeholt und problemlos in meine neue Wohnung in Alcúdia gebracht. Danke, dass Sie es so einfach gemacht haben!"),
        dict(name="Javier Morales", role="Privatumzug", quote="Ich habe den Transportservice für meinen Umzug beauftragt, und es war eine ausgezeichnete Erfahrung. Sie haben mir geholfen, alle meine Kartons und Möbel sicher und pünktlich zu transportieren. Der Fahrer war sehr freundlich. Sehr empfehlenswert für jeden, der umziehen muss!"),
        dict(name="Carlos Hernández", role="Firmentransport", quote="Ich habe den Transportservice beauftragt, um Möbel von der Fabrik in mein Lager zu bringen, und es war eine ausgezeichnete Erfahrung. Sie waren pünktlich, sorgfältig, und alles kam in einwandfreiem Zustand an. Ich werde sie für zukünftige Lieferungen definitiv wieder wählen."),
    ],
    faq_section=dict(eyebrow="Häufige Fragen", h2="Wir beantworten Ihre Fragen"),
    faq=[
        ("Was beinhaltet der Transport- oder Umzugsservice?", "Er beinhaltet Abholung, Transport und Lieferung Ihrer Gegenstände zum vereinbarten Zielort. Wir übernehmen auch das Be- und Entladen des Fahrzeugs."),
        ("Muss ich meine Gegenstände vor dem Transport verpacken?", "Das ist nicht zwingend erforderlich. Auf Wunsch übernimmt unser Team die Verpackung und den Schutz Ihrer Möbel und zerbrechlichen Gegenstände."),
        ("Wie wird der Preis des Service berechnet?", "Der Preis hängt vom zu transportierenden Volumen, der Entfernung, dem Zugang (Aufzug, Etagen) und einer eventuell nötigen Demontage ab. Wir geben Ihnen ein Festpreisangebot ohne Überraschungen."),
        ("Können Sie meine großen Möbel demontieren?", "Ja, wir haben ein spezialisiertes Team für die Demontage und Montage von Schränken, Küchen und Elektrogeräten."),
        ("Wie lange im Voraus sollte ich buchen?", "Wir empfehlen, einige Tage im Voraus zu buchen, bieten aber auch Express-Umzüge für dringende Fälle an."),
        ("Kann ich Dinge zwischen den Inseln transportieren?", "Ja, wir bedienen Strecken zwischen Mallorca, Menorca, Ibiza und Formentera für Umzüge und Waren."),
    ],
    final_cta=dict(h2="Bereit für Ihren Umzug auf Mallorca?", p="Fordern Sie jetzt Ihr kostenloses Angebot an. Unverbindlich, schnelle Antwort."),
    contact=dict(eyebrow="Kontakt", h2="Fordern Sie Ihr kostenloses Angebot an",
                 lead="Sagen Sie uns, was Sie transportieren möchten, und wir melden uns so schnell wie möglich bei Ihnen. Sie können uns auch direkt anrufen oder schreiben.",
                 call_label="Rufen Sie uns an", email_label="Schreiben Sie uns", whatsapp_label="WhatsApp", whatsapp_sub="Schnelle Antwort",
                 hours_label="Öffnungszeiten", hours1="Montag bis Freitag: 8:00 – 20:00 Uhr", hours2="Samstags und sonntags: in Ausnahmefällen nach Absprache",
                 form=dict(name="Name", phone="Telefon", email="E-Mail", service_type="Art der Dienstleistung",
                           options=["Privatumzug", "Firmen-/Büroumzug", "Möbeltransport", "Demontage und Montage", "Express-Umzug", "Transport zwischen den Inseln", "Sonstiges"],
                           message_label="Was möchten Sie transportieren?", message_placeholder="Abhol- und Zielort, ungefähres Datum, Art der Gegenstände...",
                           submit="Angebotsanfrage senden"),
                 note_pre="Beim Absenden öffnet sich Ihre E-Mail-App mit den bereits ausgefüllten Angaben. Alternativ können Sie uns direkt unter ", note_post=" anrufen."),
    footer=dict(blurb="Spezialisten für Umzüge und Möbeltransport auf Mallorca seit über 15 Jahren. Service für Privat- und Geschäftskunden auf der ganzen Insel.",
                services_h4="Dienstleistungen", services_links=["Privatumzüge", "Firmenumzüge", "Möbeltransport", "Demontage und Montage", "Transport zwischen den Inseln"],
                contact_h4="Kontakt", address="Insel Mallorca, Spanien",
                company_h4="Unternehmen", company_links=dict(coverage="Abdeckung", jobs="Durchgeführte Aufträge", reviews="Bewertungen", blog="Blog", faq="Häufige Fragen"),
                copyright="© 2026 Mallorca Transportes. Alle Rechte vorbehalten. Carrefusta, SLU."),
)

# ---------------------------------------------------------- CHINESE (zh-CN) --
T["zh"] = dict(
    meta_title="马略卡岛搬家与家具运输 | Mallorca Transportes",
    meta_description="Mallorca Transportes 是一家在马略卡岛拥有超过15年经验的搬家与家具运输公司。为个人和企业提供快速、安全、实惠的服务。24小时内提供免费报价。☎ +34 659 924 515",
    meta_keywords="马略卡岛搬家, 马略卡岛家具运输, 马略卡岛搬家公司, 帕尔马搬家, 马略卡岛物流, 巴利阿里群岛间运输, 马略卡岛家具拆装",
    og_description="马略卡岛全境搬家与家具运输服务。超过15年经验，运输有保险，并提供免费报价。欢迎致电或通过WhatsApp联系我们。",
    skip_link="跳至内容",
    nav=dict(servicios="服务", opiniones="评价", blog="博客", contacto="联系我们"),
    header_whatsapp="WhatsApp",
    wa_generic="您好，我想咨询在马略卡岛的搬家/运输报价",
    hero=dict(
        eyebrow="马略卡岛搬家与运输公司",
        h1_pre="轻松搞定", h1_accent="马略卡岛", h1_post="的搬家与家具运输",
        subtitle="超过15年为岛上的家庭和企业提供搬家服务。快速、安全，提供免费报价，无需承诺。",
        cta_call="立即致电", cta_whatsapp="直接WhatsApp联系", cta_quote="获取免费报价 →",
        stats=[("15+", "年经验"), ("1500+", "满意客户"), ("100+", "每月服务次数"), ("100%", "马略卡岛全境覆盖")],
    ),
    trust=["运输有保险", "24小时内报价", "覆盖马略卡岛全境", "自有专业团队"],
    services_section=dict(eyebrow="我们的服务", h2="马略卡岛搬家与运输服务",
                           lead="为各种需求量身定制的搬家与物流方案，从整套住宅搬迁到紧急家具家电运输，一应俱全。"),
    services=[
        dict(title="家庭搬家", desc="公寓、住宅的整体搬迁服务，包括家具、纸箱、家电及个人物品。", wa="您好，我想咨询在马略卡岛的家庭搬家报价"),
        dict(title="企业与办公室搬迁", desc="办公室、诊所、店铺及场所搬迁，不影响您的正常营业。如有需要，我们也可在非营业时间作业。", wa="您好，我想咨询企业或办公室搬迁报价"),
        dict(title="家具家电运输", desc="沙发、床、衣柜、厨房用具及家电的单次配送，提供专业包装与保护。", wa="您好，我想咨询家具家电运输报价"),
        dict(title="家具拆装", desc="专业团队负责衣柜、厨房及家电的拆卸，并包含目的地的重新安装。", wa="您好，我想咨询家具拆装服务报价"),
        dict(title="快捷搬家", desc="适用于紧急、小型或临时的搬迁需求，专为学生及限时交付设计的灵活服务。", wa="您好，我想咨询快捷搬家服务报价"),
        dict(title="巴利阿里群岛间运输", desc="马略卡岛、梅诺卡岛、伊维萨岛和福门特拉岛之间的常规航线，用于搬家、纸箱及货物运输。", wa="您好，我想咨询巴利阿里群岛间运输报价"),
        dict(title="家具升降机租赁", desc="为没有电梯或出入不便的高层住户提供家具升降机，含操作人员。", wa="您好，我想咨询租用家具升降机的报价"),
        dict(title="家具仓储", desc="在安全、受控的空间内，按您所需的时长为您存放家具及物品。", wa="您好，我想咨询家具仓储服务报价"),
        dict(title="往返西班牙大陆的搬家", desc="马略卡岛与西班牙大陆任何地点之间的门到门整体搬迁服务。", wa="您好，我想咨询往返西班牙大陆搬家的报价"),
        dict(title="储物间租赁", desc="按天、按月或长期租用，可根据您的需求选择合适的储物空间大小。", wa="您好，我想咨询租用储物间的报价"),
        dict(title="仓库及场所清空", desc="全面清空工业仓库、店铺或库房，并处理相关废弃物。", wa="您好，我想咨询仓库或场所清空服务报价"),
        dict(title="卡车租赁", desc="提供带司机或不带司机的卡车，用于大批量的单次运输。", wa="您好，我想咨询租用卡车的报价"),
        dict(title="货车租赁", desc="提供多种尺寸的货车，可按小时或按天租用于您自己的搬运。", wa="您好，我想咨询租用货车的报价"),
        dict(title="专业包装", desc="使用专业包装材料与技术，在运输过程中保护您最贵重、易碎的物品。", wa="您好，我想咨询专业包装服务报价"),
    ],
    process=dict(eyebrow="工作流程", h2="简单、快捷、专业", cta="准备好安排您的运输了吗？立即申请报价",
                 steps=[("提交您的报价请求", "填写表单或通过WhatsApp告知我们您的搬家详情。"),
                        ("确认服务", "我们与您确认日期、时间及运输细节。"),
                        ("安全取件与运输", "我们上门取件，并小心妥善地运输您的物品。"),
                        ("送达约定地点", "一切准时送达，随时可以摆放使用。")]),
    whyus=dict(eyebrow="为什么选择我们", h2="专业团队为您打理马略卡岛的搬家事宜",
               lead="我们是一家在马略卡岛拥有超过15年搬家与运输经验的本地公司。我们注重每一个细节，确保您的搬迁快捷、无忧。",
               items=["在马略卡岛拥有超过15年经验", "自有团队，统一着装，配备专业防护材料",
                      "每项服务均提供运输保险", "免费报价，无需承诺",
                      "保证准时，非营业时间同样可预约", "全程贴心、个性化的服务"],
               cta="申请您的免费报价", img_alt="Mallorca Transportes 团队将纸箱装上货车"),
    coverage=dict(eyebrow="服务范围", h2="覆盖马略卡岛及巴利阿里群岛全境",
                  lead="我们为马略卡岛的所有市镇提供搬家与运输服务，从帕尔马到最小的村庄皆可覆盖。我们也常年运营岛屿之间的运输航线。",
                  towns_h3="马略卡岛市镇",
                  towns=["Palma de Mallorca", "Calvià", "Marratxí", "Llucmajor", "Inca", "Manacor", "Sóller", "Andratx", "Alcúdia", "Pollença", "Felanitx", "以及岛上其他地区"],
                  islands_h3="岛屿间运输", routes=["马略卡岛 ⇄ 梅诺卡岛", "马略卡岛 ⇄ 伊维萨岛", "马略卡岛 ⇄ 福门特拉岛"],
                  islands_p="需要在岛屿之间寄送物品吗？我们将为您全程办理。", islands_cta="咨询可用性",
                  map_alt="巴利阿里群岛地图，展示马略卡岛、梅诺卡岛、伊维萨岛与福门特拉岛之间的运输航线"),
    fleet=dict(eyebrow="我们的车队", h2="适合各类搬家需求的车辆",
               lead="我们配备多种尺寸的货车与卡车，可根据您搬家或运输的体积灵活匹配，从单件物品到整套住宅均可满足。",
               items=["封闭式车厢，为家具及纸箱提供保护", "配备升降平台，可承载重物", "自有车队，覆盖全岛"],
               img_alt="Mallorca Transportes 车队的卡车与货车"),
    gallery=dict(eyebrow="真实案例", h2="我们在马略卡岛完成的搬家与运输案例",
                 lead="以下是我们在全岛完成的部分搬家、包装及家具运输服务案例。",
                 alts=["马略卡岛住宅搬家，纸箱已打包完毕", "马略卡岛搬家中的家电专业包装",
                       "马略卡岛厨房家具运输", "马略卡岛搬家中的家具拆卸与包装",
                       "马略卡岛搬家后的厨房安装", "马略卡岛装修翻新中的木质家具组装"]),
    testimonials_section=dict(eyebrow="客户评价", h2="客户怎么说"),
    testimonials=[
        dict(name="Alice Klein", role="个人搬家", quote="从头到尾服务都非常出色。我委托他们负责我的搬家，非常满意。他们准时、对每件家具都很细心，整个过程井井有条。"),
        dict(name="David Romero", role="企业运输", quote="我们需要将办公家具和文件从马纳科尔运到新场所。团队高效、专业、速度快，整个过程非常顺利。"),
        dict(name="Juan Pérez", role="厨房拆装", quote="拆卸和搬运家具非常专业、迅速。他们不仅帮我安装了新厨房，还拆除了旧厨房，让我不用为处理旧家具而烦恼。"),
        dict(name="Marc Vidal", role="家具运输", quote="我在二手店买了一张沙发和一张桌子，他们负责取件并送到我家，全程没有任何品牌介入，非常专业细心。"),
        dict(name="Sonia Mestre", role="岛屿间运输", quote="我委托他们将几件家电从马略卡岛运往伊维萨岛。全程保持沟通，并按时完成。强烈推荐用于岛屿间运输。"),
        dict(name="Lucía Fernández", role="个人搬家", quote="我委托他们负责从因卡到帕尔马的搬家。他们非常准时，对我的家具十分细心，一切都完好无损地送达。能看出他们经验丰富，绝对还会再次选择！"),
        dict(name="Clara Ríos", role="个人搬家", quote="因为换房子，我需要紧急搬家。尽管时间紧迫，他们依然全力配合，帮我处理了一切。快速、高效、态度友好，满分十分！"),
        dict(name="Patricia Navarro", role="个人搬家", quote="这是我第一次委托运输服务，一开始有很多疑虑。他们从一开始就给予专业建议，报价清晰，全程都非常细心周到。他们在帕尔马取件，顺利送到我在阿尔库迪亚的新家。谢谢你们让一切变得如此简单！"),
        dict(name="Javier Morales", role="个人搬家", quote="我委托了运输服务来完成我的搬家，体验非常棒。他们帮我安全、准时地搬运了所有纸箱和家具，司机也非常友善。强烈推荐给需要搬家的人！"),
        dict(name="Carlos Hernández", role="企业运输", quote="我委托他们将家具从工厂运到我的仓库，体验非常出色。他们准时、细心，一切都完好送达。以后有需要一定会再次选择他们。"),
    ],
    faq_section=dict(eyebrow="常见问题", h2="为您解答疑问"),
    faq=[
        ("运输或搬家服务包含哪些内容？", "包括上门取件、运输以及将您的物品送达约定地点。我们也负责车辆的装卸货。"),
        ("运输前我需要自己打包物品吗？", "不是必须的。如果您愿意，我们的团队可以负责为您的家具及易碎物品打包和防护。"),
        ("服务价格如何计算？", "价格取决于运输体积、距离、出入条件（是否有电梯、楼层）以及是否需要拆装家具。我们会为您提供固定报价，绝无隐藏费用。"),
        ("你们可以拆卸我的大件家具吗？", "可以，我们拥有专业团队负责衣柜、厨房及家电的拆卸与安装。"),
        ("我应该提前多久预约？", "建议提前几天预约，但如有紧急需求，我们也提供快捷搬家服务。"),
        ("我可以在岛屿之间运输物品吗？", "可以，我们在马略卡岛、梅诺卡岛、伊维萨岛和福门特拉岛之间运营搬家及货运航线。"),
    ],
    final_cta=dict(h2="准备好在马略卡岛开始您的搬家了吗？", p="现在就申请您的免费报价，无需承诺，快速回复。"),
    contact=dict(eyebrow="联系我们", h2="获取您的免费报价",
                 lead="告诉我们您需要运输的物品，我们会尽快与您联系。您也可以直接致电或给我们发消息。",
                 call_label="致电我们", email_label="给我们写信", whatsapp_label="WhatsApp", whatsapp_sub="快速回复",
                 hours_label="营业时间", hours1="周一至周五：8:00 – 20:00", hours2="周六、周日：特殊情况可协调安排",
                 form=dict(name="姓名", phone="电话", email="电子邮箱", service_type="服务类型",
                           options=["家庭搬家", "企业/办公室搬迁", "家具运输", "拆装服务", "快捷搬家", "岛屿间运输", "其他"],
                           message_label="请告诉我们您需要运输的物品", message_placeholder="起点、终点、大致日期、物品类型...",
                           submit="发送报价申请"),
                 note_pre="提交后将自动打开您的邮件应用并填好相关信息。如果您更喜欢，也可以直接致电 ", note_post="。"),
    footer=dict(blurb="超过15年专注于马略卡岛搬家与家具运输服务，为岛上的个人及企业客户提供服务。",
                services_h4="服务", services_links=["家庭搬家", "企业搬迁", "家具运输", "拆装服务", "岛屿间运输"],
                contact_h4="联系方式", address="西班牙 马略卡岛",
                company_h4="公司", company_links=dict(coverage="服务范围", jobs="已完成案例", reviews="客户评价", blog="博客", faq="常见问题"),
                copyright="© 2026 Mallorca Transportes。保留所有权利。Carrefusta, SLU。"),
)

MOBILE_QUOTE_LABEL = {"es": "Presupuesto", "en": "Quote", "de": "Angebot", "zh": "报价"}
MOBILE_CALL_LABEL = {"es": "Llamar", "en": "Call", "de": "Anrufen", "zh": "致电"}

print("All 4 languages loaded OK")


def esc(s):
    return str(s).replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')


def esc_attr(s):
    return str(s).replace('"', '&quot;')


def build_head(lang, d, rel):
    canonical = SITE_URL + "/" + LANG_META[lang]["path"]
    og_image = SITE_URL + "/img/og-image.jpg"

    hreflang_links = []
    for l in LANG_ORDER:
        hreflang_links.append('<link rel="alternate" hreflang="{}" href="{}/{}">'.format(
            "zh-Hans" if l == "zh" else l, SITE_URL, LANG_META[l]["path"]))
    hreflang_links.append('<link rel="alternate" hreflang="x-default" href="{}/">'.format(SITE_URL))
    hreflang_block = "\n".join(hreflang_links)

    zh_font = ""
    if lang == "zh":
        zh_font = '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n'

    schema = """<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "MovingCompany",
  "name": "Mallorca Transportes",
  "alternateName": "Carrefusta, SLU",
  "image": {og_image},
  "url": {canonical},
  "telephone": "{phone}",
  "email": "{email}",
  "priceRange": "€€",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Palma de Mallorca",
    "addressRegion": "Illes Balears",
    "addressCountry": "ES"
  }},
  "areaServed": [
    {{"@type": "AdministrativeArea", "name": "Mallorca"}},
    {{"@type": "AdministrativeArea", "name": "Menorca"}},
    {{"@type": "AdministrativeArea", "name": "Ibiza"}},
    {{"@type": "AdministrativeArea", "name": "Formentera"}}
  ],
  "openingHoursSpecification": [
    {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "08:00",
      "closes": "20:00"
    }}
  ],
  "inLanguage": "{lang}",
  "sameAs": []
}}
</script>""".format(og_image=json.dumps(og_image), canonical=json.dumps(canonical), phone=PHONE_E164, email=EMAIL, lang=lang)

    return """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow">
<meta name="author" content="Mallorca Transportes - Carrefusta, SLU">
<link rel="canonical" href="{canonical}">
{hreflang_block}

<meta property="og:type" content="website">
<meta property="og:locale" content="{locale}">
<meta property="og:site_name" content="Mallorca Transportes">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:image" content="{og_image}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{og_desc}">
<meta name="twitter:image" content="{og_image}">

<link rel="icon" type="image/png" sizes="32x32" href="{rel}img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="{rel}img/favicon-192.png">
<link rel="apple-touch-icon" href="{rel}img/apple-touch-icon.png">
<meta name="theme-color" content="#FF7300">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
{zh_font}<link rel="stylesheet" href="{rel}css/styles.css">

{schema}""".format(
        title=esc(d["meta_title"]), desc=esc_attr(d["meta_description"]), keywords=esc_attr(d["meta_keywords"]),
        canonical=canonical, hreflang_block=hreflang_block, locale=LANG_META[lang]["locale"],
        og_desc=esc_attr(d["og_description"]), og_image=og_image, rel=rel, zh_font=zh_font, schema=schema,
    )


def build_lang_switch(lang, rel):
    links = []
    for l in LANG_ORDER:
        href = rel + LANG_META[l]["path"] if rel else ("./" if l == "es" else LANG_META[l]["path"])
        if l == lang:
            links.append('<span class="lang-current">{}</span>'.format(LANG_META[l]["label"]))
        else:
            links.append('<a href="{}">{}</a>'.format(href, LANG_META[l]["label"]))
    return '<div class="lang-switch">' + "".join(links) + "</div>"


def build_header(lang, d, rel):
    home_href = rel + "index.html" if rel else "#top"
    blog_href = rel + "blog/index.html" if rel else "blog/index.html"
    wa_href = wa_url(d["wa_generic"])
    nav = d["nav"]

    servicios_href = (rel + "index.html#servicios") if rel else "#servicios"
    opiniones_href = (rel + "index.html#opiniones") if rel else "#opiniones"
    contacto_href = (rel + "index.html#contacto") if rel else "#contacto"

    return """<a class="skip-link" href="#contenido">{skip}</a>

<header class="site-header" id="top">
  <div class="container header-inner">
    <a href="{home}" class="brand" aria-label="Mallorca Transportes{home_suffix}">
      <img src="{rel}img/logo.svg" alt="Mallorca Transportes" class="brand-logo" width="220" height="50">
    </a>

    <nav class="main-nav" id="main-nav" aria-label="{aria_nav}">
      <a href="{servicios}">{nav_servicios}</a>
      <a href="{opiniones}">{nav_opiniones}</a>
      <a href="{blog}">{nav_blog}</a>
      <a href="{contacto}">{nav_contacto}</a>
    </nav>

    <div class="header-actions">
      {lang_switch}
      <a href="tel:{phone_e164}" class="btn btn-ghost btn-sm header-call">
        {phone_icon}
        <span>{phone_display}</span>
      </a>
      <a href="{wa_href}" class="btn btn-primary btn-sm" target="_blank" rel="noopener">
        {wa_icon}
        <span>{wa_label}</span>
      </a>
      <button class="nav-toggle" id="nav-toggle" aria-expanded="false" aria-controls="main-nav" aria-label="{aria_menu}">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
""".format(
        skip=esc(d["skip_link"]), home=home_href, rel=rel, home_suffix=esc_attr(ARIA[lang]["home_suffix"]),
        aria_nav=esc_attr(ARIA[lang]["nav"]), aria_menu=esc_attr(ARIA[lang]["menu"]),
        servicios=servicios_href, opiniones=opiniones_href, blog=blog_href, contacto=contacto_href,
        nav_servicios=esc(nav["servicios"]), nav_opiniones=esc(nav["opiniones"]), nav_blog=esc(nav["blog"]), nav_contacto=esc(nav["contacto"]),
        lang_switch=build_lang_switch(lang, rel),
        phone_e164=PHONE_E164, phone_icon=PHONE_ICON, phone_display=PHONE_DISPLAY,
        wa_href=wa_href, wa_icon=WHATSAPP_ICON, wa_label=esc(d["header_whatsapp"]),
    )


def build_footer(lang, d, rel):
    f = d["footer"]
    servicios_href = (rel + "index.html#servicios") if rel else "#servicios"
    cobertura_href = (rel + "index.html#cobertura") if rel else "#cobertura"
    trabajos_href = (rel + "index.html#trabajos") if rel else "#trabajos"
    opiniones_href = (rel + "index.html#opiniones") if rel else "#opiniones"
    faq_href = (rel + "index.html#faq") if rel else "#faq"
    blog_href = rel + "blog/index.html" if rel else "blog/index.html"
    contacto_href = (rel + "index.html#contacto") if rel else "#contacto"
    wa_href = wa_url(d["wa_generic"])

    services_links_html = "\n        ".join(
        '<li><a href="{}">{}</a></li>'.format(servicios_href, esc(s)) for s in f["services_links"])

    return """<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <img src="{rel}img/logo.svg" alt="Mallorca Transportes" class="footer-logo" width="200" height="46">
      <p>{blurb}</p>
    </div>
    <div class="footer-col">
      <h4>{services_h4}</h4>
      <ul>
        {services_links}
      </ul>
    </div>
    <div class="footer-col">
      <h4>{contact_h4}</h4>
      <ul>
        <li><a href="tel:{phone_e164}">{phone_display}</a></li>
        <li><a href="mailto:{email}">{email}</a></li>
        <li>{address}</li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>{company_h4}</h4>
      <ul>
        <li><a href="{cobertura}">{l_coverage}</a></li>
        <li><a href="{trabajos}">{l_jobs}</a></li>
        <li><a href="{opiniones}">{l_reviews}</a></li>
        <li><a href="{blog}">{l_blog}</a></li>
        <li><a href="{faq}">{l_faq}</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>{copyright}</p>
  </div>
</footer>

<a href="{wa_href}" class="whatsapp-float" target="_blank" rel="noopener" aria-label="{aria_wa_float}">
  {wa_icon_big}
</a>

<div class="mobile-cta-bar">
  <a href="tel:{phone_e164}" class="mobile-cta-btn call">
    {phone_icon}
    {mobile_call}
  </a>
  <a href="{wa_href}" class="mobile-cta-btn whatsapp" target="_blank" rel="noopener">
    {wa_icon}
    WhatsApp
  </a>
  <a href="{contacto}" class="mobile-cta-btn quote">{mobile_quote}</a>
</div>

<script src="{rel}js/main.js"></script>
</body>
</html>
""".format(
        rel=rel, blurb=esc(f["blurb"]), services_h4=esc(f["services_h4"]), services_links=services_links_html,
        contact_h4=esc(f["contact_h4"]), phone_e164=PHONE_E164, phone_display=PHONE_DISPLAY, email=EMAIL, address=esc(f["address"]),
        company_h4=esc(f["company_h4"]), cobertura=cobertura_href, l_coverage=esc(f["company_links"]["coverage"]),
        trabajos=trabajos_href, l_jobs=esc(f["company_links"]["jobs"]), opiniones=opiniones_href, l_reviews=esc(f["company_links"]["reviews"]),
        blog=blog_href, l_blog=esc(f["company_links"]["blog"]), faq=faq_href, l_faq=esc(f["company_links"]["faq"]),
        copyright=esc(f["copyright"]), wa_href=wa_href, wa_icon_big=WHATSAPP_ICON_BIG, phone_icon=PHONE_ICON,
        wa_icon=WHATSAPP_ICON, contacto=contacto_href,
        mobile_call=MOBILE_CALL_LABEL[lang], mobile_quote=MOBILE_QUOTE_LABEL[lang],
        aria_wa_float=esc_attr(ARIA[lang]["whatsapp_float"]),
    )


SERVICE_ICONS = [
    'M3 9.5 12 3l9 6.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1V9.5z',
    'M4 21V9l8-6 8 6v12h-6v-7h-4v7H4z',
    'M3 4h13v9h5l3 4v3h-2a2.5 2.5 0 0 1-5 0H9.5a2.5 2.5 0 0 1-5 0H3V4zm2 2v7h11V6H5zm12.5 14a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM7 20a1 1 0 1 0 0-2 1 1 0 0 0 0 2z',
    'M5 3h14v4H5V3zm0 6h14v4H5V9zm0 6h9v4H5v-4z',
    'M13 2 4 14h6l-1 8 9-12h-6l1-8z',
    'M12 2a10 10 0 1 0 .001 20.001A10 10 0 0 0 12 2zm7.9 9h-3.2a15.7 15.7 0 0 0-1.2-5.4A8 8 0 0 1 19.9 11zM12 4.1c1 1.5 1.9 3.8 2.2 6.9H9.8c.3-3.1 1.2-5.4 2.2-6.9zM4.1 13h3.2c.2 2 .6 3.8 1.2 5.4A8 8 0 0 1 4.1 13zm3.2-2H4.1a8 8 0 0 1 4.4-5.4A15.7 15.7 0 0 0 7.3 11zM12 19.9c-1-1.5-1.9-3.8-2.2-6.9h4.4c-.3 3.1-1.2 5.4-2.2 6.9zm2.5-1.5c.6-1.6 1-3.4 1.2-5.4h3.2a8 8 0 0 1-4.4 5.4z',
    'M12 2 5 10h4v10h6V10h4L12 2z',
    'M2 10 12 3l10 7v10a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V10zm4 9h4v-6H6v6zm8 0h4v-6h-4v6z',
    'M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z',
    'M3 3h8v8H3V3zm10 0h8v8h-8V3zM3 13h8v8H3v-8zm10 0h8v8h-8v-8z',
    'M3 4h18v3H3V4zm0 5h18v11a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9zm2 2v8h14v-8H5z',
    'M3 6h11v9H3V6zm11 3h4l3 3v3h-2a2 2 0 1 1-4 0H9a2 2 0 1 1-4 0H3v-2h1V9zM8 20a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm10 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2z',
    'M2 8h12v8H2V8zm12 2h3.5L20 13v3h-1.5a1.8 1.8 0 1 1-3.6 0H8.6a1.8 1.8 0 1 1-3.6 0H2v-2h12v-3zM6.8 20.6a.8.8 0 1 0 0-1.6.8.8 0 0 0 0 1.6zm10 0a.8.8 0 1 0 0-1.6.8.8 0 0 0 0 1.6z',
    'M3 8 12 4l9 4v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V8zm9-1.8L5.6 8.4 12 11l6.4-2.6L12 6.2zM11 12v7h2v-7h-2z',
]

GALLERY_IMAGES = [
    'trabajo-mudanza-01.jpg', 'trabajo-mudanza-02.jpg', 'trabajo-mudanza-03.jpg',
    'trabajo-mudanza-04.jpg', 'trabajo-mudanza-05.jpg', 'trabajo-mudanza-06.jpg',
]


def build_main(lang, d, rel):
    contacto_href = (rel + "index.html#contacto") if rel else "#contacto"
    wa_generic_href = wa_url(d["wa_generic"])

    # ---- HERO ----
    h = d["hero"]
    stats_html = "\n        ".join(
        '<li><strong>{}</strong><span>{}</span></li>'.format(esc(v), esc(l)) for v, l in h["stats"])
    hero_html = """  <section class="hero">
    <div class="hero-bg">
      <img src="{rel}img/hero-mudanzas-mallorca.jpg" alt="{hero_img_alt}" width="1920" height="1080" fetchpriority="high">
      <div class="hero-overlay"></div>
    </div>
    <div class="container hero-content">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1_pre}<span class="text-accent">{h1_accent}</span>{h1_post}</h1>
      <p class="hero-subtitle">{subtitle}</p>
      <div class="hero-cta">
        <a href="tel:{phone_e164}" class="btn btn-primary btn-lg">
          {phone_icon}
          {cta_call}
        </a>
        <a href="{wa_href}" class="btn btn-outline-light btn-lg" target="_blank" rel="noopener">
          {cta_whatsapp}
        </a>
        <a href="{contacto}" class="btn btn-text-light btn-lg">{cta_quote}</a>
      </div>

      <ul class="hero-stats">
        {stats}
      </ul>
    </div>
  </section>
""".format(rel=rel, hero_img_alt=esc_attr(h["eyebrow"]), eyebrow=esc(h["eyebrow"]),
           h1_pre=esc(h["h1_pre"]), h1_accent=esc(h["h1_accent"]), h1_post=esc(h["h1_post"]),
           subtitle=esc(h["subtitle"]), phone_e164=PHONE_E164, phone_icon=PHONE_ICON, cta_call=esc(h["cta_call"]),
           wa_href=wa_generic_href, cta_whatsapp=esc(h["cta_whatsapp"]), contacto=contacto_href, cta_quote=esc(h["cta_quote"]),
           stats=stats_html)

    # ---- TRUST STRIP ----
    trust_icons = [
        'M12 2 3 6v6c0 5 3.8 9.7 9 11 5.2-1.3 9-6 9-11V6l-9-4zm0 2.2 7 3.1V12c0 4-3 8-7 9-4-1-7-5-7-9V7.3l7-3.1zM10.8 15l-3-3 1.4-1.4 1.6 1.6 4.8-4.8 1.4 1.4-6.2 6.2z',
        'M12 8v5l3.5 2.1.8-1.3-3-1.8V8H12zM12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm0 18a8 8 0 1 1 0-16 8 8 0 0 1 0 16z',
        'M12 2 2 7l10 5 8-4v6h2V7L12 2zM4 10.2V16c0 2.2 3.6 4 8 4s8-1.8 8-4v-5.8l-8 4-8-4z',
        'M20 8h-3V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a1 1 0 0 0 1 1h1.2a3 3 0 0 0 5.6 0h4.4a3 3 0 0 0 5.6 0H22a1 1 0 0 0 1-1v-4l-3-3zM9 18.5A1.5 1.5 0 1 1 9 15.5a1.5 1.5 0 0 1 0 3zm10 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM15 12V6h0 3.6L21 9.4V12H15z',
    ]
    trust_items = "\n      ".join(
        '<div class="trust-item"><svg class="icon" viewBox="0 0 24 24"><path d="{}"/></svg><span>{}</span></div>'.format(icon, esc(t))
        for icon, t in zip(trust_icons, d["trust"]))
    trust_html = '  <section class="trust-strip">\n    <div class="container trust-strip-inner">\n      {}\n    </div>\n  </section>\n'.format(trust_items)

    # ---- SERVICES ----
    ss = d["services_section"]
    cards = []
    for icon, s in zip(SERVICE_ICONS, d["services"]):
        cards.append("""        <article class="service-card">
          <div class="service-icon">
            <svg class="icon" viewBox="0 0 24 24"><path d="{icon}"/></svg>
          </div>
          <h3>{title}</h3>
          <p>{desc}</p>
          <a href="{wa}" target="_blank" rel="noopener" class="service-link">{link_label} →</a>
        </article>""".format(icon=icon, title=esc(s["title"]), desc=esc(s["desc"]), wa=wa_url(s["wa"]), link_label=esc(ARIA[lang]["service_link"])))
    services_html = """  <section class="section" id="servicios">
    <div class="container">
      <p class="section-eyebrow">{eyebrow}</p>
      <h2>{h2}</h2>
      <p class="section-lead">{lead}</p>

      <div class="grid services-grid">
{cards}
      </div>
    </div>
  </section>
""".format(eyebrow=esc(ss["eyebrow"]), h2=esc(ss["h2"]), lead=esc(ss["lead"]), cards="\n\n".join(cards))

    # ---- PROCESS ----
    p = d["process"]
    steps_html = []
    for i, (title, desc) in enumerate(p["steps"], 1):
        steps_html.append("""        <div class="process-step">
          <span class="process-number">{n}</span>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>""".format(n=i, title=esc(title), desc=esc(desc)))
    process_html = """  <section class="process">
    <div class="container">
      <p class="section-eyebrow section-eyebrow-light">{eyebrow}</p>
      <h2 class="text-white">{h2}</h2>
      <div class="process-steps">
{steps}
      </div>
      <div class="process-cta">
        <a href="{contacto}" class="btn btn-white btn-lg">{cta}</a>
      </div>
    </div>
  </section>
""".format(eyebrow=esc(p["eyebrow"]), h2=esc(p["h2"]), steps="\n".join(steps_html), contacto=contacto_href, cta=esc(p["cta"]))

    # ---- WHY US ----
    w = d["whyus"]
    items_html = "\n          ".join('<li>{}</li>'.format(esc(i)) for i in w["items"])
    whyus_html = """  <section class="section" id="por-que-elegirnos">
    <div class="container why-us">
      <div class="why-us-image">
        <img src="{rel}img/equipo-mudanzas-mallorca.jpg" loading="lazy" alt="{img_alt}" width="1200" height="900">
      </div>
      <div class="why-us-content">
        <p class="section-eyebrow">{eyebrow}</p>
        <h2>{h2}</h2>
        <p class="section-lead">{lead}</p>
        <ul class="check-list">
          {items}
        </ul>
        <a href="{contacto}" class="btn btn-primary">{cta}</a>
      </div>
    </div>
  </section>
""".format(rel=rel, img_alt=esc_attr(w["img_alt"]), eyebrow=esc(w["eyebrow"]), h2=esc(w["h2"]), lead=esc(w["lead"]),
           items=items_html, contacto=contacto_href, cta=esc(w["cta"]))

    # ---- COVERAGE ----
    c = d["coverage"]
    towns_html = "\n            ".join('<li>{}</li>'.format(esc(t)) for t in c["towns"])
    routes_html = "\n            ".join(
        '<li><span class="island-badge">✓</span> {}</li>'.format(esc(r)) for r in c["routes"])
    coverage_html = """  <section class="section section-alt" id="cobertura">
    <div class="container">
      <p class="section-eyebrow">{eyebrow}</p>
      <h2>{h2}</h2>
      <p class="section-lead">{lead}</p>

      <div class="coverage-grid">
        <div class="coverage-towns">
          <h3>{towns_h3}</h3>
          <ul class="towns-list">
            {towns}
          </ul>
        </div>
        <div class="coverage-islands">
          <h3>{islands_h3}</h3>
          <img src="{rel}img/mapa-islas-baleares.svg" alt="{map_alt}" class="coverage-map" width="600" height="487" loading="lazy">
          <ul class="islands-list">
            {routes}
          </ul>
          <p>{islands_p}</p>
          <a href="tel:{phone_e164}" class="btn btn-outline">{islands_cta}</a>
        </div>
      </div>
    </div>
  </section>
""".format(eyebrow=esc(c["eyebrow"]), h2=esc(c["h2"]), lead=esc(c["lead"]), towns_h3=esc(c["towns_h3"]), towns=towns_html,
           islands_h3=esc(c["islands_h3"]), rel=rel, map_alt=esc_attr(c["map_alt"]), routes=routes_html,
           islands_p=esc(c["islands_p"]), phone_e164=PHONE_E164, islands_cta=esc(c["islands_cta"]))

    # ---- FLEET ----
    fl = d["fleet"]
    fleet_items_html = "\n          ".join('<li>{}</li>'.format(esc(i)) for i in fl["items"])
    fleet_html = """  <section class="section" id="flota">
    <div class="container fleet">
      <div class="fleet-content">
        <p class="section-eyebrow">{eyebrow}</p>
        <h2>{h2}</h2>
        <p class="section-lead">{lead}</p>
        <ul class="check-list">
          {items}
        </ul>
      </div>
      <div class="fleet-images">
        <img src="{rel}img/flota-camion-furgoneta.jpg" loading="lazy" alt="{img_alt}" width="1200" height="900">
      </div>
    </div>
  </section>
""".format(eyebrow=esc(fl["eyebrow"]), h2=esc(fl["h2"]), lead=esc(fl["lead"]), items=fleet_items_html, rel=rel, img_alt=esc_attr(fl["img_alt"]))

    # ---- GALLERY ----
    g = d["gallery"]
    gallery_items_html = "\n        ".join(
        '<div class="gallery-item"><img src="{rel}img/{img}" loading="lazy" alt="{alt}" width="900" height="675"></div>'.format(rel=rel, img=img, alt=esc_attr(alt))
        for img, alt in zip(GALLERY_IMAGES, g["alts"]))
    gallery_html = """  <section class="section section-alt" id="trabajos">
    <div class="container">
      <p class="section-eyebrow">{eyebrow}</p>
      <h2>{h2}</h2>
      <p class="section-lead">{lead}</p>

      <div class="gallery-grid">
        {items}
      </div>
    </div>
  </section>
""".format(eyebrow=esc(g["eyebrow"]), h2=esc(g["h2"]), lead=esc(g["lead"]), items=gallery_items_html)

    # ---- TESTIMONIALS ----
    ts = d["testimonials_section"]
    slides = []
    for t in d["testimonials"]:
        slides.append("""            <li class="carousel-slide">
              <figure class="testimonial-card">
                <div class="testimonial-head">
                  <img src="{rel}img/avatar-placeholder.jpg" alt="" class="testimonial-avatar" width="56" height="56" loading="lazy">
                  <div>
                    <span class="testimonial-name">{name}</span>
                    <span class="testimonial-role">{role}</span>
                    <div class="stars" aria-hidden="true">★★★★★</div>
                  </div>
                </div>
                <blockquote>&ldquo;{quote}&rdquo;</blockquote>
              </figure>
            </li>""".format(rel=rel, name=esc(t["name"]), role=esc(t["role"]), quote=esc(t["quote"])))
    testimonials_html = """  <section class="section" id="opiniones">
    <div class="container">
      <p class="section-eyebrow">{eyebrow}</p>
      <h2>{h2}</h2>

      <div class="testimonial-carousel" id="testimonial-carousel">
        <button class="carousel-arrow prev" type="button" aria-label="{aria_prev}">
          <svg class="icon" viewBox="0 0 24 24"><path d="M15.5 4.5 8 12l7.5 7.5 1.4-1.4L10.8 12l6.1-6.1z"/></svg>
        </button>

        <div class="carousel-viewport">
          <ul class="carousel-track" id="carousel-track">
{slides}
          </ul>
        </div>

        <button class="carousel-arrow next" type="button" aria-label="{aria_next}">
          <svg class="icon" viewBox="0 0 24 24"><path d="M8.5 4.5 16 12l-7.5 7.5-1.4-1.4L13.2 12l-6.1-6.1z"/></svg>
        </button>
      </div>
      <div class="carousel-dots" id="carousel-dots"></div>
    </div>
  </section>
""".format(eyebrow=esc(ts["eyebrow"]), h2=esc(ts["h2"]), slides="\n\n".join(slides),
           aria_prev=esc_attr(ARIA[lang]["prev"]), aria_next=esc_attr(ARIA[lang]["next"]))

    # ---- FAQ ----
    fs = d["faq_section"]
    faq_items = []
    for i, (q, a) in enumerate(d["faq"]):
        open_attr = " open" if i == 0 else ""
        faq_items.append("""        <details class="faq-item"{open}>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>""".format(open=open_attr, q=esc(q), a=esc(a)))
    faq_html = """  <section class="section section-alt" id="faq">
    <div class="container container-narrow">
      <p class="section-eyebrow">{eyebrow}</p>
      <h2>{h2}</h2>

      <div class="faq-list">
{items}
      </div>
    </div>
  </section>
""".format(eyebrow=esc(fs["eyebrow"]), h2=esc(fs["h2"]), items="\n".join(faq_items))

    # ---- FINAL CTA ----
    fc = d["final_cta"]
    final_cta_html = """  <section class="final-cta">
    <div class="container final-cta-inner">
      <h2 class="text-white">{h2}</h2>
      <p>{p}</p>
      <div class="final-cta-actions">
        <a href="tel:{phone_e164}" class="btn btn-white btn-lg">{phone_display}</a>
        <a href="{wa_href}" class="btn btn-outline-light btn-lg" target="_blank" rel="noopener">WhatsApp</a>
        <a href="mailto:{email}" class="btn btn-text-light btn-lg">{email}</a>
      </div>
    </div>
  </section>
""".format(h2=esc(fc["h2"]), p=esc(fc["p"]), phone_e164=PHONE_E164, phone_display=PHONE_DISPLAY,
           wa_href=wa_url(d["wa_generic"]), email=EMAIL)

    # ---- CONTACT ----
    ct = d["contact"]
    fo = ct["form"]
    options_html = "\n              ".join('<option>{}</option>'.format(esc(o)) for o in fo["options"])
    contact_html = """  <section class="section contact-section" id="contacto">
    <div class="container">
      <p class="section-eyebrow">{eyebrow}</p>
      <h2>{h2}</h2>
      <p class="section-lead">{lead}</p>

      <div class="contact-grid">
        <div class="contact-info">
          <a class="contact-info-item" href="tel:{phone_e164}">
            <span class="contact-icon">{phone_icon}</span>
            <span>
              <strong>{call_label}</strong>
              <span>{phone_display}</span>
            </span>
          </a>
          <a class="contact-info-item" href="mailto:{email}">
            <span class="contact-icon"><svg class="icon" viewBox="0 0 24 24"><path d="M4 4h16a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zm16 3.4-8 5.4-8-5.4V19h16V7.4zM4.5 6l7.5 5 7.5-5h-15z"/></svg></span>
            <span>
              <strong>{email_label}</strong>
              <span>{email}</span>
            </span>
          </a>
          <a class="contact-info-item" href="{wa_href}" target="_blank" rel="noopener">
            <span class="contact-icon">{wa_icon}</span>
            <span>
              <strong>{whatsapp_label}</strong>
              <span>{whatsapp_sub}</span>
            </span>
          </a>

          <div class="contact-hours">
            <strong>{hours_label}</strong>
            <p>{hours1}</p>
            <p>{hours2}</p>
          </div>
        </div>

        <form class="contact-form" id="contact-form">
          <div class="form-row">
            <label>
              <span>{f_name}</span>
              <input type="text" name="nombre" required autocomplete="name">
            </label>
            <label>
              <span>{f_phone}</span>
              <input type="tel" name="telefono" required autocomplete="tel">
            </label>
          </div>
          <label>
            <span>{f_email}</span>
            <input type="email" name="email" required autocomplete="email">
          </label>
          <label>
            <span>{f_service_type}</span>
            <select name="servicio">
              {options}
            </select>
          </label>
          <label>
            <span>{f_message_label}</span>
            <textarea name="mensaje" rows="4" placeholder="{f_message_placeholder}"></textarea>
          </label>
          <button type="submit" class="btn btn-primary btn-lg btn-block">{f_submit}</button>
          <p class="form-note">{note_pre}<a href="tel:{phone_e164}">{phone_display}</a>{note_post}</p>
        </form>
      </div>
    </div>
  </section>
""".format(eyebrow=esc(ct["eyebrow"]), h2=esc(ct["h2"]), lead=esc(ct["lead"]), phone_e164=PHONE_E164,
           phone_icon=PHONE_ICON, call_label=esc(ct["call_label"]), phone_display=PHONE_DISPLAY, email=EMAIL,
           email_label=esc(ct["email_label"]), wa_href=wa_url(d["wa_generic"]), wa_icon=WHATSAPP_ICON,
           whatsapp_label=esc(ct["whatsapp_label"]), whatsapp_sub=esc(ct["whatsapp_sub"]),
           hours_label=esc(ct["hours_label"]), hours1=esc(ct["hours1"]), hours2=esc(ct["hours2"]),
           f_name=esc(fo["name"]), f_phone=esc(fo["phone"]), f_email=esc(fo["email"]), f_service_type=esc(fo["service_type"]),
           options=options_html, f_message_label=esc(fo["message_label"]), f_message_placeholder=esc_attr(fo["message_placeholder"]),
           f_submit=esc(fo["submit"]), note_pre=esc(ct["note_pre"]), note_post=esc(ct["note_post"]))

    return "\n<main id=\"contenido\">\n\n" + hero_html + "\n" + trust_html + "\n" + services_html + "\n" + process_html + \
        "\n" + whyus_html + "\n" + coverage_html + "\n" + fleet_html + "\n" + gallery_html + "\n" + testimonials_html + \
        "\n" + faq_html + "\n" + final_cta_html + "\n" + contact_html + "\n</main>\n"


def build_page(lang):
    d = T[lang]
    rel = "" if lang == "es" else "../"
    html = "<!doctype html>\n<html lang=\"{lang_attr}\">\n<head>\n{head}\n</head>\n<body>\n\n{header}\n{main}\n{footer}".format(
        lang_attr=("zh-Hans" if lang == "zh" else lang),
        head=build_head(lang, d, rel),
        header=build_header(lang, d, rel),
        main=build_main(lang, d, rel),
        footer=build_footer(lang, d, rel),
    )
    out_dir = os.path.join(BASE, LANG_META[lang]["path"]) if LANG_META[lang]["path"] else BASE
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote", out_path, "(", len(html), "bytes )")


for lang in LANG_ORDER:
    build_page(lang)

print("\nDone.")
