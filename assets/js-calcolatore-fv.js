/* Il Cardine — dimensionamento fotovoltaico, costo e tempo di rientro.
   Costi, produzione e quota di autoconsumo con accumulo provengono dalle
   rilevazioni pubblicate su questo sito (fotovoltaico: costi 2026).
   Valori indicativi: non sostituiscono un sopralluogo. */
(function () {
  'use strict';
  // Taglia: [kWp, costoMin, costoMax, prodMin, prodMax, consumoMaxTipico]
  var TAGLIE = [
    { kwp: 3,   cmin: 4000,  cmax: 5500,  pmin: 3300, pmax: 4500,  fino: 3000 },
    { kwp: 4.5, cmin: 6000,  cmax: 8000,  pmin: 5000, pmax: 6700,  fino: 4500 },
    { kwp: 6,   cmin: 7500,  cmax: 10500, pmin: 6600, pmax: 9000,  fino: 7000 },
    { kwp: 9,   cmin: 10500, cmax: 15000, pmin: 8800, pmax: 15000, fino: 99999 }
  ];
  var ACCUMULO_EXTRA = [4500, 5500];   // 6 kW: da 7.500-10.500 a 12.000-16.000 €
  var AUTOCONS_SENZA = 0.35;           // stima di settore
  var AUTOCONS_CON   = 0.75;           // 70-80% da tabella del sito
  var DETRAZIONE     = 0.50;

  function el(id) { return document.getElementById(id); }
  function eur(n) { return Math.round(n).toLocaleString('it-IT', { useGrouping: true }) + ' €'; }
  function kwh(n) { return Math.round(n).toLocaleString('it-IT', { useGrouping: true }) + ' kWh'; }

  function calcola() {
    var consumo = parseFloat(el('consumo').value);
    var prezzo  = parseFloat((el('prezzo').value || '').toString().replace(',', '.'));
    var acc     = el('accumulo').checked;
    var out     = el('fv-out');
    if (!isFinite(consumo) || consumo <= 0 || !isFinite(prezzo) || prezzo <= 0) {
      out.innerHTML = '<p class="calc-hint">Inserisci consumo annuo e prezzo dell’energia per vedere la stima.</p>';
      return;
    }
    var t = TAGLIE.find(function (x) { return consumo <= x.fino; }) || TAGLIE[TAGLIE.length - 1];
    var cmin = t.cmin + (acc ? ACCUMULO_EXTRA[0] : 0);
    var cmax = t.cmax + (acc ? ACCUMULO_EXTRA[1] : 0);
    var prod = (t.pmin + t.pmax) / 2;
    var quota = acc ? AUTOCONS_CON : AUTOCONS_SENZA;
    var autocons = Math.min(prod * quota, consumo);
    var risparmio = autocons * prezzo;
    var costoMedio = (cmin + cmax) / 2;
    var netto = costoMedio * (1 - DETRAZIONE);
    var rientro = risparmio > 0 ? netto / risparmio : 0;

    out.innerHTML =
      '<table class="calc-table"><caption>Stima per un consumo di ' + kwh(consumo) + ' all’anno</caption><tbody>' +
      '<tr><th scope="row">Taglia consigliata</th><td><strong>' + t.kwp.toLocaleString('it-IT') + ' kWp' + (acc ? ' + accumulo' : '') + '</strong></td></tr>' +
      '<tr><th scope="row">Costo chiavi in mano</th><td>' + eur(cmin) + ' – ' + eur(cmax) + '</td></tr>' +
      '<tr><th scope="row">Produzione annua stimata</th><td>' + kwh(prod) + '</td></tr>' +
      '<tr><th scope="row">Energia autoconsumata (' + Math.round(quota * 100) + '%)</th><td>' + kwh(autocons) + '</td></tr>' +
      '<tr><th scope="row">Risparmio annuo in bolletta</th><td><strong>' + eur(risparmio) + '</strong></td></tr>' +
      '<tr><th scope="row">Costo netto dopo detrazione 50%</th><td>' + eur(netto) + '</td></tr>' +
      '<tr><th scope="row">Tempo di rientro</th><td><strong>' + rientro.toFixed(1).replace('.', ',') + ' anni</strong></td></tr>' +
      '</tbody></table>' +
      '<p class="calc-note">La quota di autoconsumo è il parametro che pesa di più: ' +
      (acc ? 'con l’accumulo sale al 70-80% perché l’energia prodotta di giorno viene usata la sera.'
           : 'senza accumulo si attesta tipicamente sul 30-40%, perché il grosso della produzione avviene quando in casa non c’è nessuno.') +
      ' Il rientro non tiene conto di eventuali rincari dell’energia, che lo accorciano.</p>';
  }

  function init() {
    ['consumo', 'prezzo'].forEach(function (id) { var e = el(id); if (e) e.addEventListener('input', calcola); });
    var a = el('accumulo'); if (a) a.addEventListener('change', calcola);
    if (el('consumo')) calcola();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
