#!/usr/bin/env python3
"""Writes the landing page in three languages (index.html, pt/index.html, es/index.html) and sitemap.xml.
One URL per language, so search engines can index each and link them with hreflang.
usage: python3 build.py   (then commit the generated files; GitHub Pages serves them as they are)
Images (img/<lang>/) are the app's real captures from biblia-duo-ios/AppStore/raw, converted with ffmpeg to WebP;
book.webp is the text-free open Bible on leather (the page puts its own title beside it), og.jpg the link preview."""
import html, json, os

BASE = "https://oviniciusramosp.github.io/biblia-duo-site/"
APP_ID = "6826902361"
STORE = f"https://apps.apple.com/app/id{APP_ID}"
HERE = os.path.dirname(os.path.abspath(__file__))

# path: where the page lives; badge: Apple's badge locale; lang: the images and the support/privacy ?lang=
PAGES = {
    "en": dict(path="", html_lang="en", og_locale="en_US", badge="en-us", currency="USD",
               name="Foldable Bible: Holy Scripture", short="Foldable Bible",
               title="Foldable Bible — the Holy Bible as a real book, for iPhone Duo",
               description="The complete Holy Bible as a real book on iPhone Duo: two pages, gilded edges and pages you turn "
                           "by hand. King James Version. Free, no ads, works offline.",
               tagline="The Bible like a real book, made for iPhone Duo.",
               facts="Free · No ads · Works offline",
               badge_alt="Download on the App Store",
               book_alt="The Bible open to Psalm 23, with gilded edges and a red ribbon",
               sections=[
                   ("Closed, the cover. Open, the book.",
                    "With iPhone Duo closed, the outer display shows your Bible's leather cover. Swipe it open and read one "
                    "page at a time. Unfold your iPhone Duo and the Bible lies open on two pages, like the one on your nightstand.",
                    "cover", "The Bible's leather cover on the iPhone Duo outer display"),
                   ("Turn pages by hand",
                    "Pages curl under your finger, with the light and shadow of paper. The gilded edges show how far you've "
                    "read, and a cloth ribbon keeps your place.",
                    "turn", "A page curling as it turns, on the iPhone Duo inner display"),
                   ("Highlight what speaks to you",
                    "Touch and hold a word to highlight the verse in one of four colors. Every highlight becomes a quote to "
                    "revisit and share.",
                    "highlights", "John 3:16 highlighted in yellow on an open page"),
                   ("Find any verse",
                    "All 66 books and every chapter, with search. Type John 3:16 and go straight to the text.",
                    "books", "The books list searching for John 3:16"),
               ],
               cards=[
                   ("Make it yours", "Four cover styles, six leather colors, six app icons, light and dark themes, and the "
                                     "text size that suits your eyes."),
                   ("No internet, no ads", "Works on a plane, at church, anywhere without signal. No ads, no distractions."),
                   ("Your reading stays yours", "No account and no data collected. Your highlights stay on your iPhone."),
               ],
               privacy="Privacy policy", support="Support",
               translations_title="Three complete translations",
               translations=["English: King James Version (KJV)", "Português: Bíblia Livre, based on the Almeida translation",
                             "Español: Reina-Valera 1909"],
               translations_note="Old and New Testament, all 66 books. Switch the language in Settings.",
               cta_title="Get Foldable Bible",
               cta="Free on the App Store. Made only for iPhone Duo, with iOS 27.1 or later.",
               credits="Bible texts: King James Version and Reina-Valera 1909 (public domain); Bíblia Livre © 2018 Diego "
                       "Santos, Mario Sérgio and Marco Teles (CC BY 4.0). Texts via eBible.org.",
               legal="Apple, the Apple logo and iPhone are trademarks of Apple Inc. App Store is a service mark of Apple Inc."),
    "pt": dict(path="pt/", html_lang="pt-BR", og_locale="pt_BR", badge="pt-br", currency="BRL",
               name="Bíblia Sagrada Fold", short="Bíblia Sagrada Fold",
               title="Bíblia Sagrada Fold — a Bíblia Sagrada como um livro, para iPhone Duo",
               description="A Bíblia Sagrada completa como um livro de verdade no iPhone Duo: duas páginas, bordas douradas e "
                           "folhas que viram com o dedo. Grátis, sem anúncios e sem internet.",
               tagline="A Bíblia como um livro de verdade, feita para o iPhone Duo.",
               facts="Grátis · Sem anúncios · Funciona sem internet",
               badge_alt="Baixar na App Store",
               book_alt="A Bíblia aberta nos Salmos, com bordas douradas e fitinha vermelha",
               sections=[
                   ("Fechado, a capa. Aberto, o livro.",
                    "Com o iPhone Duo fechado, a tela de fora mostra a capa de couro da sua Bíblia. Deslize para abrir e leia "
                    "uma página de cada vez. Abra o iPhone Duo e a Bíblia aparece aberta em duas páginas, como aquela que fica na "
                    "cabeceira.",
                    "cover", "A capa de couro da Bíblia na tela externa do iPhone Duo"),
                   ("Vire a página com o dedo",
                    "As folhas se curvam sob o dedo, com a luz e a sombra do papel. As bordas douradas mostram quanto você já "
                    "leu, e uma fitinha de tecido guarda a página onde parou.",
                    "turn", "Uma página se curvando ao virar, na tela interna do iPhone Duo"),
                   ("Destaque o que fala com você",
                    "Toque e segure uma palavra para destacar o versículo em uma de quatro cores. Cada destaque vira uma "
                    "citação para reler e compartilhar.",
                    "highlights", "João 3:16 destacado em amarelo numa página aberta"),
                   ("Ache qualquer versículo",
                    "Os 66 livros e todos os capítulos, com busca. Digite João 3:16 e vá direto ao texto.",
                    "books", "A lista de livros buscando João 3:16"),
               ],
               cards=[
                   ("Do seu jeito", "Quatro estilos de capa, seis cores de couro, seis ícones, tema claro e escuro e o "
                                    "tamanho de letra melhor para os seus olhos."),
                   ("Sem internet e sem anúncios", "Funciona no avião, na igreja e onde não há sinal. Sem anúncios e sem "
                                                   "distrações."),
                   ("Sua leitura é só sua", "Não pedimos conta e não coletamos dados. Seus destaques ficam no seu iPhone."),
               ],
               privacy="Política de privacidade", support="Suporte",
               translations_title="Três traduções completas",
               translations=["Português: Bíblia Livre, tradução baseada na Almeida", "English: King James Version (KJV)",
                             "Español: Reina-Valera 1909"],
               translations_note="Antigo e Novo Testamento, os 66 livros. O idioma muda nos Ajustes.",
               cta_title="Baixe a Bíblia Sagrada Fold",
               cta="Grátis na App Store. Feita só para o iPhone Duo, com iOS 27.1 ou posterior.",
               credits="Textos bíblicos: Bíblia Livre © 2018 Diego Santos, Mario Sérgio e Marco Teles (CC BY 4.0); King James "
                       "Version e Reina-Valera 1909 (domínio público). Textos via eBible.org.",
               legal="Apple, o logotipo da Apple e iPhone são marcas comerciais da Apple Inc. App Store é uma marca de "
                     "serviço da Apple Inc."),
    "es": dict(path="es/", html_lang="es", og_locale="es_MX", badge="es-mx", currency="USD",
               name="Santa Biblia Fold", short="Santa Biblia Fold",
               title="Santa Biblia Fold — la Santa Biblia como un libro, para iPhone Duo",
               description="La Santa Biblia completa como un libro de verdad en el iPhone Duo: dos páginas, cantos dorados y "
                           "hojas que pasas con el dedo. Reina-Valera 1909. Gratis, sin anuncios y sin internet.",
               tagline="La Biblia como un libro de verdad, hecha para el iPhone Duo.",
               facts="Gratis · Sin anuncios · Funciona sin internet",
               badge_alt="Descargar en la App Store",
               book_alt="La Biblia abierta en los Salmos, con cantos dorados y una cinta roja",
               sections=[
                   ("Cerrado, la cubierta. Abierto, el libro.",
                    "Con el iPhone Duo cerrado, la pantalla exterior muestra la cubierta de piel de tu Biblia. Deslízala para "
                    "abrirla y lee una página a la vez. Abre el iPhone Duo y la Biblia aparece abierta en dos páginas, como la que "
                    "tienes junto a la cama.",
                    "cover", "La cubierta de piel de la Biblia en la pantalla exterior del iPhone Duo"),
                   ("Pasa la página con el dedo",
                    "Las hojas se curvan bajo tu dedo, con la luz y la sombra del papel. Los cantos dorados muestran cuánto "
                    "has leído, y una cinta de tela guarda tu lugar.",
                    "turn", "Una página curvándose al pasar, en la pantalla interior del iPhone Duo"),
                   ("Resalta lo que te habla",
                    "Toca y mantén una palabra para resaltar el versículo en uno de cuatro colores. Cada resaltado se "
                    "convierte en una cita para releer y compartir.",
                    "highlights", "Juan 3:16 resaltado en amarillo en una página abierta"),
                   ("Encuentra cualquier versículo",
                    "Los 66 libros y todos los capítulos, con búsqueda. Escribe Juan 3:16 y ve directo al texto.",
                    "books", "La lista de libros buscando Juan 3:16"),
               ],
               cards=[
                   ("A tu manera", "Cuatro estilos de cubierta, seis colores de piel, seis iconos, tema claro y oscuro y el "
                                   "tamaño de letra que mejor le quede a tus ojos."),
                   ("Sin internet y sin anuncios", "Funciona en el avión, en la iglesia y donde no hay señal. Sin anuncios "
                                                   "ni distracciones."),
                   ("Tu lectura es solo tuya", "Sin cuenta y sin recopilar datos. Tus resaltados se quedan en tu iPhone."),
               ],
               privacy="Política de privacidad", support="Soporte",
               translations_title="Tres traducciones completas",
               translations=["Español: Reina-Valera 1909", "English: King James Version (KJV)",
                             "Português: Bíblia Livre, basada en la traducción Almeida"],
               translations_note="Antiguo y Nuevo Testamento, los 66 libros. El idioma se cambia en Ajustes.",
               cta_title="Descarga Santa Biblia Fold",
               cta="Gratis en la App Store. Hecha solo para el iPhone Duo, con iOS 27.1 o posterior.",
               credits="Textos bíblicos: Reina-Valera 1909 y King James Version (dominio público); Bíblia Livre © 2018 Diego "
                       "Santos, Mario Sérgio y Marco Teles (CC BY 4.0). Textos vía eBible.org.",
               legal="Apple, el logotipo de Apple y iPhone son marcas comerciales de Apple Inc. App Store es una marca de "
                     "servicio de Apple Inc."),
}
LANG_NAMES = {"pt": "Português", "en": "English", "es": "Español"}   # also the order of the language links
SHOTS = {"turn": (1400, 984), "highlights": (1400, 984), "books": (1400, 984), "cover": (700, 1018)}


