// One page, three languages: the browser's language picks one (?lang=pt|en|es overrides), the buttons switch.
const EMAIL = "suporte@exemplo.com";   // TODO: the support email shown on both pages

document.querySelectorAll("a.email").forEach(a => { a.href = "mailto:" + EMAIL; a.textContent = EMAIL; });

function show(lang) {
  document.querySelectorAll("article").forEach(a => { a.hidden = a.dataset.lang !== lang; });
  document.querySelectorAll(".langs button").forEach(b => b.setAttribute("aria-pressed", b.dataset.lang === lang));
  document.documentElement.lang = document.querySelector(`article[data-lang="${lang}"]`).lang;
}

const asked = new URLSearchParams(location.search).get("lang");
const browser = (navigator.language || "en").slice(0, 2);
show(["pt", "en", "es"].find(l => l === asked) || (["pt", "es"].includes(browser) ? browser : "en"));
document.querySelectorAll(".langs button").forEach(b => b.addEventListener("click", () => show(b.dataset.lang)));
