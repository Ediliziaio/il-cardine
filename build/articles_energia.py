# -*- coding: utf-8 -*-
"""Contenuti articoli silo efficienza-energetica (4 articoli)."""

PILLAR = "/efficienza-energetica/pannelli-solari-guida/"
COSTI = "/efficienza-energetica/fotovoltaico-costi-2026/"
INCENTIVI = "/efficienza-energetica/fotovoltaico-incentivi-2026/"
POMPE = "/efficienza-energetica/pompe-di-calore-come-funzionano/"
CAPPOTTO = "/efficienza-energetica/cappotto-termico-esterno-guida/"
BONUS_RIST = "/incentivi-bonus/bonus-ristrutturazione-2026-guida/"
CONTO_TERMICO = "/incentivi-bonus/conto-termico-3-guida/"

MF = dict(
    author="Marco Ferreri", initials="MF",
    role="Redazione Il Cardine · Efficienza energetica",
    bio="Giornalista tecnico, segue da oltre dieci anni efficienza energetica, rinnovabili e mercato delle costruzioni. Per Il Cardine cura le guide su fotovoltaico, pompe di calore e incentivi per la riqualificazione degli edifici.",
)
GS = dict(
    author="Giulia Santoro", initials="GS",
    role="Redazione Il Cardine · Incentivi e fisco edile",
    bio="Giornalista specializzata in fiscalità degli interventi edilizi e incentivi energetici. Per Il Cardine segue bonus casa, Conto Termico, comunità energetiche e le pratiche ENEA e GSE per la riqualificazione.",
)
LB = dict(
    author="Luca Bianchi", initials="LB",
    role="Redazione Il Cardine · Involucro edilizio e materiali",
    bio="Ingegnere edile e giornalista tecnico, si occupa di involucro, isolamento e materiali da costruzione. Per Il Cardine scrive guide su cappotti termici, murature e prestazioni energetiche degli edifici esistenti.",
)

REL_COSTI = [
    dict(href=PILLAR, thumb="t-energia", cat="Efficienza Energetica",
         title="Pannelli solari: la guida definitiva 2026 — costi, incentivi e installazione",
         excerpt="La guida pillar: tecnologie, prezzi, incentivi e iter completo di installazione.",
         date="21 lug 2026", mins="11 min"),
    dict(href=INCENTIVI, thumb="t-energia", cat="Efficienza Energetica",
         title="Incentivi fotovoltaico 2026: detrazione 50%, comunità energetiche e ritiro dedicato",
         excerpt="Tutte le agevolazioni utilizzabili nel 2026 e come combinarle senza errori.",
         date="15 lug 2026", mins="8 min"),
    dict(href=POMPE, thumb="t-energia", cat="Efficienza Energetica",
         title="Pompa di calore: come funziona, consumi reali e quando conviene",
         excerpt="Il partner ideale del fotovoltaico: COP, consumi e abbinamento con l'impianto solare.",
         date="10 lug 2026", mins="9 min"),
]
REL_INCENTIVI = [
    dict(href=PILLAR, thumb="t-energia", cat="Efficienza Energetica",
         title="Pannelli solari: la guida definitiva 2026 — costi, incentivi e installazione",
         excerpt="La guida pillar: tecnologie, prezzi, incentivi e iter completo di installazione.",
         date="21 lug 2026", mins="11 min"),
    dict(href=COSTI, thumb="t-energia", cat="Efficienza Energetica",
         title="Quanto costa un impianto fotovoltaico nel 2026: prezzi al kWp e tempi di rientro",
         excerpt="Prezzi reali per taglia di impianto, voci di costo nascoste e ritorno dell'investimento.",
         date="18 lug 2026", mins="9 min"),
    dict(href=CAPPOTTO, thumb="t-energia", cat="Efficienza Energetica",
         title="Cappotto termico esterno: materiali, costi al mq e detrazioni 2026",
         excerpt="L'intervento che riduce il fabbisogno: materiali a confronto e agevolazioni.",
         date="6 lug 2026", mins="10 min"),
]
REL_POMPE = [
    dict(href=PILLAR, thumb="t-energia", cat="Efficienza Energetica",
         title="Pannelli solari: la guida definitiva 2026 — costi, incentivi e installazione",
         excerpt="La guida pillar: tecnologie, prezzi, incentivi e iter completo di installazione.",
         date="21 lug 2026", mins="11 min"),
    dict(href=COSTI, thumb="t-energia", cat="Efficienza Energetica",
         title="Quanto costa un impianto fotovoltaico nel 2026: prezzi al kWp e tempi di rientro",
         excerpt="Prezzi reali per taglia di impianto, voci di costo nascoste e ritorno dell'investimento.",
         date="18 lug 2026", mins="9 min"),
    dict(href=CAPPOTTO, thumb="t-energia", cat="Efficienza Energetica",
         title="Cappotto termico esterno: materiali, costi al mq e detrazioni 2026",
         excerpt="L'intervento che riduce il fabbisogno: materiali a confronto e agevolazioni.",
         date="6 lug 2026", mins="10 min"),
]
REL_CAPPOTTO = [
    dict(href=PILLAR, thumb="t-energia", cat="Efficienza Energetica",
         title="Pannelli solari: la guida definitiva 2026 — costi, incentivi e installazione",
         excerpt="La guida pillar: tecnologie, prezzi, incentivi e iter completo di installazione.",
         date="21 lug 2026", mins="11 min"),
    dict(href=POMPE, thumb="t-energia", cat="Efficienza Energetica",
         title="Pompa di calore: come funziona, consumi reali e quando conviene",
         excerpt="Dopo il cappotto, la pompa di calore rende al massimo: COP e consumi reali.",
         date="10 lug 2026", mins="9 min"),
    dict(href=INCENTIVI, thumb="t-energia", cat="Efficienza Energetica",
         title="Incentivi fotovoltaico 2026: detrazione 50%, comunità energetiche e ritiro dedicato",
         excerpt="Tutte le agevolazioni utilizzabili nel 2026 e come combinarle senza errori.",
         date="15 lug 2026", mins="8 min"),
]