def badge(p):
    # Apple's official badge, served by Apple Marketing Tools (their embed code hotlinks it).
    src = f"https://toolbox.marketingtools.apple.com/api/v2/badges/download-on-the-app-store/black/{p['badge']}"
    return (f"<a class='badge' href='{STORE}'><img src='{src}' alt='{html.escape(p['badge_alt'])}' "
            f"width='200' height='67'></a>")


def page(code):
    p = PAGES[code]
    e = html.escape
    root = "../" if p["path"] else ""
    url = BASE + p["path"]
    img = lambda name: f"{root}img/{code}/{name}.webp"
    alternates = "".join(f"<link rel='alternate' hreflang='{c}' href='{BASE + PAGES[c]['path']}'>\n" for c in PAGES)
    data = {
        "@context": "https://schema.org", "@type": "MobileApplication",
        "name": p["name"], "alternateName": p["short"], "description": p["description"],
        "operatingSystem": "iOS 27.1", "applicationCategory": "ReferenceApplication",
        "inLanguage": ["en", "pt-BR", "es"], "url": url, "downloadUrl": STORE,
        "image": f"{BASE}img/{code}/og.jpg",
        "screenshot": [f"{BASE}img/{code}/{s}.webp" for s in ("turn", "highlights", "books", "cover")],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": p["currency"]},
        "author": {"@type": "Person", "name": "Vinicius Ramos"},
    }   # no aggregateRating: only real ratings may go here
    link = lambda c: f"<a href='{root}{PAGES[c]['path'] or './'}' hreflang='{c}'"
    langs = "".join(link(c) + (" aria-current='page'" if c == code else "") + f">{LANG_NAMES[c]}</a>" for c in LANG_NAMES)
    footer_langs = " · ".join(link(c) + f">{LANG_NAMES[c]}</a>" for c in LANG_NAMES)
    sections = ""
    for i, (title, text, shot, alt) in enumerate(p["sections"]):
        w, h = SHOTS[shot]
        cls = "feature" + (" flip" if i % 2 else "") + (" portrait" if shot == "cover" else "")
        sections += (f"<section class='{cls}'><div><h2>{e(title)}</h2><p>{e(text)}</p></div>"
                     f"<figure><img src='{img(shot)}' alt='{e(alt)}' width='{w}' height='{h}' loading='lazy'></figure></section>\n")
    cards = "".join(f"<div><h3>{e(t)}</h3><p>{e(x)}</p></div>" for t, x in p["cards"])
    translations = "".join(f"<li>{e(t)}</li>" for t in p["translations"])
    links = f"{root}support.html?lang={code}", f"{root}privacy.html?lang={code}"
    return f"""<!doctype html>
<html lang="{p['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['description'])}">
<meta name="apple-itunes-app" content="app-id={APP_ID}">
<link rel="canonical" href="{url}">
{alternates}<link rel="alternate" hreflang="x-default" href="{BASE}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(p['description'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}img/{code}/og.jpg">
<meta property="og:locale" content="{p['og_locale']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}img/cross.svg">
<link rel="stylesheet" href="{root}style.css">
<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>
</head>
<body class="landing">
<div class="wrap">
<nav class="langs" aria-label="Idioma / Language / Idioma">{langs}</nav>
<header class="hero">
<div class="app-icon"><img src="{root}img/frame.svg" alt=""><img src="{root}img/cross.svg" alt=""></div>
<h1>{e(p['short'])}</h1>
<p class="tagline">{e(p['tagline'])}</p>
{badge(p)}
<p class="facts">{e(p['facts'])}</p>
</header>
</div>
<img class="book" src="{img('book')}" alt="{e(p['book_alt'])}" width="1920" height="824">
<main class="wrap">
{sections}<section class="cards">{cards}</section>
<section class="translations"><h2>{e(p['translations_title'])}</h2><ul>{translations}</ul><p>{e(p['translations_note'])}</p></section>
<section class="cta"><h2>{e(p['cta_title'])}</h2><p>{e(p['cta'])}</p>{badge(p)}</section>
</main>
<footer class="wrap site">
<p><a href="{links[0]}">{e(p['support'])}</a> · <a href="{links[1]}">{e(p['privacy'])}</a> · {footer_langs}</p>
<p>{e(p['credits'])}</p>
<p>{e(p['legal'])}</p>
</footer>
</body>
</html>
"""


def sitemap():
    alt = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{BASE + PAGES[c]["path"]}"/>' for c in PAGES)
    urls = "".join(f"<url><loc>{BASE + PAGES[c]['path']}</loc>{alt}</url>\n" for c in PAGES)
    urls += "".join(f"<url><loc>{BASE}{f}</loc></url>\n" for f in ("support.html", "privacy.html"))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            f'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n')


if __name__ == "__main__":
    for code, p in PAGES.items():
        out = os.path.join(HERE, p["path"], "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w").write(page(code))
        print("wrote", out)
    open(os.path.join(HERE, "sitemap.xml"), "w").write(sitemap())
    print("wrote sitemap.xml")
