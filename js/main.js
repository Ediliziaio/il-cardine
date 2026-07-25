// Il Cardine — JS minimo (progressive enhancement, nessuna dipendenza, defer)
(function () {
  "use strict";

  // Rispetta prefers-reduced-motion per ogni comportamento di scroll
  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // --- Data corrente nella topbar (formato italiano) ---
  var dateEl = document.querySelector("[data-tb-date]");
  if (dateEl) {
    var fmt = new Intl.DateTimeFormat("it-IT", {
      weekday: "long", day: "numeric", month: "long", year: "numeric"
    });
    var s = fmt.format(new Date());
    dateEl.textContent = s.charAt(0).toUpperCase() + s.slice(1);
  }

  // --- Anno corrente nel footer ---
  var yearEls = document.querySelectorAll("[data-year]");
  for (var i = 0; i < yearEls.length; i++) {
    yearEls[i].textContent = new Date().getFullYear();
  }

  // --- Menu mobile: toggle hamburger ---
  var nav = document.querySelector(".mainnav");
  var toggle = document.querySelector(".nav-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var isOpen = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", String(!isOpen));
      toggle.setAttribute("aria-expanded", String(!isOpen));
    });
    // Chiudi il menu quando si attiva una voce (navigazione su mobile)
    nav.addEventListener("click", function (ev) {
      if (ev.target.closest("a") && nav.getAttribute("data-open") === "true") {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // --- Smooth scroll per ancore TOC (solo se motion consentito) ---
  if (!reducedMotion) {
    document.addEventListener("click", function (ev) {
      var link = ev.target.closest('a[href^="#"]');
      if (!link) return;
      var id = link.getAttribute("href");
      if (id.length < 2) return;
      var target = document.getElementById(id.slice(1));
      if (!target) return;
      ev.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
      // Sposta il focus sull'ancora per accessibilità da tastiera
      if (!target.hasAttribute("tabindex")) target.setAttribute("tabindex", "-1");
      target.focus({ preventScroll: true });
      if (window.history && window.history.replaceState) {
        window.history.replaceState(null, "", id);
      }
    });
  }

  /* ============================================================
     Ricerca client-side (pagina /cerca/)
     - attiva solo se esiste #search-app nella pagina
     - indice: /assets/search-index.json (generato da tools/build_search_index.py)
     - filtra su title + excerpt + category, case-insensitive, min 2 caratteri
     - ranking semplice: i match nel titolo vengono prima
     - legge il parametro ?q= dall'URL all'apertura (coerente con SearchAction /cerca?q=)
     - nessuna dipendenza esterna
     ============================================================ */
  (function () {
    var app = document.getElementById("search-app");
    if (!app) return;

    var input = document.getElementById("q");
    var countEl = document.getElementById("search-count");
    var listEl = document.getElementById("search-results");
    var index = [];
    var MAX_RESULTS = 20;
    var MIN_CHARS = 2;

    var fmtDate = new Intl.DateTimeFormat("it-IT", {
      day: "numeric", month: "long", year: "numeric"
    });

    function esc(str) {
      var div = document.createElement("div");
      div.textContent = str;
      return div.innerHTML;
    }

    function formatDate(iso) {
      var d = new Date(iso);
      if (isNaN(d.getTime())) return "";
      return fmtDate.format(d);
    }

    function render(results, query) {
      listEl.innerHTML = "";
      if (query.length < MIN_CHARS) {
        countEl.textContent = "Digita almeno " + MIN_CHARS + " caratteri per iniziare la ricerca.";
        return;
      }
      if (!results.length) {
        countEl.textContent = "Nessun risultato per \u201C" + query + "\u201D. Prova con altre parole chiave.";
        return;
      }
      countEl.textContent = results.length === 1
        ? "1 risultato per \u201C" + query + "\u201D"
        : results.length + " risultati per \u201C" + query + "\u201D";
      for (var i = 0; i < results.length; i++) {
        var item = results[i];
        var li = document.createElement("li");
        li.className = "sr-item";
        li.innerHTML =
          '<h2 class="sr-title"><a href="' + esc(item.url) + '">' + esc(item.title) + "</a></h2>" +
          '<p class="sr-meta"><span class="sr-cat">' + esc(item.category) + "</span>" +
          (item.date ? ' · <time datetime="' + esc(item.date) + '">' + esc(formatDate(item.date)) + "</time>" : "") +
          "</p>" +
          '<p class="sr-excerpt">' + esc(item.excerpt) + "</p>";
        listEl.appendChild(li);
      }
    }

    function search(query) {
      var q = query.trim().toLowerCase();
      if (q.length < MIN_CHARS) return [];
      var inTitle = [];
      var inRest = [];
      for (var i = 0; i < index.length; i++) {
        var item = index[i];
        var title = item.title.toLowerCase();
        if (title.indexOf(q) !== -1) {
          inTitle.push(item);
        } else if (
          item.excerpt.toLowerCase().indexOf(q) !== -1 ||
          item.category.toLowerCase().indexOf(q) !== -1
        ) {
          inRest.push(item);
        }
      }
      return inTitle.concat(inRest).slice(0, MAX_RESULTS);
    }

    var debounceTimer = null;
    function onInput() {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(function () {
        render(search(input.value), input.value.trim());
      }, 120);
    }

    // Carica l'indice, poi esegue la ricerca iniziale (parametro ?q= o campo già compilato)
    fetch("/assets/search-index.json")
      .then(function (res) {
        if (!res.ok) throw new Error("HTTP " + res.status);
        return res.json();
      })
      .then(function (data) {
        index = data;
        var params = new URLSearchParams(window.location.search);
        var initial = (params.get("q") || "").trim();
        if (initial && !input.value) input.value = initial;
        input.addEventListener("input", onInput);
        if (input.value.trim().length >= MIN_CHARS) {
          render(search(input.value), input.value.trim());
        } else {
          countEl.textContent = "Digita almeno " + MIN_CHARS + " caratteri per cercare tra " + index.length + " articoli.";
        }
      })
      .catch(function () {
        countEl.textContent = "La ricerca non è disponibile al momento. Riprova più tardi.";
      });
  })();

  /* ============================================================
     Cookie banner (leggero, zero CLS, nessuno script di terze parti)
     - mostrato solo se localStorage 'ic-cookie-consent' è assente
     - scelta salvata in localStorage ('accepted' | 'rejected')
     - inserito dopo requestIdleCallback per non impattare il rendering
     ============================================================ */
  (function () {
    var STORAGE_KEY = "ic-cookie-consent";
    var saved = null;
    try {
      saved = window.localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      saved = null;
    }
    if (saved) return;

    function buildBanner() {
      var banner = document.createElement("div");
      banner.className = "cookie-banner";
      banner.setAttribute("role", "dialog");
      banner.setAttribute("aria-label", "Informativa breve sui cookie");
      banner.setAttribute("aria-live", "polite");
      banner.innerHTML =
        '<p class="cb-text">Questo sito usa solo cookie tecnici e, previo consenso, strumenti di misurazione anonima. ' +
        'Dettagli nella <a href="/cookie-policy/">cookie policy</a>.</p>' +
        '<div class="cb-actions">' +
        '<button type="button" class="cb-btn cb-reject" data-consent="rejected">Rifiuta</button>' +
        '<button type="button" class="cb-btn cb-accept" data-consent="accepted">Accetta</button>' +
        "</div>";

      banner.addEventListener("click", function (ev) {
        var btn = ev.target.closest("[data-consent]");
        if (!btn) return;
        try {
          window.localStorage.setItem(STORAGE_KEY, btn.getAttribute("data-consent"));
        } catch (e) {
          /* storage non disponibile: chiudi comunque il banner */
        }
        banner.classList.add("is-hiding");
        var remove = function () {
          if (banner.parentNode) banner.parentNode.removeChild(banner);
        };
        if (reducedMotion) {
          remove();
        } else {
          banner.addEventListener("transitionend", remove, { once: true });
        }
      });

      document.body.appendChild(banner);
      // attiva la transizione di ingresso solo dopo il primo paint (zero CLS)
      window.requestAnimationFrame(function () {
        banner.classList.add("is-visible");
      });
    }

    var schedule = window.requestIdleCallback || function (cb) {
      return setTimeout(cb, 1500);
    };
    if (document.readyState === "complete" || document.readyState === "interactive") {
      schedule(buildBanner);
    } else {
      document.addEventListener("DOMContentLoaded", function () {
        schedule(buildBanner);
      });
    }
  })();
})();