ARTICOLI_ENERGIA = [

# ───────────────────────────── 1. FOTOVOLTAICO COSTI 2026 ─────────────────────
dict(
    silo="efficienza-energetica", silo_name="Efficienza Energetica",
    slug="fotovoltaico-costi-2026",
    title_tag="Costo impianto fotovoltaico 2026: prezzi al kWp",
    desc="Costo impianto fotovoltaico 2026: prezzi chiavi in mano da 1.300 a 1.800 €/kWp, costo con accumulo, voci di preventivo e tempi di rientro reali.",
    h1="Quanto costa un impianto fotovoltaico nel 2026: prezzi al kWp e tempi di rientro",
    kicker="Efficienza Energetica · Prezzi 2026",
    standfirst="Da 1.300 a 1.800 euro al kWp chiavi in mano, con l'accumulo che aggiunge 3.500-6.000 euro: ecco quanto costa davvero un impianto fotovoltaico nel 2026, voce per voce, e in quanti anni si ripaga con la detrazione del 50%.",
    breadcrumb_title="Fotovoltaico: costi 2026",
    pub="2026-07-18", pub_it="18 luglio 2026", mod="2026-07-18", mod_it="18 luglio 2026",
    read_min=9,
    thumb="t-energia", thumb_label="Efficienza Energetica · Prezzi 2026",
    thumb_aria="Copertura editoriale: costi del fotovoltaico 2026",
    keywords="costo impianto fotovoltaico, prezzo fotovoltaico al kWp, costo fotovoltaico 2026, tempi di rientro fotovoltaico, fotovoltaico con accumulo prezzo",
    og_title="Quanto costa un impianto fotovoltaico nel 2026: prezzi al kWp e tempi di rientro",
    og_desc="Prezzi chiavi in mano per taglia di impianto, voci di costo, accumulo e tempi di rientro con la detrazione del 50%: l'analisi completa.",
    tw_title="Costo impianto fotovoltaico 2026: prezzi al kWp",
    tw_desc="Da 1.300 a 1.800 €/kWp chiavi in mano: prezzi per taglia, accumulo e tempi di rientro reali del fotovoltaico nel 2026.",
    answer="Nel 2026 il <strong>costo di un impianto fotovoltaico</strong> domestico chiavi in mano è di 1.300-1.800 euro al kWp: un 3 kW costa 4.000-5.500 euro, un 6 kW 7.500-10.500 euro, IVA e posa incluse. Con la detrazione del 50% la spesa netta si dimezza e il rientro avviene in 5-8 anni, meno con accumulo e autoconsumo elevato.",
    toc=[
        ("prezzi-al-kwp", "Quanto costa un impianto fotovoltaico al kWp nel 2026?"),
        ("voci-di-costo", "Quali voci compongono il prezzo dell'impianto?"),
        ("prezzi-per-taglia", "I prezzi per taglia di impianto, da 3 a 10 kW"),
        ("costo-accumulo", "Quanto incide il sistema di accumulo sul costo?"),
        ("tempi-di-rientro", "In quanti anni si ripaga l'investimento?"),
        ("come-risparmiare", "Come ridurre il costo dell'impianto fotovoltaico"),
        ("confrontare-preventivi", "Come leggere e confrontare i preventivi"),
    ],
    body="""          <h2 id="prezzi-al-kwp">Quanto costa un impianto fotovoltaico al kWp nel 2026?</h2>
          <p>Il <strong>costo di un impianto fotovoltaico</strong> residenziale nel 2026 si misura in euro per kilowatt di picco (€/kWp) e si colloca, per il chiavi in mano, tra <strong>1.300 e 1.800 euro al kWp</strong>. La forchetta dipende dalla taglia: sotto i 3 kW il prezzo unitario sale verso 1.700-1.900 €/kWp perché i costi fissi (progettazione, pratiche, ponteggio) si spalmano su pochi pannelli; sopra i 6 kW scende verso 1.250-1.450 €/kWp. Sono valori che includono moduli, inverter, struttura, manodopera, pratiche GSE e IVA agevolata al 10%.</p>
          <p>Rispetto al picco del 2022-2023, quando la crisi dei materiali e la corsa al Superbonus avevano spinto i listini oltre i 2.200 €/kWp, il mercato si è normalizzato: i moduli fotovoltaici costano oggi il 60-70% in meno di dieci anni fa e la concorrenza tra installatori è tornata a premiare chi confronta più preventivi. Il risultato è che nel 2026 il fotovoltaico domestico è tornato ad essere un investimento valutabile con un semplice foglio di calcolo, come spieghiamo nella <a href="/efficienza-energetica/pannelli-solari-guida/">guida ai pannelli solari</a> del nostro silo.</p>
          <p>Attenzione però alle offerte «sottocosto»: un preventivo sotto i 1.100 €/kWp chiavi in mano va letto con sospetto, perché spesso esclude ponteggio, pratiche di connessione o garanzie reali. Al contrario, sopra i 2.000 €/kWp senza accumulo il sovrapprezzo raramente è giustificato dalla qualità dei componenti.</p>

          <h2 id="voci-di-costo">Quali voci compongono il prezzo dell'impianto?</h2>
          <p>Capire il costo di un impianto fotovoltaico significa scomporlo nelle sue voci. In un impianto domestico tipo da 6 kW, il peso percentuale medio delle componenti è il seguente:</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Incidenza media delle voci di costo su un impianto da 6 kW (Italia, 2026)</caption>
            <thead>
              <tr><th>Voce di costo</th><th>Incidenza sul totale</th><th>Importo indicativo su 9.000 €</th><th>Note</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Moduli fotovoltaici</strong></td><td>30-35%</td><td>2.700-3.150 €</td><td>Monocristallini TOPCon/HJT da 430-460 Wp</td></tr>
              <tr><td><strong>Inverter</strong></td><td>12-15%</td><td>1.100-1.350 €</td><td>Stringa o ibrido predisposto per accumulo</td></tr>
              <tr><td><strong>Struttura e materiali elettrici</strong></td><td>10-12%</td><td>900-1.100 €</td><td>Binari, cavi, quadri, scaricatori</td></tr>
              <tr><td><strong>Manodopera e ponteggio</strong></td><td>25-30%</td><td>2.250-2.700 €</td><td>2-4 giorni di cantiere, linee vita incluse</td></tr>
              <tr><td><strong>Progettazione e pratiche</strong></td><td>8-12%</td><td>700-1.100 €</td><td>Comune, distributore, GSE, DiCo</td></tr>
              <tr><td><strong>Margine installatore</strong></td><td>10-15%</td><td>900-1.350 €</td><td>Garanzie, assistenza, gestione cantiere</td></tr>
            </tbody>
          </table>
          </div>
          <p>Tre voci gonfiano i preventivi senza aggiungere valore reale: le strutture di sostegno «speciali» proposte su tetti che non ne hanno bisogno, i pacchetti di manutenzione pluriennale venduti come obbligatori (per legge non esiste alcun obbligo di manutenzione programmata sul residenziale) e le batterie sottodimensionate rivendute come upgrade a fine trattativa. La regola pratica è chiedere sempre il preventivo analitico, non il prezzo «a corpo».</p>

          <h2 id="prezzi-per-taglia">I prezzi per taglia di impianto, da 3 a 10 kW</h2>
          <p>Il modo più rapido per stimare il costo di un impianto fotovoltaico è partire dai consumi annui in bolletta: indicativamente, ogni 1.000 kWh consumati richiedono 0,8-1 kWp di potenza installata. Ecco i prezzi medi chiavi in mano rilevati sui listini italiani a luglio 2026.</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 2 — Costo impianto fotovoltaico per taglia, chiavi in mano (IVA 10% inclusa, 2026)</caption>
            <thead>
              <tr><th>Taglia</th><th>Prezzo medio</th><th>€/kWp</th><th>Produzione annua</th><th>Profilo tipo</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>3 kW</strong></td><td>4.000-5.500 €</td><td>1.400-1.800</td><td>3.300-4.500 kWh</td><td>Coppie, consumi fino a 3.000 kWh/anno</td></tr>
              <tr><td><strong>4,5 kW</strong></td><td>6.000-8.000 €</td><td>1.350-1.750</td><td>5.000-6.700 kWh</td><td>Famiglia tipo, 3.500-4.500 kWh/anno</td></tr>
              <tr><td><strong>6 kW</strong></td><td>7.500-10.500 €</td><td>1.300-1.700</td><td>6.600-9.000 kWh</td><td>Pompa di calore o induzione, 5.000+ kWh/anno</td></tr>
              <tr><td><strong>8-10 kW</strong></td><td>10.500-15.000 €</td><td>1.250-1.500</td><td>8.800-15.000 kWh</td><td>Ville con auto elettrica e climatizzazione estiva</td></tr>
              <tr><td><strong>6 kW + accumulo 10 kWh</strong></td><td>12.000-16.000 €</td><td>—</td><td>Autoconsumo 70-80%</td><td>Consumi serali elevati, massima indipendenza</td></tr>
            </tbody>
          </table>
          </div>
          <p>La produzione annua varia sensibilmente con la latitudine: lo stesso kWp installato rende circa 1.100 kWh/anno in Lombardia, 1.250-1.350 in Toscana e fino a 1.500-1.600 in Sicilia. Per questo il prezzo al kWp non basta a giudicare la convenienza: conta il costo per kWh prodotto, che al Sud scende sotto i 6 centesimi su vita utile trentennale.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="costo-accumulo">Quanto incide il sistema di accumulo sul costo?</h2>
          <p>La batteria è la voce discrezionale che più sposta il budget: un accumulo al litio da 5 kWh aggiunge <strong>3.500-4.500 euro</strong>, uno da 10 kWh <strong>5.000-6.500 euro</strong>, inverter ibrido compreso. Il prezzo per kWh immagazzinato si colloca tra 500 e 650 euro, in calo rispetto agli oltre 800 del 2023 ma ancora la metà circa del valore dell'intero impianto base.</p>
          <p>L'accumulo conviene quando i consumi sono concentrati la sera e nei weekend — profilo tipico delle famiglie che lavorano fuori casa — perché porta la quota di autoconsumo dal 30-35% al 70-80%. Conviene meno quando in casa c'è qualcuno di giorno, quando la <a href="/efficienza-energetica/pompe-di-calore-come-funzionano/">pompa di calore</a> lavora nelle ore centrali o quando si aderisce a una comunità energetica che valorizza l'energia condivisa, come spieghiamo nell'articolo sugli <a href="/efficienza-energetica/fotovoltaico-incentivi-2026/">incentivi fotovoltaico 2026</a>.</p>
          <p>Un'alternativa intermedia è l'<strong>inverter ibrido senza batteria</strong>: costa 300-500 euro in più di un inverter di stringa ma lascia aperta la possibilità di aggiungere l'accumulo in un secondo momento senza sostituire componenti. È la scelta che consigliamo a chi oggi è indeciso.</p>

          <h2 id="tempi-di-rientro">In quanti anni si ripaga l'investimento?</h2>
          <p>Il tempo di rientro dipende da tre leve: prezzo dell'energia elettrica, quota di autoconsumo e agevolazioni. Con la <strong>detrazione fiscale del 50%</strong> — che sulla prima casa recupera metà della spesa in dieci rate annuali, come dettagliato nella <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">guida al bonus ristrutturazione 2026</a> — il costo netto di un 6 kW pagato 9.000 euro scende a 4.500 euro effettivi.</p>
          <p>Mettiamo i numeri in fila per una famiglia del Centro Italia con 4.800 kWh di consumi annui e un impianto da 4,5 kW pagato 7.200 euro: detrazione 50% → spesa netta 3.600 euro; autoconsumo diretto → 550-650 euro l'anno di bolletta risparmiata; energia immessa in rete con ritiro dedicato → 150-250 euro l'anno. Totale beneficio: circa 750-850 euro l'anno, per un <strong>rientro in 5-6 anni</strong> a fronte di una vita utile di almeno 30.</p>
          <p>Al Sud, dove lo stesso impianto produce il 25-30% in più, il rientro scende a 4-5 anni; al Nord senza accumulo e con autoconsumo basso può salire a 7-8 anni. In tutti i casi, il rendimento netto supera ampiamente quello di un impiego finanziario prudente, e cresce se in casa arrivano pompa di calore, piano a induzione o auto elettrica.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="come-risparmiare">Come ridurre il costo dell'impianto fotovoltaico</h2>
          <p>Cinque mosse pratiche riducono la spesa senza sacrificare la qualità:</p>
          <ol>
            <li><strong>Dimensionare sui consumi reali</strong>: un impianto tarato sulle bollette degli ultimi 12 mesi evita il sovradimensionamento, l'errore più costoso in assoluto.</li>
            <li><strong>Confrontare almeno tre preventivi analitici</strong>: a parità di componenti le differenze tra installatori arrivano al 20-25%.</li>
            <li><strong>Sfruttare la detrazione del 50%</strong> pagando con bonifico parlante e conservando fatture e Dichiarazione di Conformità.</li>
            <li><strong>Valutare il Conto Termico 3.0</strong> per gli interventi combinati con solare termico, ricordando che non è cumulabile con la detrazione sulla stessa spesa: i dettagli nella <a href="/incentivi-bonus/conto-termico-3-guida/">guida al Conto Termico 3.0</a>.</li>
            <li><strong>Ragionare sul tetto prima dei pannelli</strong>: se la copertura è a fine vita, conviene abbinare il rifacimento del manto — magari con un <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico esterno</a> sulle pareti — in un unico cantiere con ponteggio condiviso.</li>
          </ol>

          <h2 id="confrontare-preventivi">Come leggere e confrontare i preventivi</h2>
          <p>Un preventivo serio indica marca e modello di moduli e inverter, potenza totale e producibilità stimata, schema di stringa, garanzie di prodotto e di resa, tempi di cantiere, voci incluse ed escluse (ponteggio, pratiche, oneri di connessione). Diffidare dei documenti che riportano solo «impianto da 6 kW, prezzo totale».</p>
          <p>Tre controlli finali prima di firmare: verificare che l'installatore sia abilitato FER secondo il DM 37/2008 e rilasci la Dichiarazione di Conformità; chiedere lo schema unifilare e il manuale d'uso; farsi indicare per iscritto chi gestisce la pratica GSE per il ritiro dedicato. Con questi elementi, il costo dell'impianto fotovoltaico smette di essere un numero opaco e diventa un investimento confrontabile, misurabile e difendibile nel tempo.</p>""",
    faq_title="Domande frequenti sul costo del fotovoltaico",
    faq=[
        ("Qual è il costo di un impianto fotovoltaico da 6 kW nel 2026?",
         "Un impianto fotovoltaico da 6 kW chiavi in mano costa nel 2026 tra <strong>7.500 e 10.500 euro</strong>, IVA al 10% e installazione comprese. Con la detrazione del 50% la spesa effettiva scende a 3.750-5.250 euro recuperate in dieci rate annuali. Il prezzo unitario si aggira su 1.300-1.700 euro al kWp."),
        ("Quanto costa un impianto fotovoltaico da 3 kW per un appartamento?",
         "Un 3 kW, taglia adatta a consumi fino a 3.000 kWh l'anno, costa indicativamente <strong>4.000-5.500 euro</strong> chiavi in mano. Il prezzo al kWp è più alto delle taglie grandi (1.400-1.800 €/kWp) perché i costi fissi di progettazione, pratiche e ponteggio si spalmano su pochi moduli."),
        ("Conviene aggiungere subito la batteria di accumulo?",
         "Dipende dal profilo di consumo: se i consumi sono concentrati la sera, l'accumulo porta l'autoconsumo dal 30-35% al 70-80% e si ripaga. Se in casa c'è qualcuno di giorno o si aderisce a una comunità energetica, spesso conviene installare solo l'inverter ibrido (300-500 euro in più) e aggiungere la batteria in seguito."),
        ("La detrazione del 50% vale anche per il fotovoltaico con accumulo?",
         "Sì: la detrazione del 50% sulla prima casa (36% sulle altre unità) copre l'intero impianto, accumulo incluso, entro il massimale di 96.000 euro. Serve il bonifico parlante e la conservazione di fatture e Dichiarazione di Conformità. Non è cumulabile con il Conto Termico 3.0 sulla stessa spesa."),
        ("Quanto incide la posizione geografica sul rientro dell'investimento?",
         "Molto: lo stesso kWp produce circa 1.100 kWh/anno al Nord e fino a 1.500-1.600 al Sud. A parità di prezzo, un impianto in Sicilia si ripaga in 4-5 anni, uno in Lombardia in 6-8. L'orientamento a sud e l'assenza di ombreggiamenti pesano più della latitudine."),
    ],
    sources="Listini installatori rilevati a luglio 2026; GSE — report ritiro dedicato e statistiche fotovoltaico; ARERA — prezzi energia elettrica; ENEA — portale detrazioni fiscali. I prezzi sono medie di mercato: per il proprio caso richiedere sempre più preventivi analitici. Contenuto a scopo informativo.",
    tags=[
        ("/efficienza-energetica/", "Costo fotovoltaico"),
        ("/efficienza-energetica/", "Prezzi al kWp"),
        ("/incentivi-bonus/", "Detrazione 50%"),
        ("/efficienza-energetica/", "Tempi di rientro"),
    ],
    related=REL_COSTI, **MF,
),

# ───────────────────────────── 2. FOTOVOLTAICO INCENTIVI 2026 ─────────────────
dict(
    silo="efficienza-energetica", silo_name="Efficienza Energetica",
    slug="fotovoltaico-incentivi-2026",
    title_tag="Incentivi fotovoltaico 2026: guida completa",
    desc="Incentivi fotovoltaico 2026: detrazione 50% e 36%, Conto Termico 3.0, ritiro dedicato e comunità energetiche. Requisiti, cumuli e come fare domanda.",
    h1="Incentivi fotovoltaico 2026: detrazione 50%, comunità energetiche e ritiro dedicato",
    kicker="Efficienza Energetica · Incentivi 2026",
    standfirst="Detrazione del 50% sulla prima casa, Conto Termico 3.0 per gli interventi combinati, ritiro dedicato per l'energia immessa e la tariffa incentivante delle comunità energetiche: la mappa completa degli incentivi per il fotovoltaico nel 2026 e le regole per combinarli senza errori.",
    breadcrumb_title="Incentivi fotovoltaico 2026",
    pub="2026-07-15", pub_it="15 luglio 2026", mod="2026-07-15", mod_it="15 luglio 2026",
    read_min=8,
    thumb="t-energia", thumb_label="Efficienza Energetica · Incentivi 2026",
    thumb_aria="Copertura editoriale: incentivi fotovoltaico 2026",
    keywords="incentivi fotovoltaico 2026, detrazione 50% fotovoltaico, conto termico 3.0, comunità energetiche, ritiro dedicato GSE",
    og_title="Incentivi fotovoltaico 2026: detrazione 50%, comunità energetiche e ritiro dedicato",
    og_desc="Tutte le agevolazioni per il fotovoltaico nel 2026: chi può accedere, quanto valgono e quali si possono combinare.",
    tw_title="Incentivi fotovoltaico 2026: guida completa",
    tw_desc="Detrazione 50%, Conto Termico 3.0, ritiro dedicato e comunità energetiche: la mappa completa degli incentivi fotovoltaico 2026.",
    answer="Nel 2026 gli <strong>incentivi per il fotovoltaico</strong> residenziale sono tre: la detrazione fiscale del 50% sulla prima casa (36% sulle altre unità) con massimale di 96.000 euro, il Conto Termico 3.0 per gli interventi combinati e il ritiro dedicato GSE per l'energia immessa. Aderendo a una comunità energetica si aggiunge una tariffa incentivante ventennale sull'energia condivisa. Le agevolazioni non sono cumulabili sulla stessa spesa.",
    toc=[
        ("detrazione-50", "Come funziona la detrazione del 50% per il fotovoltaico?"),
        ("chi-puo-accedere", "Chi può accedere agli incentivi fotovoltaico 2026?"),
        ("conto-termico", "Conto Termico 3.0: quando conviene per il solare"),
        ("ritiro-dedicato", "Ritiro dedicato: quanto vale l'energia immessa in rete"),
        ("comunita-energetiche", "Comunità energetiche: come funzionano e quanto rendono"),
        ("cumulo", "Quali incentivi si possono combinare?"),
        ("come-fare-domanda", "Come fare domanda: iter e documenti"),
    ],
    body="""          <h2 id="detrazione-50">Come funziona la detrazione del 50% per il fotovoltaico?</h2>
          <p>Il canale principale tra gli <strong>incentivi fotovoltaico 2026</strong> è la detrazione per ristrutturazioni edilizie: <strong>50% sulla prima casa e 36% sulle altre unità immobiliari</strong>, con massimale di spesa di 96.000 euro e recupero in dieci rate annuali di pari importo. Rientrano nell'agevolazione l'intero impianto — moduli, inverter, struttura, manodopera, batteria di accumulo e oneri di connessione — a condizione che l'intervento sia installazione di un impianto «a servizio dell'edificio».</p>
          <p>Tre adempimenti fanno la differenza tra detrazione piena e contenzioso: il pagamento con <strong>bonifico parlante</strong> (bancario o postale, con causale, codice fiscale e riferimento normativo), la conservazione di fatture e Dichiarazione di Conformità dell'impianto elettrico e, per gli interventi che modificano la prospetto, la verifica del titolo edilizio — nella maggior parte dei casi il fotovoltaico resta edilizia libera secondo il Glossario unico. Tutti i dettagli operativi sono nella <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">guida al bonus ristrutturazione 2026</a>.</p>
          <p>La detrazione spetta a chi sostiene la spesa e possiede o detiene l'immobile: proprietari, nudi proprietari, usufruttuari, locatari e comodatari con consenso scritto del proprietario. Vale anche per gli impianti condominiali a servizio delle parti comuni, con ripartizione per millesimi.</p>

          <h2 id="chi-puo-accedere">Chi può accedere agli incentivi fotovoltaico 2026?</h2>
          <p>La platea è più ampia di quanto si pensi. Accedono alla detrazione del 50% i proprietari di prima casa e i familiari conviventi che sostengono le spese; accedono al 36% proprietari di seconde case, immobili locati e unità nel patrimonio. Per i condomini è sufficiente la delibera assembleare con la maggioranza semplice prevista per gli interventi sulle parti comuni, e ogni condomino detrae in quota millesimale.</p>
          <p>Le imprese e le partite IVA seguono un binario diverso: non usano il bonus ristrutturazioni ma ammortizzano l'impianto come bene strumentale, con la possibilità di credito d'imposta per gli investimenti in beni strumentali «green» quando ricompresi nei piani annuali. Per gli agricoli restano i bandi del PSN e del PNRR sul fotovoltaico in agricoltura, con dotazioni aggiornate a inizio 2026.</p>
          <p>Attenzione a un limite spesso ignorato: per i redditi oltre 75.000 euro si applica il meccanismo di rimodulazione delle detrazioni introdotto dalla riforma fiscale, con franchigie e massimali che riducono il beneficio effettivo. Chi ha redditi elevati dovrebbe simulare il risparmio reale prima di scegliere il canale agevolativo.</p>

          <h2 id="conto-termico">Conto Termico 3.0: quando conviene per il solare</h2>
          <p>Il <strong>Conto Termico 3.0</strong>, gestito dal GSE, è un incentivo diretto — non una detrazione — erogato in un'unica soluzione sotto i 15.000 euro o in rate annuali sopra questa soglia. Per il solare termico e gli interventi combinati (solare termico + pompa di calore, solare + sostituzione del generatore) copre quote rilevanti della spesa ammissibile, con tabelle di incentivo aggiornate al 2026.</p>
          <p>Il punto decisivo è la non cumulabilità: sulla stessa spesa si sceglie o la detrazione fiscale o il Conto Termico. In genere conviene la detrazione del 50% per il fotovoltaico puro, mentre il Conto Termico diventa interessante per chi non ha capienza fiscale (pensionati con redditi bassi, soggetti incapienti) o per gli interventi trainanti di efficienza come la <a href="/efficienza-energetica/pompe-di-calore-come-funzionano/">pompa di calore</a> e il <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico</a>, dove gli incentivi diretti sono particolarmente generosi. La procedura completa è nella <a href="/incentivi-bonus/conto-termico-3-guida/">guida al Conto Termico 3.0</a>.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="ritiro-dedicato">Ritiro dedicato: quanto vale l'energia immessa in rete</h2>
          <p>L'energia prodotta e non autoconsumata viene immessa in rete e valorizzata dal GSE con il <strong>ritiro dedicato</strong>: un prezzo zonale orario di mercato con minimi garantiti, che nel 2026 si aggira mediamente tra 8 e 11 centesimi al kWh secondo la fascia e la zona. Per un impianto da 6 kW che immette 2.500-3.000 kWh l'anno, il controvalore è di 200-330 euro annui, liquidati con conguaglio annuale.</p>
          <p>L'attivazione è semplice: dopo l'allaccio, l'installatore o il proprietario registra l'impianto sul portale GSE e stipula la convenzione di ritiro dedicato. Il pagamento delle eccedenze è soggetto a tassazione come reddito diverso, mentre i corrispettivi a copertura dei prelievi restano neutri. Chi non fa nulla perde semplicemente il contributo: l'energia immessa non valorizzata resta un regalo alla rete.</p>

          <h2 id="comunita-energetiche">Comunità energetiche: come funzionano e quanto rendono</h2>
          <p>Le <strong>comunità energetiche rinnovabili (CER)</strong> sono la novità strutturale del quadro 2026: gruppi di utenti — famiglie, imprese, enti pubblici — che condividono energia prodotta localmente da impianti rinnovabili. Sull'energia «condivisa» (prodotta e consumata nella stessa ora all'interno della comunità) il GSE riconosce una <strong>tariffa incentivante ventennale</strong>, articolata per taglia d'impianto, più il ristorno del corrispettivo tariffario sull'energia condivisa.</p>
          <p>In termini pratici, aderire a una CER può valere 5-9 centesimi in più per ogni kWh condiviso, cumulabili con il ritiro dedicato sull'energia immessa. Per un impianto domestico in una comunità ben bilanciata il beneficio annuo si aggira tra 150 e 400 euro, senza rinunciare alla detrazione del 50% sull'impianto: sono incentivi su grandezze diverse (spesa d'investimento la prima, energia condivisa la seconda) e per questo compatibili.</p>
          <p>Chi non ha un tetto disponibile può comunque partecipare come membro consumatore: è la strada per accedere ai benefici del solare in condominio, in affitto o con coperture vincolate. La mappa delle CER attive è pubblicata sul portale GSE, e molti Comuni mettono a disposizione sportelli di supporto alla costituzione.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="cumulo">Quali incentivi si possono combinare?</h2>
          <p>La regola d'oro è il <strong>principio di non cumulo</strong>: la stessa spesa non può essere agevolata due volte. All'interno di questa cornice, però, le combinazioni legittime sono più di quanto si creda:</p>
          <ul>
            <li><strong>Detrazione 50% sul fotovoltaico + Conto Termico sul solare termico</strong>: due interventi distinti dello stesso progetto, con computi e fatture separati.</li>
            <li><strong>Detrazione 50% + comunità energetica + ritiro dedicato</strong>: la detrazione premia l'investimento, la CER e il ritiro premiano l'energia; nessuna sovrapposizione.</li>
            <li><strong>Conto Termico su pompa di calore o cappotto + detrazione sul fotovoltaico</strong>: schema tipico delle riqualificazioni profonde, spesso il mix economicamente migliore.</li>
            <li><strong>IVA al 10%</strong> sulla fornitura con posa in opera: si cumula con tutti i canali perché è un'aliquota, non un incentivo.</li>
          </ul>
          <p>Ciò che non si può fare: detrarre al 50% e chiedere il Conto Termico sulla medesima fattura, oppure sommare due detrazioni sullo stesso intervento. Il GSE e l'AdE incrociano i dati di bonifici, fatture e pratiche ENEA: i recuperi con sanzioni sono ormai automatici.</p>

          <h2 id="come-fare-domanda">Come fare domanda: iter e documenti</h2>
          <p>Per la detrazione non serve alcuna domanda preventiva: bastano bonifico parlante, fatture e — dove richiesto — la pratica ENEA entro 90 giorni dalla fine dei lavori per gli interventi di riqualificazione energetica. Per il Conto Termico la domanda va presentata sul portale GSE entro 60 giorni dalla fine lavori (con la scheda descrittiva degli interventi) o tramite l'iter semplificato per gli apparecchi a catalogo.</p>
          <p>Per il ritiro dedicato e le CER l'iter è interamente online sul portale GSE, normalmente gestito dall'installatore o dal referente della comunità. Il consiglio pratico: far mettere nero su bianco nel contratto chi segue quale pratica, entro quando e con quali documenti. È il modo più semplice per non perdere incentivi per un adempimento dimenticato. E per il quadro completo dell'intervento, la nostra <a href="/efficienza-energetica/pannelli-solari-guida/">guida ai pannelli solari</a> ripercorre costi, tecnologie e installazione passo per passo, mentre l'articolo sui <a href="/efficienza-energetica/fotovoltaico-costi-2026/">costi del fotovoltaico 2026</a> dettaglia i prezzi per taglia.</p>""",
    faq_title="Domande frequenti sugli incentivi fotovoltaico 2026",
    faq=[
        ("Quali sono gli incentivi per il fotovoltaico nel 2026?",
         "Nel 2026 gli incentivi fotovoltaico principali sono: la <strong>detrazione del 50%</strong> sulla prima casa (36% sulle altre unità) con massimale di 96.000 euro, il Conto Termico 3.0 per gli interventi combinati, il ritiro dedicato GSE sull'energia immessa in rete e la tariffa incentivante ventennale delle comunità energetiche. Sulla stessa spesa le agevolazioni non si cumulano."),
        ("La detrazione del 50% vale anche per la batteria di accumulo?",
         "Sì: la batteria installata contestualmente o successivamente all'impianto rientra nella detrazione per ristrutturazioni (50% prima casa, 36% altre unità) entro il massimale di 96.000 euro. Servono bonifico parlante, fattura e Dichiarazione di Conformità dell'impianto elettrico."),
        ("Posso avere detrazione 50% e Conto Termico insieme?",
         "Non sulla stessa spesa. Si possono però combinare su interventi diversi dello stesso progetto: ad esempio detrazione del 50% sull'impianto fotovoltaico e Conto Termico 3.0 sul solare termico o sulla pompa di calore, tenendo computi e fatture rigorosamente separati."),
        ("Quanto rende aderire a una comunità energetica?",
         "Sull'energia condivisa nella stessa ora tra i membri, la CER riconosce una tariffa incentivante ventennale (in genere 5-9 centesimi/kWh secondo taglia) più il ristorno tariffario. Per un impianto domestico in una comunità ben bilanciata il beneficio tipico è di 150-400 euro l'anno, cumulabile con detrazione e ritiro dedicato."),
        ("Serve la pratica ENEA per il fotovoltaico?",
         "Dipende dalla qualificazione dell'intervento: se il fotovoltaico è installato come riqualificazione energetica con detrazione, la pratica ENEA va trasmessa entro 90 giorni dalla fine dei lavori. Se si usa il solo canale del ritiro dedicato o della CER senza detrazione, la pratica ENEA non è dovuta; restano gli adempimenti GSE."),
    ],
    sources="Agenzia delle Entrate — guide detrazioni 2026; GSE — regole applicative Conto Termico 3.0, ritiro dedicato e CER; ENEA — portale pratiche; ARERA — tariffa incentivante configurazioni. Normativa e aliquote aggiornate al 15 luglio 2026. Contenuto a scopo informativo: per il proprio caso consultare un professionista fiscale.",
    tags=[
        ("/efficienza-energetica/", "Incentivi fotovoltaico"),
        ("/incentivi-bonus/", "Detrazione 50%"),
        ("/efficienza-energetica/", "Comunità energetiche"),
        ("/incentivi-bonus/", "Conto Termico 3.0"),
    ],
    related=REL_INCENTIVI, **GS,
),

# ───────────────────────────── 3. POMPE DI CALORE ─────────────────────────────
dict(
    silo="efficienza-energetica", silo_name="Efficienza Energetica",
    slug="pompe-di-calore-come-funzionano",
    title_tag="Pompa di calore: come funziona e quando conviene",
    desc="Pompa di calore: come funziona il ciclo termodinamico, consumi reali in kWh, costi 2026 per aria-acqua e aria-aria, incentivi e quando conviene davvero.",
    h1="Pompa di calore: come funziona, consumi reali e quando conviene",
    kicker="Efficienza Energetica · Climatizzazione",
    standfirst="Un kWh elettrico per tre-quattro kWh termici: è il segreto della pompa di calore, la tecnologia che sta sostituendo le caldaie a gas nelle ristrutturazioni italiane. Come funziona, quanto consuma davvero, quanto costa nel 2026 e in quali case conviene installarla.",
    breadcrumb_title="Pompe di calore: come funzionano",
    pub="2026-07-10", pub_it="10 luglio 2026", mod="2026-07-10", mod_it="10 luglio 2026",
    read_min=9,
    thumb="t-energia", thumb_label="Efficienza Energetica · Climatizzazione",
    thumb_aria="Copertura editoriale: pompe di calore e climatizzazione efficiente",
    keywords="pompa di calore come funziona, consumi pompa di calore, pompa di calore aria acqua, costo pompa di calore 2026, COP pompa di calore",
    og_title="Pompa di calore: come funziona, consumi reali e quando conviene",
    og_desc="Ciclo termodinamico, COP, consumi reali in kWh, prezzi 2026 e incentivi: la guida pratica alla pompa di calore per la casa.",
    tw_title="Pompa di calore: come funziona e quando conviene",
    tw_desc="Come funziona una pompa di calore, consumi reali e costi 2026: quando conviene sostituire la caldaia a gas.",
    answer="Una <strong>pompa di calore</strong> funziona come un frigorifero al contrario: preleva calore dall'aria esterna, dall'acqua o dal terreno e lo «pompa» in casa usando un compressore elettrico. Con 1 kWh di elettricità produce 3-4 kWh termici (COP 3-4): per questo consuma il 50-65% in meno di una caldaia a gas. Conviene nelle case ben isolate, con riscaldamento a pavimento o radiatori sovradimensionati.",
    toc=[
        ("come-funziona", "Come funziona una pompa di calore?"),
        ("tipologie", "Aria-acqua, aria-aria e geotermiche: le tipologie"),
        ("cop-consumi", "Quanto consuma davvero una pompa di calore?"),
        ("costi-2026", "Quanto costa installarla nel 2026?"),
        ("quando-conviene", "Quando conviene (e quando no)?"),
        ("abbinamento-fotovoltaico", "L'abbinamento con il fotovoltaico"),
        ("incentivi-2026", "Quali incentivi si possono usare nel 2026?"),
    ],
    body="""          <h2 id="come-funziona">Come funziona una pompa di calore?</h2>
          <p>Capire <strong>come funziona una pompa di calore</strong> è più semplice di quanto suggerisca il nome: è lo stesso principio del frigorifero, applicato al contrario. Un circuito chiuso contiene un <strong>refrigerante</strong> che evapora a bassa temperatura assorbendo calore dalla sorgente esterna — aria, acqua di falda o terreno — viene compresso da un <strong>compressore elettrico</strong> salendo di temperatura, e cede il calore all'impianto di casa attraverso un condensatore. Il ciclo si ripete in continuo: espansione, evaporazione, compressione, condensazione.</p>
          <p>Il punto chiave è che la pompa di calore non «genera» calore bruciando qualcosa: lo <strong>sposta</strong> da fuori a dentro. L'unica energia pagata è quella elettrica del compressore e dei ventilatori, ed è per questo che con 1 kWh elettrico si ottengono 3-4 kWh termici. In estate il ciclo si inverte e la stessa macchina raffresca, cedendo calore all'esterno: riscaldamento, raffrescamento e — nei modelli aria-acqua — acqua calda sanitaria in un unico apparecchio.</p>
          <p>Le unità si dividono in <strong>monoblocco</strong> (tutto il ciclo nell'unità esterna, solo tubi dell'acqua verso casa, installazione più semplice) e <strong>split</strong> (unità esterna e idronica interna collegate da linee frigorifere, migliori prestazioni con climi rigidi). I refrigeranti di nuova generazione come l'R290 (propano) hanno resa elevata e impatto ambientale minimo, e nel 2026 dominano i listini delle case principali.</p>

          <h2 id="tipologie">Aria-acqua, aria-aria e geotermiche: le tipologie</h2>
          <p>La scelta della tipologia dipende da come la casa distribuisce il calore e da quanto spazio esterno è disponibile. Le tre famiglie principali a confronto:</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Le tipologie di pompa di calore a confronto (valori residenziali, 2026)</caption>
            <thead>
              <tr><th>Tipologia</th><th>Sorgente / emissione</th><th>COP medio stagionale</th><th>Costo installato</th><th>Ideale per</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Aria-acqua</strong></td><td>Aria esterna → acqua impianto</td><td>SCOP 3,5-4,5</td><td>8.000-15.000 €</td><td>Riscaldamento a pavimento, radiatori sovradimensionati, ACS</td></tr>
              <tr><td><strong>Aria-aria (split)</strong></td><td>Aria esterna → aria interna</td><td>SCOP 4-5</td><td>1.500-3.500 €/unità</td><td>Raffrescamento estivo, integrazione, case senza impianto idronico</td></tr>
              <tr><td><strong>Acqua-acqua / geotermica</strong></td><td>Falda o sonde → acqua impianto</td><td>SCOP 4,5-5,5</td><td>18.000-30.000 €</td><td>Nuove costruzioni, climi rigidi, grandi metrature</td></tr>
              <tr><td><strong>Ibrida (PdC + caldaia)</strong></td><td>Aria + gas a supporto</td><td>—</td><td>9.000-14.000 €</td><td>Case poco isolate, radiatori piccoli, zone fredde</td></tr>
            </tbody>
          </table>
          </div>
          <p>L'<strong>aria-acqua</strong> è la protagonista delle ristrutturazioni: alimenta l'impianto a pavimento o i radiatori esistenti e produce acqua calda sanitaria con un bollitore integrato. L'<strong>aria-aria</strong> — i comuni climatizzatori a split — è imbattibile per costo e semplicità nel raffrescamento, ma non scalda l'acqua sanitaria e nelle mezze stagioni va integrata. La <strong>geotermica</strong> ha le prestazioni migliori ma richiede sonde o captazione di falda: cantiere complesso, giustificato soprattutto nel nuovo.</p>

          <h2 id="cop-consumi">Quanto consuma davvero una pompa di calore?</h2>
          <p>Il consumo reale dipende dal <strong>COP</strong> (Coefficient of Performance) istantaneo e dallo <strong>SCOP</strong> stagionale, che tiene conto dell'intero inverno. Una buona aria-acqua del 2026 dichiara COP 4,5-5 a 7 °C esterni con mandata a 35 °C, che scende a 2,2-2,8 con -5 °C e mandata a 55 °C. La regola tecnica è semplice: <strong>più bassa è la temperatura di mandata, più alta è l'efficienza</strong> — per questo riscaldamento a pavimento (30-35 °C) e pompa di calore sono la coppia perfetta, mentre i radiatori piccoli che chiedono 65-70 °C la penalizzano.</p>
          <p>In numeri assoluti: una casa di 120 mq in classe E, riqualificata con <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">cappotto termico</a> fino alla classe B, ha un fabbisogno termico di circa 5.000-6.000 kWh l'anno. Con SCOP 3,8 la pompa di calore consuma <strong>1.300-1.600 kWh elettrici l'anno</strong> per il riscaldamento: ai prezzi elettrici del 2026 sono 350-500 euro, contro i 900-1.100 euro del gas per la stessa casa con caldaia a condensazione. Il risparmio tipico si attesta tra il 50 e il 65%.</p>
          <p>Due accorgimenti proteggono i consumi: il dimensionamento corretto (una macchina sovradimensionata pendola e degrada lo SCOP) e la gestione climatica con mandata scorrevole, che adatta la temperatura dell'acqua alle condizioni esterne invece di lavorare a punto fisso.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="costi-2026">Quanto costa installarla nel 2026?</h2>
          <p>Una pompa di calore aria-acqua da 6-9 kW per una villetta costa nel 2026 <strong>8.000-15.000 euro installata</strong>, inclusi unità esterna, modulo idronico, bollitore per ACS da 200-300 litri, collegamenti e pratiche. Le voci che fanno oscillare il prezzo sono la potenza, la presenza del bollitore, la distanza tra unità esterna e centrale termica e gli eventuali lavori elettrici (spesso serve portare il contatore a 6 kW e predisporre una linea dedicata).</p>
          <p>Più contenuto l'esborso per l'aria-aria: un dual split di qualità si installa con 2.500-4.000 euro. In cima alla scala le geotermiche, dove le sonde possono raddoppiare l'investimento. Per un quadro completo dei prezzi delle opere collegate — dal rifacimento impianti al massetto radiante — vale la nostra panoramica sul <a href="/ristrutturazioni/costo-ristrutturazione-al-mq-2026/">costo della ristrutturazione al mq nel 2026</a>.</p>

          <h2 id="quando-conviene">Quando conviene (e quando no)?</h2>
          <p>La pompa di calore conviene quando quattro condizioni si combinano: involucro isolato o in via di isolamento, terminali a bassa temperatura (pavimento radiante, fancoil o radiatori sovradimensionati), gas da sostituire o GPL/gasolio (dove il risparmio esplode) e disponibilità di spazio per l'unità esterna. Conviene moltissimo al posto del GPL e del gasolio, dove i tempi di rientro scendono sotto i 4 anni.</p>
          <p>Conviene meno in case poco isolate con radiatori piccoli e fabbisogni elevati: qui la macchina lavora a mandata alta, il COP crolla e il conto elettrico può superare quello del gas. In questi casi la sequenza corretta è <strong>prima l'involucro, poi il generatore</strong>: cappotto e serramenti riducono il fabbisogno, e solo dopo la pompa di calore lavora nel suo campo ideale. In attesa dell'intervento sull'involucro, una soluzione ibrida (pompa di calore + caldaia di backup) resta un compromesso onesto.</p>

          <h2 id="abbinamento-fotovoltaico">L'abbinamento con il fotovoltaico</h2>
          <p>La pompa di calore è il motivo per cui nel 2026 il fotovoltaico si dimensiona più grande: i 1.300-1.600 kWh annui di consumo elettrico della macchina si sommano ai consumi domestici, e un impianto da 6 kW diventa la taglia standard della riqualificazione. L'autoconsumo diretto è buono in estate (raffrescamento nelle ore di sole) e parziale in inverno, dove la produzione è bassa proprio quando la pompa consuma di più: anche così, la quota di fabbisogno coperta dal sole arriva al 30-40% annuo.</p>
          <p>Con la batteria e la gestione smart — la pompa che «carica» il massetto e il bollitore nelle ore di sole sfruttando l'inerzia termica — la copertura sale oltre il 50%. Per i prezzi dell'impianto solare rimandiamo all'analisi sui <a href="/efficienza-energetica/fotovoltaico-costi-2026/">costi del fotovoltaico 2026</a> e per il quadro tecnologico completo alla <a href="/efficienza-energetica/pannelli-solari-guida/">guida ai pannelli solari</a>.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="incentivi-2026">Quali incentivi si possono usare nel 2026?</h2>
          <p>La sostituzione del generatore con pompa di calore è un <strong>intervento trainante</strong> di riqualificazione energetica e accede a due canali alternativi: la <strong>detrazione del 50%</strong> (prima casa) o 36% (altre unità) con pratica ENEA obbligatoria entro 90 giorni, oppure il <strong>Conto Termico 3.0</strong> del GSE, incentivo diretto che per le pompe di calore raggiunge quote particolarmente rilevanti della spesa ammissibile, con erogazione rapida anche in un'unica soluzione. I dettagli sono nelle guide al <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">bonus ristrutturazione 2026</a> e al <a href="/incentivi-bonus/conto-termico-3-guida/">Conto Termico 3.0</a>.</p>
          <p>Il Conto Termico è spesso la scelta migliore per le pompe di calore: incentivo calcolato su tabelle che premiano la sostituzione di caldaie vecchie, nessuna attesa decennale e compatibilità con la detrazione su altri interventi dello stesso cantiere. Resta fermo il principio di non cumulo sulla stessa voce di spesa.</p>""",
    faq_title="Domande frequenti sulle pompe di calore",
    faq=[
        ("Come funziona una pompa di calore in parole semplici?",
         "Una pompa di calore funziona come un frigorifero al contrario: un refrigerante assorbe calore dall'aria esterna evaporando, un compressore elettrico ne alza la temperatura e il calore viene ceduto all'impianto di casa. Non brucia nulla: sposta calore, e per questo con 1 kWh elettrico produce 3-4 kWh termici."),
        ("Quanto consuma una pompa di calore al giorno in inverno?",
         "In una casa riqualificata di 120 mq, una pompa di calore consuma in media <strong>8-15 kWh elettrici al giorno</strong> nei mesi freddi, contro i 25-40 kWh termici equivalenti di una caldaia a gas. Il consumo reale dipende da isolamento, temperatura di mandata e clima: più bassa la mandata, minore il consumo."),
        ("La pompa di calore funziona con i radiatori esistenti?",
         "Sì, a una condizione: i radiatori devono essere sufficientemente grandi da scaldare con acqua a 45-50 °C invece che a 70 °C. Se i termosifoni sono piccoli rispetto al fabbisogno, servono più elementi, fancoil o una soluzione ibrida. La verifica si fa con un semplice calcolo termotecnico prima dell'acquisto."),
        ("Quanto costa una pompa di calore aria-acqua nel 2026?",
         "Nel 2026 una pompa di calore aria-acqua da 6-9 kW costa installata <strong>8.000-15.000 euro</strong>, bollitore per l'acqua calda sanitaria compreso. Con la detrazione del 50% o il Conto Termico 3.0 la spesa effettiva si riduce sensibilmente; con GPL o gasolio da sostituire il rientro scende sotto i 4 anni."),
        ("La pompa di calore conviene al Nord con climi rigidi?",
         "Sì, con le dovute scelte: i modelli di ultima generazione mantengono buone rese fino a -10/-15 °C, ma in zone molto fredde conviene una macchina leggermente sovradimensionata, mandata bassa e, nei casi limite, un'ibrida con caldaia di backup per i picchi. L'involucro isolato resta la condizione decisiva."),
    ],
    sources="Schede tecniche e listini dei principali produttori (2026); UNI/TS 11300 e banche dati ENEA sui fabbisogni; GSE — regole Conto Termico 3.0; ARERA — prezzi energia. I consumi indicati sono medie su casi reali: il dimensionamento va affidato a un termotecnico. Contenuto a scopo informativo.",
    tags=[
        ("/efficienza-energetica/", "Pompa di calore"),
        ("/efficienza-energetica/", "Consumi reali"),
        ("/impianti/", "Climatizzazione"),
        ("/incentivi-bonus/", "Conto Termico 3.0"),
    ],
    related=REL_POMPE, **MF,
),

# ───────────────────────────── 4. CAPPOTTO TERMICO ────────────────────────────
dict(
    silo="efficienza-energetica", silo_name="Efficienza Energetica",
    slug="cappotto-termico-esterno-guida",
    title_tag="Cappotto termico: costi al mq e detrazioni 2026",
    desc="Cappotto termico esterno: costi da 60 a 120 €/mq nel 2026, materiali a confronto (EPS, lana di roccia, sughero), fasi di cantiere e detrazioni.",
    h1="Cappotto termico esterno: materiali, costi al mq e detrazioni 2026",
    kicker="Efficienza Energetica · Involucro",
    standfirst="L'intervento che taglia il fabbisogno alla radice: il cappotto termico esterno riduce del 30-40% i consumi di riscaldamento e protegge la facciata per decenni. Materiali a confronto, prezzi al mq aggiornati al 2026, fasi di cantiere e detrazioni utilizzabili.",
    breadcrumb_title="Cappotto termico esterno",
    pub="2026-07-06", pub_it="6 luglio 2026", mod="2026-07-06", mod_it="6 luglio 2026",
    read_min=10,
    thumb="t-energia", thumb_label="Efficienza Energetica · Involucro",
    thumb_aria="Copertura editoriale: cappotto termico esterno e isolamento delle facciate",
    keywords="cappotto termico, costo cappotto termico al mq, cappotto esterno materiali, isolamento a cappotto, detrazioni cappotto 2026",
    og_title="Cappotto termico esterno: materiali, costi al mq e detrazioni 2026",
    og_desc="EPS, lana di roccia, sughero e fibra di legno a confronto, prezzi al mq nel 2026 e detrazioni: la guida completa al cappotto esterno.",
    tw_title="Cappotto termico: costi al mq e detrazioni 2026",
    tw_desc="Cappotto termico esterno: materiali a confronto, prezzi da 60 a 120 €/mq e detrazioni 2026.",
    answer="Il <strong>cappotto termico</strong> esterno costa nel 2026 tra 60 e 120 euro al mq posato, secondo materiale e spessore: l'EPS da 12-16 cm è la scelta più diffusa (60-85 €/mq), la lana di roccia e i materiali naturali costano di più. L'intervento riduce i consumi di riscaldamento del 30-40% e accede alla detrazione del 50% sulla prima casa o al Conto Termico 3.0.",
    toc=[
        ("cos-e", "Cos'è il cappotto termico esterno e perché funziona"),
        ("materiali", "Quali materiali scegliere per il cappotto?"),
        ("costi-al-mq", "Quanto costa il cappotto termico al mq nel 2026?"),
        ("quando-conviene", "Quando conviene il cappotto esterno?"),
        ("fasi-cantiere", "Come si realizza: le fasi di cantiere"),
        ("detrazioni-2026", "Quali detrazioni e incentivi nel 2026?"),
        ("errori-da-evitare", "Gli errori da evitare in progetto e in cantiere"),
    ],
    body="""          <h2 id="cos-e">Cos'è il cappotto termico esterno e perché funziona</h2>
          <p>Il <strong>cappotto termico</strong> esterno — tecnicamente ETICS, External Thermal Insulation Composite System — è un sistema a strati applicato sulla facciata: pannelli isolanti incollati e tassellati alla muratura, rasatura armata con rete in fibra di vetro e finitura a intonachino colorato. Avvolge l'edificio come un guscio continuo ed è l'unico intervento che risolve alla radice i <strong>ponti termici</strong> di pilastri, balconi e travi, responsabili da soli del 15-25% delle dispersioni di una casa non isolata.</p>
          <p>Perché funziona così bene: la muratura esistente resta all'interno del guscio isolato e diventa <strong>massa termica</strong>, accumulando calore d'inverno e frescura d'estate. Il risultato è una riduzione del fabbisogno di riscaldamento del 30-40% (fino al 50% sugli edifici anni '60-'80 non coibentati), pareti interne più calde di 3-4 °C — addio muffa da condensa superficiale — e una facciata rifatta che protegge la struttura dalle intemperie per 25-30 anni.</p>
          <p>Il cappotto è anche l'intervento che «prepara» la casa alla <a href="/efficienza-energetica/pompe-di-calore-come-funzionano/">pompa di calore</a>: riducendo il fabbisogno, permette al generatore di lavorare a bassa temperatura di mandata, dove il COP è massimo. Per questo nelle riqualificazioni serie la sequenza è sempre prima l'involucro, poi l'impianto, come ribadiamo nella <a href="/efficienza-energetica/pannelli-solari-guida/">guida ai pannelli solari</a> e alla riqualificazione integrata.</p>

          <h2 id="materiali">Quali materiali scegliere per il cappotto?</h2>
          <p>Il materiale incide su prezzo, comportamento al fuoco, traspirabilità e spessore necessario. Il confronto tra le quattro famiglie principali, per pareti in laterizio con obiettivo di trasmittanza U ≤ 0,28 W/mqK:</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Materiali per cappotto termico a confronto (valori medi, 2026)</caption>
            <thead>
              <tr><th>Materiale</th><th>Conducibilità λ (W/mK)</th><th>Spessore tipico</th><th>Costo al mq posato</th><th>Punti di forza</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>EPS (grafite)</strong></td><td>0,031-0,033</td><td>12-16 cm</td><td>60-85 €</td><td>Prezzo, leggerezza, posa rapida</td></tr>
              <tr><td><strong>Lana di roccia</strong></td><td>0,035-0,038</td><td>14-18 cm</td><td>85-110 €</td><td>Classe A1 al fuoco, acustica, traspirabilità</td></tr>
              <tr><td><strong>Sughero</strong></td><td>0,038-0,040</td><td>14-18 cm</td><td>100-130 €</td><td>Naturale, durevole, ottimo al caldo estivo</td></tr>
              <tr><td><strong>Fibra di legno</strong></td><td>0,038-0,042</td><td>14-18 cm</td><td>95-125 €</td><td>Sfasamento estivo, bioedilizia</td></tr>
              <tr><td><strong>Calcio silicato (interno)</strong></td><td>0,055-0,065</td><td>5-8 cm</td><td>90-120 €</td><td>Cappotto interno su facciate vincolate</td></tr>
            </tbody>
          </table>
          </div>
          <p>L'<strong>EPS con grafite</strong> copre oltre il 70% dei cantieri italiani: costa meno, pesa poco e con la grafite raggiunge prestazioni elevate a spessori contenuti. La <strong>lana di roccia</strong> è la scelta d'obbligo dove serve reazione al fuoco A1 (edifici alti, condomini) e premia in acustica. <strong>Sughero e fibra di legno</strong> giocano la carta dello sfasamento estivo — ritardano l'onda di calore di 10-12 ore contro le 6-8 dell'EPS — e della sostenibilità, a un prezzo superiore del 40-60%.</p>

          <h2 id="costi-al-mq">Quanto costa il cappotto termico al mq nel 2026?</h2>
          <p>Il prezzo chiavi in mano di un cappotto esterno nel 2026 si colloca tra <strong>60 e 120 euro al mq di facciata</strong>, ponteggio, materiali, posa e finitura compresi. La forchetta dipende da materiale e spessore, altezza dell'edificio, numero di aperture (davanzali, soglie e imbotti sono lavorazioni a parte) e stato del supporto. Su una villetta unifamiliare di 120 mq con 150-180 mq di facciata, il conto tipico è di <strong>12.000-18.000 euro</strong>; su un condominio di 4-6 piani la scala riduce il prezzo unitario del 10-15%.</p>
          <p>Le voci accessorie da mettere sempre a budget: ponteggio (8-14 €/mq, spesso compreso), adeguamento di davanzali e soglie, spostamento di gronde e pluviali, prolungamento di persiane e scuri, ripristino di cavi e antenne. Insieme valgono il 10-20% del totale e sono la prima causa di sorprese nei preventivi «a corpo». Per confrontare queste cifre con le altre voci di un cantiere completo, utile la nostra analisi del <a href="/ristrutturazioni/costo-ristrutturazione-al-mq-2026/">costo di ristrutturazione al mq nel 2026</a>.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="quando-conviene">Quando conviene il cappotto esterno?</h2>
          <p>Il cappotto conviene quando tre condizioni coincidono: edificio non isolato o con intercapedine inefficace, facciata comunque da rifare (l'intonaco a fine vita rende l'intervento quasi marginale rispetto al rifacimento semplice) e prospetto di permanenza nell'immobile di almeno 8-10 anni. Con la detrazione del 50%, il risparmio energetico del 30-40% e la rivalutazione dell'immobile — il salto di due classi APE vale il 5-10% del prezzo di vendita — il rientro si colloca tra 6 e 10 anni.</p>
          <p>Il cappotto esterno non si può fare — o conviene farlo interno — in tre casi: facciate vincolate dalla Soprintendenza (centri storici), spazi esterni insufficienti (marciapiedi stretti, confini a ridosso) e singoli appartamenti in condomini che non deliberano l'intervento comune. La soluzione è il <strong>cappotto interno</strong> in calcio silicato o pannelli accoppiati: ruba 5-8 cm per parete e costa di più a parità di prestazione, ma è realizzabile appartamento per appartamento e risolve comunque muffa e dispersioni sulle pareti perimetrali.</p>

          <h2 id="fasi-cantiere">Come si realizza: le fasi di cantiere</h2>
          <p>Un cantiere di cappotto su villetta dura 3-6 settimane e segue una sequenza rigorosa:</p>
          <ol>
            <li><strong>Progetto termotecnico</strong>: calcolo della trasmittanza, scelta di spessore e materiale, verifica dei nodi (davanzali, balconi, attacco a terra) e analisi del rischio condensa.</li>
            <li><strong>Preparazione del supporto</strong>: lavaggio, rimozione delle parti ammalorate, rasatura di fondo e verifica di aderenza con prove di strappo.</li>
            <li><strong>Posa dei pannelli</strong>: incollaggio a cordoli e punti, tassellatura (4-6 tasselli al mq secondo altezza e zona sismica), profili di partenza e angolari.</li>
            <li><strong>Rasatura armata</strong>: doppio strato di rasante con rete in fibra di vetro annegata, spessore complessivo 4-5 mm.</li>
            <li><strong>Finitura</strong>: primer e intonachino silossanico o siliconico, scelto anche per la resistenza ad alghe e piovaschi.</li>
          </ol>
          <p>I nodi critici decidono la durata dell'intervento: l'attacco a terra va protetto con profilo e fascia di zoccolatura, i davanzali sagomati con gocciolatoio, le soglie finestre isolate per non ricreare ponti termici. Un cappotto ben eseguito non richiede manutenzione straordinaria per 25-30 anni, salvo riverniciatura della finitura dopo 15-20 anni.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="detrazioni-2026">Quali detrazioni e incentivi nel 2026?</h2>
          <p>L'isolamento delle pareti opache è intervento trainante di riqualificazione energetica e nel 2026 accede a due canali alternativi: la <strong>detrazione del 50%</strong> sulla prima casa (36% sulle altre unità) con massimale autonomo per gli interventi sull'involucro e pratica ENEA entro 90 giorni dalla fine lavori, oppure il <strong>Conto Termico 3.0</strong>, che rimborsa direttamente quote rilevanti della spesa ammissibile con erogazione rapida. Le procedure complete sono nelle nostre guide al <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">bonus ristrutturazione 2026</a> e al <a href="/incentivi-bonus/conto-termico-3-guida/">Conto Termico 3.0</a>.</p>
          <p>In condominio la detrazione si ripartisce per millesimi e l'intervento può essere deliberato con la maggioranza prevista per le innovazioni dirette al miglioramento dell'efficienza energetica. Chi abbinasse nello stesso cantiere il fotovoltaico troverà il quadro completo nell'articolo sugli <a href="/efficienza-energetica/fotovoltaico-incentivi-2026/">incentivi fotovoltaico 2026</a>, ricordando che ogni voce di spesa segue il proprio canale senza doppie agevolazioni.</p>

          <h2 id="errori-da-evitare">Gli errori da evitare in progetto e in cantiere</h2>
          <ul>
            <li><strong>Spessore insufficiente</strong>: sotto i 10-12 cm nel Nord Italia il cappotto lavora male; il costo marginale dello spessore in più è minimo rispetto al beneficio.</li>
            <li><strong>Trascurare i nodi</strong>: davanzali, balconi e attacco a terra non isolati annullano metà del beneficio e generano condense localizzate.</li>
            <li><strong>Risparmiare sulla rasatura</strong>: rete di scarsa qualità o strato unico portano a fessurazioni della finitura entro pochi anni.</li>
            <li><strong>Non verificare il supporto</strong>: incollare su intonaci ammalorati senza ripristino compromette l'aderenza dell'intero sistema.</li>
            <li><strong>Affidarsi a posatori non certificati</strong>: i sistemi ETICS vanno posati secondo le linee guida ETAG/EAD; la certificazione del posatore è la prima garanzia reale.</li>
          </ul>""",
    faq_title="Domande frequenti sul cappotto termico",
    faq=[
        ("Quanto costa il cappotto termico esterno al mq nel 2026?",
         "Nel 2026 il cappotto termico esterno costa <strong>60-120 euro al mq posato</strong>, ponteggio e finitura compresi: 60-85 €/mq per l'EPS con grafite, 85-110 per la lana di roccia, 100-130 per sughero e fibra di legno. Su una villetta con 150-180 mq di facciata il conto tipico è di 12.000-18.000 euro."),
        ("Meglio cappotto esterno o interno?",
         "L'esterno è nettamente superiore: elimina i ponti termici, sfrutta la massa della muratura e protegge la facciata. L'interno si sceglie solo quando l'esterno è impossibile — facciate vincolate, spazi insufficienti, singoli appartamenti — accettando la perdita di 5-8 cm per parete e prestazioni leggermente inferiori."),
        ("Quanto dura un cappotto termico ben fatto?",
         "Un sistema ETICS posato a regola d'arte dura <strong>25-30 anni</strong> senza manutenzione straordinaria. La finitura a intonachino può richiedere una riverniciatura dopo 15-20 anni. La durata dipende soprattutto dalla qualità della rasatura armata e dal trattamento dei nodi critici come attacco a terra e davanzali."),
        ("Il cappotto termico rientra nel bonus ristrutturazione 2026?",
         "Sì: l'isolamento delle pareti opache è intervento trainante e accede alla <strong>detrazione del 50%</strong> sulla prima casa (36% sulle altre unità) con pratica ENEA obbligatoria, oppure al Conto Termico 3.0 con rimborso diretto. I due canali non sono cumulabili sulla stessa spesa."),
        ("Serve il permesso del Comune per fare il cappotto?",
         "Dipende dai casi: il cappotto che non altera forme e colori può rientrare in attività semplificata, ma l'aumento di spessore della parete e la modifica del prospetto richiedono in genere una CILA o una SCIA secondo il contesto, oltre al parere della Soprintendenza nelle zone vincolate. La verifica preventiva con un tecnico evita fermi cantiere."),
    ],
    sources="Listini sistemi ETICS e associazioni di categoria (2026); Cortexa — guide tecniche; ENEA — requisiti detrazioni involucro; GSE — Conto Termico 3.0. I prezzi sono medie nazionali: per il proprio edificio serve un preventivo su sopralluogo. Contenuto a scopo informativo.",
    tags=[
        ("/efficienza-energetica/", "Cappotto termico"),
        ("/efficienza-energetica/", "Isolamento pareti"),
        ("/materiali-costruzione/", "Materiali isolanti"),
        ("/incentivi-bonus/", "Detrazioni 2026"),
    ],
    related=REL_CAPPOTTO, **LB,
),
]
