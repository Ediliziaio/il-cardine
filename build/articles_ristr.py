# -*- coding: utf-8 -*-
"""Contenuti articoli silo ristrutturazioni (4 articoli)."""

COSTO_MQ = "/ristrutturazioni/costo-ristrutturazione-al-mq-2026/"
CHIAVI = "/ristrutturazioni/ristrutturazione-chiavi-in-mano/"
BAGNO = "/ristrutturazioni/ristrutturare-bagno-costi-tempi/"
PERMESSI = "/ristrutturazioni/ristrutturare-casa-permessi-cila-scia/"
BONUS_RIST = "/incentivi-bonus/bonus-ristrutturazione-2026-guida/"
IDRAULICO = "/impianti/rifacimento-impianto-idraulico-costi/"
CASE_GREEN = "/normative/direttiva-case-green-cosa-cambia/"

ER = dict(
    author="Elena Riva", initials="ER",
    role="Redazione Il Cardine · Ristrutturazioni",
    bio="Giornalista edile, segue cantieri, contratti e mercato delle ristrutturazioni da oltre dieci anni. Per Il Cardine scrive guide su costi, computi metrici e rapporto tra committenti e imprese.",
)
PG = dict(
    author="Paolo Gatti", initials="PG",
    role="Redazione Il Cardine · Impianti e bagni",
    bio="Tecnico impiantista e giornalista, cura per Il Cardine i contenuti su impianti idraulici ed elettrici, bagni e finiture, con un occhio ai costi reali di cantiere.",
)
SC = dict(
    author="Sara Colombo", initials="SC",
    role="Redazione Il Cardine · Normative e iter edilizi",
    bio="Architetto e giornalista tecnica, si occupa di normativa edilizia, titoli abilitativi e pratiche comunali. Per Il Cardine spiega permessi, CILA, SCIA e adempimenti per ristrutturare in regola.",
)

REL_COSTO_MQ = [
    dict(href=CHIAVI, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Ristrutturazione chiavi in mano: come funziona, costi e garanzie",
         excerpt="Un solo interlocutore dal progetto alla consegna: vantaggi, costi e tutele.",
         date="12 lug 2026", mins="8 min"),
    dict(href=BAGNO, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Ristrutturare il bagno nel 2026: costi, tempi e errori da evitare",
         excerpt="Quanto costa rifare il bagno, quanto dura e gli errori che fanno lievitare il conto.",
         date="8 lug 2026", mins="8 min"),
    dict(href=PERMESSI, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Ristrutturare casa: quali permessi servono tra CILA, SCIA e titolo edilizio",
         excerpt="Edilizia libera, CILA e SCIA: quale titolo serve per ogni tipo di lavoro.",
         date="2 lug 2026", mins="8 min"),
]
REL_CHIAVI = [
    dict(href=COSTO_MQ, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Costo ristrutturazione al mq nel 2026: prezzi voce per voce",
         excerpt="Il listino reale dei lavori: demolizioni, impianti, pavimenti e finiture al mq.",
         date="19 lug 2026", mins="9 min"),
    dict(href=BAGNO, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Ristrutturare il bagno nel 2026: costi, tempi e errori da evitare",
         excerpt="Quanto costa rifare il bagno, quanto dura e gli errori che fanno lievitare il conto.",
         date="8 lug 2026", mins="8 min"),
    dict(href=PERMESSI, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Ristrutturare casa: quali permessi servono tra CILA, SCIA e titolo edilizio",
         excerpt="Edilizia libera, CILA e SCIA: quale titolo serve per ogni tipo di lavoro.",
         date="2 lug 2026", mins="8 min"),
]
REL_BAGNO = [
    dict(href=COSTO_MQ, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Costo ristrutturazione al mq nel 2026: prezzi voce per voce",
         excerpt="Il listino reale dei lavori: demolizioni, impianti, pavimenti e finiture al mq.",
         date="19 lug 2026", mins="9 min"),
    dict(href=CHIAVI, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Ristrutturazione chiavi in mano: come funziona, costi e garanzie",
         excerpt="Un solo interlocutore dal progetto alla consegna: vantaggi, costi e tutele.",
         date="12 lug 2026", mins="8 min"),
    dict(href=PERMESSI, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Ristrutturare casa: quali permessi servono tra CILA, SCIA e titolo edilizio",
         excerpt="Edilizia libera, CILA e SCIA: quale titolo serve per ogni tipo di lavoro.",
         date="2 lug 2026", mins="8 min"),
]
REL_PERMESSI = [
    dict(href=COSTO_MQ, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Costo ristrutturazione al mq nel 2026: prezzi voce per voce",
         excerpt="Il listino reale dei lavori: demolizioni, impianti, pavimenti e finiture al mq.",
         date="19 lug 2026", mins="9 min"),
    dict(href=CHIAVI, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Ristrutturazione chiavi in mano: come funziona, costi e garanzie",
         excerpt="Un solo interlocutore dal progetto alla consegna: vantaggi, costi e tutele.",
         date="12 lug 2026", mins="8 min"),
    dict(href=BAGNO, thumb="t-ristrutturazioni", cat="Ristrutturazioni",
         title="Ristrutturare il bagno nel 2026: costi, tempi e errori da evitare",
         excerpt="Quanto costa rifare il bagno, quanto dura e gli errori che fanno lievitare il conto.",
         date="8 lug 2026", mins="8 min"),
]

ARTICOLI_RISTR = [

# ───────────────────── 5. COSTO RISTRUTTURAZIONE AL MQ 2026 ───────────────────
dict(
    silo="ristrutturazioni", silo_name="Ristrutturazioni",
    slug="costo-ristrutturazione-al-mq-2026",
    title_tag="Costo ristrutturazione al mq 2026: prezzi reali",
    desc="Costo ristrutturazione al mq nel 2026: da 700 a 1.600 €/mq secondo il livello. Prezzi voce per voce: demolizioni, impianti, pavimenti, bagno e cucina.",
    h1="Costo ristrutturazione al mq nel 2026: prezzi voce per voce",
    kicker="Ristrutturazioni · Prezzi 2026",
    standfirst="Da 700 €/mq per una ristrutturazione economica a oltre 1.600 €/mq per il livello alto: il listino reale dei lavori nel 2026, scomposto voce per voce — demolizioni, impianti, pavimenti, bagno e cucina — con i fattori che fanno lievitare o contenere il conto finale.",
    breadcrumb_title="Costo ristrutturazione al mq 2026",
    pub="2026-07-19", pub_it="19 luglio 2026", mod="2026-07-19", mod_it="19 luglio 2026",
    read_min=9,
    thumb="t-ristrutturazioni", thumb_label="Ristrutturazioni · Prezzi 2026",
    thumb_aria="Copertura editoriale: costi di ristrutturazione al mq nel 2026",
    keywords="costo ristrutturazione al mq, prezzi ristrutturazione 2026, costo ristrutturare casa, preventivo ristrutturazione, costo ristrutturazione completa",
    og_title="Costo ristrutturazione al mq nel 2026: prezzi voce per voce",
    og_desc="Il listino reale 2026: da 700 a 1.600 €/mq secondo il livello, con il dettaglio di demolizioni, impianti, pavimenti, bagno e cucina.",
    tw_title="Costo ristrutturazione al mq 2026: prezzi reali",
    tw_desc="Ristrutturare casa nel 2026 costa 700-1.600 €/mq: il dettaglio voce per voce e i fattori che muovono il prezzo.",
    answer="Nel 2026 il <strong>costo di una ristrutturazione al mq</strong> va da 700-900 euro per un livello economico a 1.000-1.300 euro per il medio e oltre 1.600 euro per l'alto, impianti e finiture compresi. Per un appartamento di 100 mq la ristrutturazione completa di medio livello costa 100.000-130.000 euro, dimezzabili al 50% con il bonus ristrutturazione in dieci anni.",
    toc=[
        ("prezzi-al-mq", "Quanto costa ristrutturare al mq nel 2026?"),
        ("voci-di-costo", "Le voci di costo, voce per voce"),
        ("fattori-di-prezzo", "Cosa fa variare il prezzo al mq?"),
        ("costi-per-ambiente", "Quanto costano bagno e cucina?"),
        ("costi-nascosti", "I costi nascosti da mettere a budget"),
        ("come-risparmiare", "Come contenere la spesa senza rinunce"),
        ("bonus-2026", "Quali bonus riducono il costo nel 2026?"),
    ],
    body="""          <h2 id="prezzi-al-mq">Quanto costa ristrutturare al mq nel 2026?</h2>
          <p>Il <strong>costo di una ristrutturazione al mq</strong> nel 2026 dipende dal livello di finiture e dalla profondità dell'intervento, ma tre fasce di riferimento ordinano il mercato italiano: <strong>700-900 €/mq</strong> per la ristrutturazione economica (impianti a norma, finiture di fascia base), <strong>1.000-1.300 €/mq</strong> per il livello medio, il più richiesto, e <strong>1.400-1.800 €/mq</strong> per l'alto di gamma con materiali pregiati, domotica e progettazione su misura.</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Costo ristrutturazione completa al mq per livello (Italia, 2026)</caption>
            <thead>
              <tr><th>Livello</th><th>Prezzo al mq</th><th>Appartamento 100 mq</th><th>Cosa comprende</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Economico</strong></td><td>700-900 €</td><td>70.000-90.000 €</td><td>Impianti a norma, pavimenti gres base, sanitari standard, tinteggiatura</td></tr>
              <tr><td><strong>Medio</strong></td><td>1.000-1.300 €</td><td>100.000-130.000 €</td><td>Gres di qualità o parquet prefinito, sanitari di marca, cartongessi, clima</td></tr>
              <tr><td><strong>Alto</strong></td><td>1.400-1.800 €</td><td>140.000-180.000 €</td><td>Materiali pregiati, domotica, radiante, serramenti alte prestazioni, interior design</td></tr>
            </tbody>
          </table>
          </div>
          <p>Questi valori si riferiscono alla ristrutturazione completa «a corpo» e includono manodopera e materiali di posa, ma non arredi, pratiche edilizie complesse e opere strutturali. Per un singolo appartamento in città il prezzo tende verso il limite alto della fascia (logistica e ponteggi pesano di più), mentre su più unità o villette la scala aiuta. Chi preferisce un unico interlocutore può valutare la <a href="/ristrutturazioni/ristrutturazione-chiavi-in-mano/">ristrutturazione chiavi in mano</a>, che incorpora progettazione e gestione a un sovrapprezzo tipico del 10-15%.</p>

          <h2 id="voci-di-costo">Le voci di costo, voce per voce</h2>
          <p>La scomposizione del prezzo al mq è il modo migliore per leggere un preventivo. Ecco le voci tipiche di una ristrutturazione completa di livello medio, con i valori 2026:</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 2 — Listino indicativo delle lavorazioni (livello medio, IVA esclusa, 2026)</caption>
            <thead>
              <tr><th>Voce di lavorazione</th><th>Prezzo indicativo</th><th>Unità</th><th>Note</th></tr>
            </thead>
            <tbody>
              <tr><td>Demolizioni e smaltimento</td><td>25-45 €</td><td>al mq di pavimento</td><td>Include trasporto in discarica autorizzata</td></tr>
              <tr><td>Rifacimento impianto elettrico</td><td>60-90 €</td><td>al punto luce</td><td>Quadro, DiCo e prese comprese nel computo tipo</td></tr>
              <tr><td>Rifacimento impianto idraulico</td><td>180-280 €</td><td>al punto acqua</td><td>Multistrato o PPR, scarichi inclusi</td></tr>
              <tr><td>Pavimenti in gres, posa compresa</td><td>55-110 €</td><td>al mq</td><td>Materiale 20-60 €/mq, posa 30-45 €/mq</td></tr>
              <tr><td>Parquet prefinito, posa compresa</td><td>90-160 €</td><td>al mq</td><td>Rovere due/tre strati</td></tr>
              <tr><td>Massetto e sottofondi</td><td>25-40 €</td><td>al mq</td><td>Tradizionale o alleggerito</td></tr>
              <tr><td>Controsoffitti e cartongessi</td><td>45-75 €</td><td>al mq</td><td>Lastre standard o idrorepellenti</td></tr>
              <tr><td>Tinteggiatura</td><td>12-20 €</td><td>al mq di parete</td><td>Due mani, idropittura lavabile</td></tr>
              <tr><td>Porte interne</td><td>350-700 €</td><td>a porta</td><td>Laminate o laccate, posa compresa</td></tr>
              <tr><td>Bagno completo (5-6 mq)</td><td>8.000-15.000 €</td><td>a corpo</td><td>Demolizione, impianti, rivestimenti, sanitari</td></tr>
            </tbody>
          </table>
          </div>
          <p>Le due voci che pesano di più sul totale sono gli <strong>impianti</strong> (20-30% del budget) e le <strong>finiture</strong> (pavimenti, rivestimenti, porte, sanitari: 30-40%). Il dettaglio sull'impianto idraulico — materiali, prezzi al punto acqua e tempi — è nella nostra guida al <a href="/impianti/rifacimento-impianto-idraulico-costi/">rifacimento dell'impianto idraulico e ai suoi costi</a>.</p>

          <h2 id="fattori-di-prezzo">Cosa fa variare il prezzo al mq?</h2>
          <p>Cinque fattori spiegano perché due appartamenti identici possono costare cifre molto diverse. Il primo è lo <strong>stato di partenza</strong>: umidità di risalita, impianti in piombo o alluminio, solai da consolidare fanno lievitare il conto anche del 30%. Il secondo è la <strong>logistica</strong>: piano alto senza ascensore, centro storico, ponteggio su strada pubblica aggiungono voci che in periferia non esistono. Il terzo è la <strong>geografia</strong>: a parità di lavorazioni, Milano e Roma costano il 15-25% in più della media nazionale, il Sud il 10-15% in meno.</p>
          <p>Il quarto fattore è la <strong>distribuzione interna</strong>: spostare il bagno o la cucina significa rifare scarichi e adduzioni con pendenze da rispettare, e può richiedere la sanatoria della planimetria catastale. Il quinto è la <strong>stagionalità</strong>: i cantieri avviati tra autunno e inverno trovano imprese più disponibili e prezzi più morbidi rispetto alla corsa primaverile.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="costi-per-ambiente">Quanto costano bagno e cucina?</h2>
          <p>Bagno e cucina concentrano il 40-50% del budget perché sommano impianti, rivestimenti e apparecchi. Un <strong>bagno di 5-6 mq</strong> rifatto da zero costa 8.000-15.000 euro: demolizione e smaltimento (800-1.200 €), impianti idrico e scarichi (1.800-3.000 €), massetto e impermeabilizzazione (600-1.000 €), rivestimenti e pavimento (1.500-3.000 €), sanitari e rubinetteria (1.200-3.000 €), box doccia o vasca (600-2.000 €). Il dettaglio completo è nella guida <a href="/ristrutturazioni/ristrutturare-bagno-costi-tempi/">ristrutturare il bagno: costi, tempi ed errori da evitare</a>.</p>
          <p>La <strong>cucina</strong> come ambiente tecnico (impianti, pavimenti, rivestimenti, predisposizioni) costa 4.000-8.000 euro esclusi i mobili; la cucina componibile aggiunge da 3.000 euro per le catene di largo consumo a 15.000-30.000 euro per le marche di fascia alta, elettrodomestici inclusi o meno secondo l'offerta.</p>

          <h2 id="costi-nascosti">I costi nascosti da mettere a budget</h2>
          <p>La regola prudente è aggiungere un <strong>fondo imprevisti del 10-15%</strong> al preventivo. Le voci più dimenticate: oneri di urbanizzazione e diritti di segreteria per le pratiche (da poche decine a oltre mille euro secondo il Comune), aggiornamento catastale dopo la variazione della planimetria, Dichiarazione di Conformità degli impianti, certificazione APE pre e post intervento, eventuale perizia per crepe o consolidamenti scoperti in demolizione, allaccio provvisorio e pulizie finali di cantiere.</p>
          <p>Attenzione anche alla voce «esclusi» dei preventivi: smaltimento macerie, ponteggio, trasporti e utenze di cantiere sono spesso fuori prezzo e valgono complessivamente il 5-8% del totale. Chiedere sempre il computo analitico con inclusi ed esclusi scritti nero su bianco, e verificare quali <a href="/ristrutturazioni/ristrutturare-casa-permessi-cila-scia/">permessi servono per ristrutturare casa</a> prima di firmare: un cantiere fermo per pratica mancante costa più della pratica stessa.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="come-risparmiare">Come contenere la spesa senza rinunce</h2>
          <ol>
            <li><strong>Progetto prima del preventivo</strong>: un capitolato dettagliato elimina le varianti in corso d'opera, la prima causa di sforamento.</li>
            <li><strong>Tre preventivi comparabili</strong>: stesse voci, stesse quantità, stesse esclusioni; differenze del 20-25% tra imprese sono normali.</li>
            <li><strong>Mantenere la distribuzione</strong>: non spostare bagno e cucina fa risparmiare 5.000-15.000 euro tra impianti e pratiche.</li>
            <li><strong>Sovrapporre invece di demolire</strong>: dove possibile, pavimenti in resina o LVT su esistente riducono demolizioni e smaltimento.</li>
            <li><strong>Materiali di fascia media su misura solo dove conta</strong>: la qualità si sente su rubinetteria, sanitari e porte; meno su massetti e intonaci.</li>
            <li><strong>Cantiere d'inverno</strong>: tra novembre e febbraio le imprese praticano sconti del 5-10% per riempire il calendario.</li>
          </ol>

          <h2 id="bonus-2026">Quali bonus riducono il costo nel 2026?</h2>
          <p>La leva decisiva è il <strong>bonus ristrutturazione</strong>: detrazione del 50% sulla prima casa e del 36% sulle altre unità, massimale 96.000 euro, recupero in dieci rate. Copre quasi tutte le voci della ristrutturazione — demolizioni, impianti, pavimenti, bagni, serramenti — esclusi gli arredi. Su un cantiere da 100.000 euro sulla prima casa il beneficio vale 50.000 euro di risparmio fiscale: il costo netto effettivo scende a 500-650 €/mq per il livello medio. I requisiti, i documenti e gli adempimenti sono nella <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">guida al bonus ristrutturazione 2026</a>.</p>
          <p>Si aggiungono l'IVA agevolata al 10% sulle prestazioni di manutenzione ordinaria e straordinaria (e sulle forniture con posa entro i limiti del valore significativo), l'ecobonus per gli interventi energetici specifici e il bonus mobili per l'arredo contestuale. La spinta verso l'efficientamento è rafforzata dalla <a href="/normative/direttiva-case-green-cosa-cambia/">direttiva Case Green</a>, che rende la riqualificazione del patrimonio esistente una traiettoria obbligata: ristrutturare bene oggi significa anche mettere l'immobile in regola con il domani.</p>""",
    faq_title="Domande frequenti sul costo di ristrutturazione al mq",
    faq=[
        ("Qual è il costo di ristrutturazione al mq di un appartamento nel 2026?",
         "Nel 2026 il costo di ristrutturazione al mq per un intervento completo è di <strong>700-900 euro per il livello economico, 1.000-1.300 per il medio e 1.400-1.800 per l'alto</strong>. Un appartamento di 100 mq ristrutturato a livello medio costa 100.000-130.000 euro, impianti e finiture compresi, arredi esclusi."),
        ("Quanto costa ristrutturare solo gli impianti?",
         "Il rifacimento di impianto elettrico e idraulico insieme costa indicativamente <strong>250-400 euro al mq</strong> di appartamento, compresi tracce, ripristini e Dichiarazioni di Conformità. Per un 100 mq si parla di 25.000-40.000 euro: è la voce che non si può risparmiare perché riguarda sicurezza e conformità."),
        ("Il bonus ristrutturazione copre tutti i lavori?",
         "Copre quasi tutte le lavorazioni edili e impiantistiche — demolizioni, murature, impianti, pavimenti, bagni, serramenti, tinteggiatura — con detrazione del 50% sulla prima casa e 36% sulle altre unità entro 96.000 euro. Restano esclusi arredi ed elettrodomestici, che seguono il bonus mobili quando applicabile."),
        ("Perché i preventivi per lo stesso appartamento sono così diversi?",
         "Perché spesso non sono comparabili: esclusioni diverse (smaltimento, ponteggio, trasporti), quantità stimate in modo differente, materiali di fascia diversa e margini diversi. La soluzione è un capitolato unico su cui far offrire tutte le imprese, con voci, quantità ed esclusi scritti."),
        ("Conviene ristrutturare tutto insieme o per step?",
         "Tutto insieme costa meno: un solo ponteggio, una sola direzione lavori, un solo smaltimento e il massimale del bonus sfruttato al meglio. Ristrutturare per step conviene solo per ragioni di budget o di abitabilità, accettando un sovrapprezzo complessivo del 10-20% e il rischio di rifare ripristini già fatti."),
    ],
    sources="Osservatorio prezzi ristrutturazioni e listini di categoria (luglio 2026); prezziari regionali delle opere edili; Agenzia delle Entrate — guida bonus ristrutturazione 2026. I valori sono medie nazionali: il preventivo reale richiede sopralluogo e computo metrico. Contenuto a scopo informativo.",
    tags=[
        ("/ristrutturazioni/", "Costo ristrutturazione"),
        ("/ristrutturazioni/", "Prezzi al mq"),
        ("/incentivi-bonus/", "Bonus ristrutturazione"),
        ("/ristrutturazioni/", "Preventivi"),
    ],
    related=REL_COSTO_MQ, **ER,
),

# ───────────────────── 6. RISTRUTTURAZIONE CHIAVI IN MANO ─────────────────────
dict(
    silo="ristrutturazioni", silo_name="Ristrutturazioni",
    slug="ristrutturazione-chiavi-in-mano",
    title_tag="Ristrutturazione chiavi in mano: costi e garanzie",
    desc="Ristrutturazione chiavi in mano: come funziona il contratto, quanto costa in più rispetto alle imprese separate, garanzie e clausole da pretendere.",
    h1="Ristrutturazione chiavi in mano: come funziona, costi e garanzie",
    kicker="Ristrutturazioni · Contratti",
    standfirst="Un unico interlocutore che consegna la casa finita, dal progetto alle pulizie finali: la ristrutturazione chiavi in mano semplifica la vita del committente ma va capita bene. Come funziona il contratto, quanto costa in più, quali garanzie pretendere e quando conviene davvero.",
    breadcrumb_title="Ristrutturazione chiavi in mano",
    pub="2026-07-12", pub_it="12 luglio 2026", mod="2026-07-12", mod_it="12 luglio 2026",
    read_min=8,
    thumb="t-ristrutturazioni", thumb_label="Ristrutturazioni · Contratti",
    thumb_aria="Copertura editoriale: ristrutturazione chiavi in mano",
    keywords="ristrutturazione chiavi in mano, costo chiavi in mano, contratto ristrutturazione, general contractor ristrutturazione, garanzie ristrutturazione",
    og_title="Ristrutturazione chiavi in mano: come funziona, costi e garanzie",
    og_desc="Dal progetto alla consegna con un solo interlocutore: costi, garanzie, clausole del contratto e quando conviene.",
    tw_title="Ristrutturazione chiavi in mano: costi e garanzie",
    tw_desc="Come funziona la ristrutturazione chiavi in mano: sovrapprezzo del 10-15%, garanzie da pretendere e clausole del contratto.",
    answer="La <strong>ristrutturazione chiavi in mano</strong> affida a un unico soggetto — impresa generalista o general contractor — progetto, pratiche, lavori e consegna della casa finita. Costa il 10-15% in più della gestione a imprese separate ma offre un solo responsabile, tempi contrattualizzati e garanzie uniche. La tutela decisiva è un contratto con capitolato, cronoprogramma e penali.",
    toc=[
        ("cos-e", "Cos'è la ristrutturazione chiavi in mano"),
        ("come-funziona", "Come funziona, passo per passo"),
        ("quanto-costa", "Quanto costa rispetto alle imprese separate?"),
        ("garanzie", "Quali garanzie e tutele offre?"),
        ("contratto", "Cosa deve contenere il contratto"),
        ("pro-contro", "Vantaggi e limiti: il bilancio onesto"),
        ("come-scegliere", "Come scegliere l'impresa giusta"),
    ],
    body="""          <h2 id="cos-e">Cos'è la ristrutturazione chiavi in mano</h2>
          <p>La <strong>ristrutturazione chiavi in mano</strong> è una formula contrattuale in cui il committente firma con un unico soggetto — impresa generalista strutturata o general contractor — che si assume la responsabilità dell'intero intervento: rilievo e progetto, pratiche edilizie e catastali, coordinamento delle maestranze, forniture, direzione lavori e consegna della casa «finita», pronta da abitare. Il nome dice tutto: il cliente riceve le chiavi e rientra.</p>
          <p>Il modello nasce come risposta alla frammentazione del cantiere tradizionale, dove il committente coordina di persona muratore, idraulico, elettricista e pittore, con rimpalli di responsabilità a ogni imprevisto. Nel chiavi in mano la catena è unica: se qualcosa non funziona, c'è un solo interlocutore e un solo responsabile contrattuale. È la differenza sostanziale rispetto all'appalto a imprese separate, e la ragione per cui questa formula cresce a doppia cifra nel residenziale italiano dal 2023.</p>

          <h2 id="come-funziona">Come funziona, passo per passo</h2>
          <p>L'iter tipo di una ristrutturazione chiavi in mano si sviluppa in sei fasi:</p>
          <ol>
            <li><strong>Sopralluogo e briefing</strong>: rilievo dell'immobile, raccolta delle esigenze, budget indicativo e tempi attesi.</li>
            <li><strong>Progetto preliminare e capitolato</strong>: distribuzione degli spazi, scelta dei materiali entro «fasce di fornitura» definite, computo analitico voce per voce.</li>
            <li><strong>Contratto e cronoprogramma</strong>: prezzo a corpo o a misura, stati di avanzamento, penali per ritardo, garanzie.</li>
            <li><strong>Pratiche</strong>: l'impresa presenta CILA o SCIA a suo nome tecnico, gestisce gli adempimenti per le detrazioni e coordina la direzione lavori. Su quale titolo serva per ogni tipo di lavoro rimandiamo alla guida sui <a href="/ristrutturazioni/ristrutturare-casa-permessi-cila-scia/">permessi per ristrutturare casa tra CILA e SCIA</a>.</li>
            <li><strong>Cantiere</strong>: le maestranze sono coordinate dall'impresa; il committente ha un referente unico e verbali di avanzamento periodici.</li>
            <li><strong>Consegna</strong>: collaudo, certificazioni (DiCo impianti, APE), documentazione per le detrazioni e verbale di consegna con eventuale lista di «punch list» da chiudere.</li>
          </ol>

          <h2 id="quanto-costa">Quanto costa rispetto alle imprese separate?</h2>
          <p>Il chiavi in mano costa in media il <strong>10-15% in più</strong> della somma delle singole maestranze coordinate in proprio: su una ristrutturazione che al <a href="/ristrutturazioni/costo-ristrutturazione-al-mq-2026/">costo al mq di medio livello</a> vale 100.000-120.000 euro per un 100 mq, il sovrapprezzo è di 10.000-18.000 euro. La maggiorazione copre progettazione, coordinamento, direzione lavori, gestione pratiche e il rischio d'impresa che il general contractor si accolla.</p>
          <p>Il confronto corretto però non è con il cantiere a imprese separate «ben riuscito», ma con quello reale: ritardi medi del 20-30%, varianti in corso d'opera, imprevisti gestiti a rimbalzo. Quando si prezzano il proprio tempo, i fermi cantiere e i contenziosi evitati, il delta si riduce sensibilmente — e per chi non può seguire il cantiere (lavoro, distanza, seconda casa) spesso si annulla del tutto.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="garanzie">Quali garanzie e tutele offre?</h2>
          <p>Il punto di forza della formula è la <strong>responsabilità unica</strong>, ma va tradotta in garanzie contrattuali esplicite. Quelle da pretendere sempre: la garanzia di buon funzionamento e la corretta esecuzione secondo la normativa sui contratti d'appalto; le <strong>Dichiarazioni di Conformità</strong> di tutti gli impianti a firma di installatori abilitati DM 37/2008 — le stesse descritte nella guida al <a href="/impianti/rifacimento-impianto-idraulico-costi/">rifacimento dell'impianto idraulico e ai suoi costi</a>; la polizza <strong>CAR/EAR o postuma decennale</strong> quando l'intervento tocca elementi strutturali; l'assicurazione RCT/RCO dell'impresa per danni a terzi durante i lavori.</p>
          <p>Due tutele economiche fanno la differenza: i <strong>pagamenti a stati di avanzamento</strong> — mai anticipi superiori al 20-30% e saldo a collaudo avvenuto — e la <strong>fideiussione</strong> a garanzia degli acconti per i contratti sopra soglie importanti. Il general contractor serio le propone da sé; chi le rifugge va scartato a prescindere dal prezzo.</p>

          <h2 id="contratto">Cosa deve contenere il contratto</h2>
          <p>Il contratto è l'unica vera garanzia del committente. Gli elementi imprescindibili:</p>
          <ul>
            <li><strong>Capitolato allegato</strong> con voci, quantità, marche e fasce di fornitura dei materiali: è il documento che decide cosa è compreso e cosa no.</li>
            <li><strong>Prezzo e forma</strong> (a corpo o a misura), con l'elenco esplicito degli esclusi e il trattamento delle varianti in corso d'opera.</li>
            <li><strong>Cronoprogramma</strong> con data di consegna e <strong>penali per ritardo</strong> (tipicamente lo 0,5-1% del prezzo per settimana di ritardo, con tetto).</li>
            <li><strong>Pagamenti a SAL</strong> legati a lavori realmente eseguiti e verificabili, saldo a collaudo.</li>
            <li><strong>Nominativi dei tecnici</strong>: direttore lavori, coordinatore sicurezza, responsabile pratiche e detrazioni.</li>
            <li><strong>Documenti di consegna</strong>: DiCo, certificazioni, APE, pratica catastale, schede tecniche e manuali dei materiali posati.</li>
            <li><strong>Clausola risolutiva</strong> e gestione dei contenziosi, meglio con tentativo di mediazione preventivo.</li>
          </ul>

          <h2 id="pro-contro">Vantaggi e limiti: il bilancio onesto</h2>
          <p>I vantaggi sono chiari: un solo interlocutore, tempi contrattualizzati con penali, responsabilità unica su difetti e non conformità, pratiche e detrazioni gestite — incluso il <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">bonus ristrutturazione 2026</a> con bonifici e documentazione a regola d'arte. Per chi ristruttura da remoto, per gli investitori e per le famiglie senza tempo è la formula che riduce di più lo stress.</p>
          <p>I limiti vanno detti con la stessa chiarezza: il sovrapprezzo del 10-15%, una minore libertà di scelta sulle maestranze (la squadra è quella dell'impresa), il rischio di fasce di fornitura «fotografate» su cataloghi che poi richiedono extra, e la qualità disomogenea del mercato — tra il general contractor strutturato e la ditta individuale che si ribattezza chiavi in mano c'è un abisso. La due diligence preliminare non è un optional.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="come-scegliere">Come scegliere l'impresa giusta</h2>
          <p>Quattro verifiche, tutte rapide e tutte decisive. Primo: <strong>visura camerale e solidità</strong> — anni di attività, capitale, assenza di procedure concorsuali; la SOA per gli appalti importanti è un plus. Secondo: <strong>referenze verificabili</strong> — almeno tre cantieri conclusi da visitare o committenti da sentire, non foto generiche. Terzo: <strong>struttura interna</strong> — il chiavi in mano vero ha tecnici, ufficio pratiche e maestranze stabili o consolidate; chi subappalta tutto al ribasso è un intermediario, non un general contractor. Quarto: <strong>contratto e garanzie</strong> proposti in bozza prima dell'impegno, con penali, fideiussioni e capitolato dettagliato.</p>
          <p>Un ultimo consiglio: confrontare almeno due proposte chiavi in mano e una a imprese separate sullo stesso capitolato. Solo così il sovrapprezzo diventa un numero reale su cui decidere, invece che un timore astratto. E chi valuta interventi mirati prima della ristrutturazione totale può partire dai singoli ambienti, come la guida su <a href="/ristrutturazioni/ristrutturare-bagno-costi-tempi/">costi e tempi per ristrutturare il bagno</a>.</p>""",
    faq_title="Domande frequenti sulla ristrutturazione chiavi in mano",
    faq=[
        ("Cosa include esattamente una ristrutturazione chiavi in mano?",
         "Include rilievo e progetto, pratiche edilizie e catastali, coordinamento di tutte le maestranze, forniture e posa, direzione lavori, certificazioni degli impianti e consegna della casa finita con documentazione completa. Gli arredi sono normalmente esclusi salvo pacchetti specifici; gli esclusi vanno sempre elencati nel contratto."),
        ("Quanto costa in più la ristrutturazione chiavi in mano?",
         "Il sovrapprezzo tipico è del <strong>10-15%</strong> rispetto alla gestione a imprese separate: copre progettazione, coordinamento, direzione lavori e pratiche. Su una ristrutturazione da 100.000 euro si tratta di 10.000-15.000 euro, da valutare contro ritardi, varianti e tempo personale richiesti dalla gestione diretta."),
        ("Chi firma le pratiche edilizie nel chiavi in mano?",
         "Le pratiche (CILA, SCIA) sono presentate dal tecnico incaricato, normalmente indicato dal general contractor, ma restano a nome del committente che ne è il titolare. Il contratto deve specificare chi si occupa di quale adempimento, incluse le comunicazioni per le detrazioni fiscali."),
        ("Cosa succede se l'impresa ritarda la consegna?",
         "Se il contratto prevede penali — da pretendere sempre, in genere lo 0,5-1% del prezzo per settimana di ritardo con un tetto massimo — il committente trattiene l'importo dai pagamenti. Senza clausola scritta il risarcimento va dimostrato in giudizio: la penale contrattuale è la tutela che conta."),
        ("Si può usare il bonus ristrutturazione con il chiavi in mano?",
         "Sì: la detrazione del 50% (prima casa) o 36% si applica anche ai contratti chiavi in mano, a condizione che le fatture siano analitiche per voce agevolabile, i pagamenti avvengano con bonifico parlante e la documentazione sia completa. I general contractor strutturati gestiscono l'intero iter documentale."),
    ],
    sources="Normativa sui contratti d'appalto e tutela del committente; listini general contractor rilevati a luglio 2026; Agenzia delle Entrate — guida bonus ristrutturazione 2026. I sovrapprezzi indicati sono medie di mercato: ogni contratto va valutato sul capitolato specifico. Contenuto a scopo informativo.",
    tags=[
        ("/ristrutturazioni/", "Chiavi in mano"),
        ("/ristrutturazioni/", "Contratto di appalto"),
        ("/ristrutturazioni/", "Garanzie"),
        ("/incentivi-bonus/", "Bonus ristrutturazione"),
    ],
    related=REL_CHIAVI, **ER,
),

# ───────────────────── 7. RISTRUTTURARE IL BAGNO ──────────────────────────────
dict(
    silo="ristrutturazioni", silo_name="Ristrutturazioni",
    slug="ristrutturare-bagno-costi-tempi",
    title_tag="Costo ristrutturazione bagno 2026: prezzi e tempi",
    desc="Costo ristrutturazione bagno 2026: da 8.000 a 15.000 € per un bagno completo di 5-6 mq. Voci di prezzo, tempi di cantiere e gli errori da evitare.",
    h1="Ristrutturare il bagno nel 2026: costi, tempi e errori da evitare",
    kicker="Ristrutturazioni · Bagno",
    standfirst="Il bagno è l'ambiente più tecnico della casa e quello dove gli errori costano di più: impianti, impermeabilizzazione, rivestimenti e sanitari si susseguono in pochi metri quadri. Prezzi reali 2026 per taglia, tempi di cantiere settimana per settimana e gli errori che fanno lievitare il conto.",
    breadcrumb_title="Ristrutturare il bagno: costi e tempi",
    pub="2026-07-08", pub_it="8 luglio 2026", mod="2026-07-08", mod_it="8 luglio 2026",
    read_min=8,
    thumb="t-ristrutturazioni", thumb_label="Ristrutturazioni · Bagno",
    thumb_aria="Copertura editoriale: ristrutturazione del bagno",
    keywords="costo ristrutturazione bagno, rifacimento bagno prezzi 2026, tempi ristrutturazione bagno, ristrutturare bagno errori, rifare il bagno costi",
    og_title="Ristrutturare il bagno nel 2026: costi, tempi e errori da evitare",
    og_desc="Da 8.000 a 15.000 euro per un bagno completo: voci di prezzo, tempi di cantiere e gli errori che fanno lievitare il conto.",
    tw_title="Costo ristrutturazione bagno 2026: prezzi e tempi",
    tw_desc="Rifare il bagno nel 2026 costa 8.000-15.000 euro: il dettaglio delle voci, i tempi reali e gli errori da evitare.",
    answer="Ristrutturare completamente un bagno di 5-6 mq costa nel 2026 tra <strong>8.000 e 15.000 euro</strong>, con una forbice che dipende da sanitari, rivestimenti e spostamento degli scarichi. I tempi di cantiere sono di 2-4 settimane. L'errore più costoso è risparmiare su impianti e impermeabilizzazione, le parti nascoste che determinano la durata dell'intervento.",
    toc=[
        ("costi-2026", "Quanto costa ristrutturare il bagno nel 2026?"),
        ("voci-di-costo", "Le voci di costo nel dettaglio"),
        ("tempi-cantiere", "Quanto tempo ci vuole? Il cronoprogramma"),
        ("spostare-sanitari", "Conviene spostare i sanitari?"),
        ("errori-da-evitare", "Gli errori da evitare (e quanto costano)"),
        ("bonus-iva", "Bonus e IVA agevolata nel 2026"),
    ],
    body="""          <h2 id="costi-2026">Quanto costa ristrutturare il bagno nel 2026?</h2>
          <p>Il <strong>costo di ristrutturazione del bagno</strong> nel 2026 per un intervento completo — demolizione, impianti, impermeabilizzazione, rivestimenti, sanitari e rubinetteria — si colloca tra <strong>8.000 e 15.000 euro</strong> per un bagno standard di 5-6 mq. La fascia si articola così: 8.000-10.000 euro con materiali di fascia base e sanitari standard, 10.000-13.000 euro per il livello medio (gres di qualità, sanitari sospesi, box doccia walk-in), oltre 15.000 euro per finiture alte, docce filo pavimento e arredo su misura.</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Costo rifacimento bagno per taglia e livello (Italia, 2026)</caption>
            <thead>
              <tr><th>Tipologia</th><th>Livello base</th><th>Livello medio</th><th>Livello alto</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Bagnino di servizio (2-3 mq)</strong></td><td>5.000-7.000 €</td><td>7.000-9.000 €</td><td>9.000-12.000 €</td></tr>
              <tr><td><strong>Bagno standard (5-6 mq)</strong></td><td>8.000-10.000 €</td><td>10.000-13.000 €</td><td>13.000-18.000 €</td></tr>
              <tr><td><strong>Bagno padronale (8-10 mq)</strong></td><td>11.000-14.000 €</td><td>14.000-19.000 €</td><td>19.000-28.000 €</td></tr>
              <tr><td><strong>Solo rivestimenti e sanitari (senza impianti)</strong></td><td>4.000-5.500 €</td><td>5.500-8.000 €</td><td>8.000-12.000 €</td></tr>
            </tbody>
          </table>
          </div>
          <p>La voce che sposta di più il preventivo è lo <strong>spostamento degli scarichi</strong>: rifare la colonna o spostare il wc richiede demolizioni profonde, verifica delle pendenze e spesso il consenso condominiale, e aggiunge 1.500-3.500 euro rispetto alla sostituzione in sede. Per il contesto completo dei prezzi di cantiere, il riferimento è la nostra analisi del <a href="/ristrutturazioni/costo-ristrutturazione-al-mq-2026/">costo di ristrutturazione al mq nel 2026</a>.</p>

          <h2 id="voci-di-costo">Le voci di costo nel dettaglio</h2>
          <p>Un bagno standard di livello medio si scompone in sette voci principali:</p>
          <ul>
            <li><strong>Demolizione e smaltimento</strong>: 800-1.200 euro. Include rimozione di sanitari, rivestimenti e massetto esistente e trasporto in discarica autorizzata.</li>
            <li><strong>Impianto idrico e scarichi</strong>: 1.800-3.000 euro. Adduzioni in multistrato o PPR, nuovi scarichi con pendenze corrette, sifoni e attacchi. Il dettaglio dei prezzi al punto acqua è nella guida al <a href="/impianti/rifacimento-impianto-idraulico-costi/">rifacimento dell'impianto idraulico</a>.</li>
            <li><strong>Massetto e impermeabilizzazione</strong>: 600-1.000 euro. La guaina liquida o a membrana sotto il pavimento e nei primi 30 cm di parete è la voce su cui non si risparmia mai.</li>
            <li><strong>Pavimento e rivestimenti</strong>: 1.500-3.000 euro per gres di fascia media posato (35-55 €/mq posa compresa su pareti e pavimento); mosaici e grandi formati fanno salire la posa.</li>
            <li><strong>Sanitari e rubinetteria</strong>: 1.200-3.000 euro. Wc e bidet sospesi con cassetta incasso costano 150-250 euro in più a pezzo ma facilitano la pulizia e guadagnano profondità.</li>
            <li><strong>Doccia o vasca</strong>: 600-2.000 euro per piatto e box; le soluzioni filo pavimento con canalina partono da 1.200 euro installate.</li>
            <li><strong>Elettrico, ventilazione e finiture</strong>: 500-1.000 euro tra punti luce, aspiratore (obbligatorio nei bagni ciechi), silicone e collaudi.</li>
          </ul>

          <h2 id="tempi-cantiere">Quanto tempo ci vuole? Il cronoprogramma</h2>
          <p>Un bagno rifatto da zero richiede <strong>2-4 settimane di cantiere</strong>, più i tempi tecnici di asciugatura che non si possono forzare. La sequenza tipo: 2-3 giorni di demolizione e rimozione macerie; 3-5 giorni per tracce, impianti idrico ed elettrico e prime prove di tenuta; 2-3 giorni per massetto e impermeabilizzazione, cui seguono 5-7 giorni di maturazione prima della posa; 3-4 giorni di pavimenti e rivestimenti; infine 2-3 giorni per sanitari, rubinetteria, box doccia, silicone e collaudo finale.</p>
          <p>Le dilazioni tipiche arrivano da tre cause: materiali non disponibili a magazzino (ordinare rivestimenti e sanitari prima dell'avvio), imprevisti in demolizione (tubi in piombo, scarichi ammalorati, umidità nelle murature) e tempi di asciugatura forzati — posare su massetto umido è la prima causa di distacchi e macchie di salnitro a distanza di mesi. Chi abita in casa durante i lavori consideri che il bagno resta inagibile per l'intera durata: con un solo bagno serve una soluzione temporanea.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="spostare-sanitari">Conviene spostare i sanitari?</h2>
          <p>Spostare wc, doccia e lavabo migliora spesso la funzionalità, ma ha un costo tecnico preciso: ogni metro di spostamento del wc richiede di ricostruire lo scarico con pendenza minima del 1-2%, e oltre i 2-3 metri dalla colonna serve una soluzione tecnica (sanitrit o rialzo del pavimento). Costo tipico: 800-1.500 euro per punto spostato, più il ripristino. In condominio, toccare la colonna fecale richiede l'autorizzazione assembleare perché è parte comune.</p>
          <p>La regola pratica: se la distribuzione esistente funziona, la sostituzione in sede fa risparmiare 2.000-4.000 euro e due settimane; se il bagno è scomodo o i sanitari sono mal posizionati, lo spostamento è un investimento che si ripaga in vivibilità quotidiana e valore dell'immobile — e in quel caso conviene farlo in un'unica ristrutturazione piuttosto che tornare su lavori finiti.</p>

          <h2 id="errori-da-evitare">Gli errori da evitare (e quanto costano)</h2>
          <ol>
            <li><strong>Risparmiare sull'impermeabilizzazione</strong>: una guaina sottodimensionata o assente è la prima causa di infiltrazioni al piano di sotto; il rifacimento a danno avvenuto costa 3-5 volte la voce risparmiata.</li>
            <li><strong>Riusare scarichi vecchi</strong>: tubazioni in piombo o ghisa affaticata vanno sostituite quando il bagno è aperto; risparmiarle significa rifare tutto alla prima occlusione.</li>
            <li><strong>Posare su massetto umido</strong>: il distacco delle piastrelle e le efflorescenze arrivano dopo mesi, a garanzia già discussa.</li>
            <li><strong>Sottovalutare l'aerazione</strong>: nei bagni ciechi l'aspiratore forzato è obbligatorio; nei bagni finestrati resta la migliore difesa dalla muffa.</li>
            <li><strong>Scegliere il piatto doccia dopo gli scarichi</strong>: la posizione dello scarico a pavimento va decisa in fase impiantistica, non a fine lavori.</li>
            <li><strong>Non chiedere la Dichiarazione di Conformità</strong>: la DiCo dell'impianto idraulico ed elettrico è obbligatoria e serve per detrazioni, assicurazioni e rivendita.</li>
          </ol>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="bonus-iva">Bonus e IVA agevolata nel 2026</h2>
          <p>Il rifacimento del bagno è manutenzione straordinaria e rientra nel <strong>bonus ristrutturazione</strong>: detrazione del 50% sulla prima casa (36% sulle altre unità) entro il massimale di 96.000 euro, con bonifico parlante e fatture analitiche. Sono agevolabili impianti, demolizioni, rivestimenti, sanitari e rubinetteria (beni significativi con IVA al 10% entro il valore della prestazione). I requisiti completi sono nella <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">guida al bonus ristrutturazione 2026</a>.</p>
          <p>L'IVA agevolata al 10% si applica su manodopera e materiali posati, con la regola dei beni significativi: su sanitari, rubinetteria e box doccia l'aliquota ridotta vale fino a concorrenza del valore della prestazione, l'eccedenza va al 22%. Per i lavori che modificano la distribuzione interna serve inoltre verificare il titolo edilizio — CILA nella maggior parte dei casi — come spiega la guida sui <a href="/ristrutturazioni/ristrutturare-casa-permessi-cila-scia/">permessi per ristrutturare casa</a>; chi preferisce delegare tutto può valutare la formula <a href="/ristrutturazioni/ristrutturazione-chiavi-in-mano/">chiavi in mano</a> anche per il solo bagno.</p>""",
    faq_title="Domande frequenti sulla ristrutturazione del bagno",
    faq=[
        ("Qual è il costo di ristrutturazione di un bagno di 5 mq nel 2026?",
         "Il costo di ristrutturazione completa di un bagno di 5 mq nel 2026 è di <strong>8.000-13.000 euro</strong> per i livelli base e medio: demolizione, impianti idrici e scarichi, impermeabilizzazione, rivestimenti, sanitari e rubinetteria compresi. Con materiali di fascia alta, doccia filo pavimento e arredo su misura si superano i 15.000 euro."),
        ("Quanto tempo serve per rifare un bagno da zero?",
         "Da 2 a 4 settimane di cantiere: 2-3 giorni di demolizione, una settimana per impianti e tracce, massetto e impermeabilizzazione con 5-7 giorni di maturazione, poi posa di pavimenti e rivestimenti e infine sanitari e collaudo. I tempi di asciugatura non si possono comprimere senza rischiare distacchi."),
        ("Si può ristrutturare il bagno senza rifare gli impianti?",
         "Sì, se gli impianti sono recenti e a norma: la sostituzione di rivestimenti, sanitari e rubinetteria senza toccare tubazioni costa 4.000-8.000 euro. Ma se le tubature hanno più di 25-30 anni o sono in piombo, rifare tutto a bagno aperto è l'unica scelta economicamente sensata."),
        ("Il rifacimento del bagno rientra nel bonus ristrutturazione 2026?",
         "Sì: è manutenzione straordinaria agevolabile al <strong>50% sulla prima casa</strong> (36% sulle altre unità) entro 96.000 euro di spesa. Servono bonifico parlante, fatture analitiche e conservazione delle Dichiarazioni di Conformità degli impianti. L'IVA agevolata al 10% si applica con la regola dei beni significativi."),
        ("Serve un permesso per ristrutturare il bagno?",
         "Il rifacimento in sede senza modifiche alla distribuzione è attività libera o assimilabile; lo spostamento dei sanitari e la modifica della planimetria richiedono in genere la CILA, e toccare la colonna fecale in condominio richiede il consenso assembleare perché la colonna è parte comune."),
    ],
    sources="Listini imprese idrauliche e rivestimenti (luglio 2026); prezziari regionali opere edili; Agenzia delle Entrate — guida bonus ristrutturazione 2026. I prezzi sono medie nazionali: il preventivo reale richiede sopralluogo. Contenuto a scopo informativo.",
    tags=[
        ("/ristrutturazioni/", "Ristrutturare il bagno"),
        ("/ristrutturazioni/", "Costi 2026"),
        ("/impianti/", "Impianto idraulico"),
        ("/incentivi-bonus/", "Bonus ristrutturazione"),
    ],
    related=REL_BAGNO, **PG,
),

# ───────────────────── 8. PERMESSI CILA SCIA ──────────────────────────────────
dict(
    silo="ristrutturazioni", silo_name="Ristrutturazioni",
    slug="ristrutturare-casa-permessi-cila-scia",
    title_tag="Permessi ristrutturazione casa: CILA, SCIA, titolo",
    desc="Permessi ristrutturazione casa: quando basta l'edilizia libera, quando serve la CILA, quando la SCIA o il permesso di costruire. Tabella per lavoro.",
    h1="Ristrutturare casa: quali permessi servono tra CILA, SCIA e titolo edilizio",
    kicker="Ristrutturazioni · Permessi",
    standfirst="Tinteggiare è libero, spostare una tramezza richiede la CILA, ingrandire una finestra può richiedere la SCIA: il confine tra i titoli edilizi è sottile e sbagliarlo costa caro. La mappa completa dei permessi per ristrutturare casa nel 2026, lavoro per lavoro.",
    breadcrumb_title="Permessi per ristrutturare casa",
    pub="2026-07-02", pub_it="2 luglio 2026", mod="2026-07-02", mod_it="2 luglio 2026",
    read_min=8,
    thumb="t-ristrutturazioni", thumb_label="Ristrutturazioni · Permessi",
    thumb_aria="Copertura editoriale: permessi e titoli edilizi per ristrutturare casa",
    keywords="permessi ristrutturazione casa, CILA quando serve, SCIA ristrutturazione, edilizia libera, titolo edilizio ristrutturazione",
    og_title="Ristrutturare casa: quali permessi servono tra CILA, SCIA e titolo edilizio",
    og_desc="Edilizia libera, CILA, SCIA e permesso di costruire: quale titolo serve per ogni lavoro di ristrutturazione, con tabella e sanzioni.",
    tw_title="Permessi ristrutturazione casa: CILA, SCIA, titolo",
    tw_desc="Quale permesso serve per ristrutturare casa: edilizia libera, CILA, SCIA o permesso di costruire, lavoro per lavoro.",
    answer="Per ristrutturare casa nel 2026 i <strong>permessi</strong> dipendono dai lavori: tinteggiature, pavimenti e impianti sono in <strong>edilizia libera</strong>; spostare tramezzi o modificare la distribuzione richiede la <strong>CILA</strong>; opere strutturali, nuove aperture o ampliamenti richiedono la <strong>SCIA</strong>; le nuove costruzioni e le ristrutturazioni pesanti il permesso di costruire. La verifica va fatta prima dell'avvio con un tecnico.",
    toc=[
        ("edilizia-libera", "Quali lavori sono in edilizia libera?"),
        ("cila", "CILA: cos'è e quando serve"),
        ("scia", "SCIA: quando è obbligatoria"),
        ("permesso-costruire", "Quando serve il permesso di costruire"),
        ("tabella-permessi", "La tabella dei titoli, lavoro per lavoro"),
        ("condominio", "E in condominio? Le regole sulle parti comuni"),
        ("sanzioni", "Cosa rischia chi lavora senza titolo"),
    ],
    body="""          <h2 id="edilizia-libera">Quali lavori sono in edilizia libera?</h2>
          <p>La buona notizia per chi affronta i <strong>permessi di ristrutturazione di casa</strong> è che la maggior parte degli interventi interni non richiede alcun titolo: è <strong>edilizia libera</strong>, disciplinata dal Glossario unico allegato al Testo Unico dell'edilizia. Rientrano in questa categoria la tinteggiatura di pareti e soffitti, la sostituzione di pavimenti e rivestimenti, il rifacimento degli impianti senza modifica della distribuzione, la sostituzione dei sanitari in sede, la posa di controsoffitti e la sostituzione di porte interne.</p>
          <p>Sono liberi anche la sostituzione degli infissi esterni a parità di sagoma e materiale, la riparazione del manto di copertura senza modifiche strutturali e l'installazione di pannelli solari su edifici (salvo vincoli paesaggistici o regolamenti particolari). L'edilizia libera non significa però «senza regole»: gli impianti richiedono comunque la Dichiarazione di Conformità, le detrazioni fiscali i loro adempimenti, e le parti condominiali il rispetto del regolamento.</p>

          <h2 id="cila">CILA: cos'è e quando serve</h2>
          <p>La <strong>CILA</strong> (Comunicazione di Inizio Lavori Asseverata) è il titolo per la <strong>manutenzione straordinaria leggera</strong>: interventi che modificano la distribuzione interna senza toccare le strutture portanti. Serve quando si spostano o eliminano tramezzi, si uniscono o dividono locali, si sposta il bagno o la cucina — con i costi che abbiamo analizzato nella guida a <a href="/ristrutturazioni/ristrutturare-bagno-costi-tempi/">ristrutturare il bagno</a> — si apre una porta interna su un muro non portante, si realizza un secondo bagno o una cabina armadio.</p>
          <p>La CILA è «asseverata» perché un tecnico abilitato — geometra, architetto, ingegnere — dichiara sotto la propria responsabilità che l'intervento non riguarda parti strutturali e rispetta le norme. I lavori possono iniziare il giorno stesso della presentazione allo Sportello Unico. Il costo tecnico tipico è di 500-1.500 euro secondo complessità, cui si aggiungono i diritti di segreteria comunali. Alla fine dei lavori, se la planimetria è cambiata, va presentato l'<strong>aggiornamento catastale</strong> (DOCFA) entro 30 giorni: la planimetria non conforme blocca compravendite e può costare la detrazione del bonus.</p>

          <h2 id="scia">SCIA: quando è obbligatoria</h2>
          <p>La <strong>SCIA</strong> (Segnalazione Certificata di Inizio Attività) è il titolo per gli interventi che toccano le <strong>strutture portanti</strong> o l'involucro: aperture di porte su muri portanti, creazione o modifica di finestre e balconi, rinforzi di solai, sostituzione del tetto con modifica strutturale, recupero dei sottotetti con opere strutturali, chiusura di verande e, in molti casi, il cappotto termico con variazione del prospetto.</p>
          <p>Come la CILA, la SCIA permette di iniziare subito i lavori, ma il Comune ha 30 giorni per verifiche e può ordinare il fermo se la pratica è incompleta o l'intervento non conforme. Richiede la relazione strutturale di un professionista e, nelle zone sismiche, il deposito del progetto strutturale al Genio Civile. Il costo tecnico è più alto — da 1.500 a 5.000 euro e oltre per gli interventi strutturali — e i tempi di progettazione vanno messi in conto nel cronoprogramma.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="permesso-costruire">Quando serve il permesso di costruire</h2>
          <p>Il <strong>permesso di costruire</strong> — oggi «titolo abilitativo edilizio» nella terminologia aggiornata — resta obbligatorio per le nuove costruzioni, gli ampliamenti volumetrici, le ristrutturazioni edilizie pesanti che cambiano sagoma, prospetti o destinazione d'uso dell'immobile e le ristrutturazioni di edifici vincolati. I tempi di rilascio variano da 60 a 90 giorni e oltre secondo il Comune, e i lavori non possono iniziare prima del rilascio.</p>
          <p>Nelle zone sottoposte a vincolo paesaggistico o storico-architettonico si aggiunge l'autorizzazione della Soprintendenza, che può richiedere mesi e condiziona materiali, colori e forme. Chi acquista da ristrutturare in centro storico o in zona vincolata dovrebbe far verificare la fattibilità degli interventi prima del rogito: le sorprese post-acquisto sui vincoli sono tra le cause più frequenti di contenzioso immobiliare.</p>

          <h2 id="tabella-permessi">La tabella dei titoli, lavoro per lavoro</h2>
          <div class="table-wrap">
          <table>
            <caption>Tabella 1 — Titolo edilizio richiesto per i principali lavori di ristrutturazione (quadro nazionale, 2026)</caption>
            <thead>
              <tr><th>Intervento</th><th>Titolo richiesto</th><th>Note</th></tr>
            </thead>
            <tbody>
              <tr><td>Tinteggiatura, pavimenti, rivestimenti</td><td><strong>Edilizia libera</strong></td><td>Nessuna comunicazione</td></tr>
              <tr><td>Rifacimento impianti senza spostamenti</td><td><strong>Edilizia libera</strong></td><td>DiCo obbligatoria</td></tr>
              <tr><td>Sostituzione infissi a pari sagoma</td><td><strong>Edilizia libera</strong></td><td>Salvo vincoli e regolamento condominiale</td></tr>
              <tr><td>Spostare/abbattere tramezzi</td><td><strong>CILA</strong></td><td>Asseverazione tecnica + aggiornamento catastale</td></tr>
              <tr><td>Spostare bagno o cucina</td><td><strong>CILA</strong></td><td>Verifica scarichi e pendenze</td></tr>
              <tr><td>Nuova finestra o allargamento</td><td><strong>SCIA</strong></td><td>Incide su prospetto e rapporti aeroilluminanti</td></tr>
              <tr><td>Apertura su muro portante</td><td><strong>SCIA</strong></td><td>Progetto strutturale, in zona sismica deposito obbligatorio</td></tr>
              <tr><td>Cappotto termico esterno</td><td><strong>CILA o SCIA</strong></td><td>Secondo variazione di prospetto e Comune</td></tr>
              <tr><td>Ampliamento, sopraelevazione</td><td><strong>Permesso di costruire</strong></td><td>Con oneri di urbanizzazione</td></tr>
              <tr><td>Edifici vincolati</td><td><strong>Permesso + autorizzazione</strong></td><td>Parere Soprintendenza preventivo</td></tr>
            </tbody>
          </table>
          </div>
          <p>Attenzione: il quadro nazionale si incrocia con regolamenti edilizi comunali che possono essere più restrittivi — ad esempio su balconi, verande e prospetti — e con i vincoli di piano. La tabella orienta, ma la verifica sul proprio Comune con un tecnico resta il passaggio obbligato prima di firmare il contratto con l'impresa. Per il quadro completo del cantiere, utile anche la panoramica sul <a href="/ristrutturazioni/costo-ristrutturazione-al-mq-2026/">costo di ristrutturazione al mq nel 2026</a>, dove pratiche e oneri entrano nelle voci di budget; chi preferisce delegare l'intero iter, pratiche comprese, può valutare la <a href="/ristrutturazioni/ristrutturazione-chiavi-in-mano/">ristrutturazione chiavi in mano</a>.</p>

          <div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-2" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>

          <h2 id="condominio">E in condominio? Le regole sulle parti comuni</h2>
          <p>In condominio i titoli edilizi si sommano alle regole condominiali. I lavori dentro il proprio appartamento sono liberi nel rispetto del regolamento (che spesso impone orari e comunicazioni all'amministratore), ma <strong>tutto ciò che tocca le parti comuni richiede l'autorizzazione assembleare</strong>: colonne fecali e di scarico, facciate, terrazzi a uso esclusivo ma di copertura, canne fumarie, installazione di condizionatori o pannelli sulla facciata comune.</p>
          <p>La giurisprudenza consolidata tutela anche il «decoro architettonico»: tende, verande, climatizzatori e oscuranti visibili dall'esterno possono essere vietati dal regolamento o richiedere delibera. Chi ristruttura in condominio dovrebbe sempre consegnare all'amministratore la comunicazione di inizio lavori con i dati dell'impresa, le coperture assicurative e il cronoprogramma: previene contestazioni e fermi.</p>

          <h2 id="sanzioni">Cosa rischia chi lavora senza titolo</h2>
          <p>L'abuso edilizio non è un rischio teorico: le verifiche incrociate tra Catasto, Agenzia delle Entrate (le pratiche del <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">bonus ristrutturazione 2026</a> espongono i lavori al controllo) e Comuni sono ormai sistematiche. Le conseguenze per chi lavora senza titolo o in difformità: <strong>fermo cantiere immediato</strong>, sanzione pecuniaria proporzionata (per le difformità minori si regolarizza con la CILA/SCIA tardiva e una sanzione raddoppiata), e nei casi gravi <strong>ordine di demolizione o ripristino</strong> e rilevanza penale dell'abuso.</p>
          <p>C'è poi il capitolo civile: la casa con abusi non si vende (il notaio richiede la conformità urbanistica), non si finanzia (le banche la peritano) e perde le detrazioni se le pratiche bonus non combaciano con i titoli. La regola finale è semplice: la pratica edilizia costa tra lo 0,5% e il 3% del valore dei lavori; l'abuso costa moltiplicatori di quella cifra e la serenità. E con la <a href="/normative/direttiva-case-green-cosa-cambia/">direttiva Case Green</a> che spinge la riqualificazione del patrimonio, lavorare in regola è anche la via per accedere agli incentivi che renderanno obbligatorio — non solo conveniente — il rinnovo del parco immobiliare italiano.</p>""",
    faq_title="Domande frequenti sui permessi per ristrutturare casa",
    faq=[
        ("Quali permessi servono per ristrutturare casa nel 2026?",
         "I permessi per ristrutturare casa dipendono dai lavori: <strong>edilizia libera</strong> per tinteggiature, pavimenti e impianti; <strong>CILA</strong> per spostare tramezzi o modificare la distribuzione; <strong>SCIA</strong> per opere strutturali, nuove aperture e modifiche al prospetto; <strong>permesso di costruire</strong> per ampliamenti, nuove costruzioni e ristrutturazioni pesanti. La verifica preventiva con un tecnico è obbligata."),
        ("Serve la CILA per abbattere una parete interna?",
         "Dipende dalla parete: abbattere o spostare un tramezzo (parete non portante) richiede la CILA con asseverazione di un tecnico e successivo aggiornamento catastale. Aprire un varco in un muro portante richiede invece la SCIA con progetto strutturale e, in zona sismica, deposito al Genio Civile."),
        ("Si possono cambiare le finestre senza permesso?",
         "La sostituzione a parità di sagoma, dimensioni e materiale è in genere edilizia libera, salvo regolamento condominiale e vincoli. Cambiare dimensioni, forma o posizione delle finestre modifica il prospetto e richiede la SCIA, oltre al rispetto dei rapporti aeroilluminanti minimi dei locali."),
        ("Cosa succede se ristrutturo senza CILA?",
         "Il Comune può ordinare il fermo lavori e applicare una sanzione pecuniaria; la regolarizzazione avviene con CILA tardiva e sanzione raddoppiata. Le conseguenze pesanti arrivano però in fase di vendita (la planimetria non conforme blocca l'atto) e sulle detrazioni, che richiedono coerenza tra titoli e lavori eseguiti."),
        ("Chi paga i tecnici per CILA e SCIA?",
         "Il committente: l'asseverazione della CILA costa in genere 500-1.500 euro, la SCIA con progetto strutturale da 1.500 a 5.000 euro e oltre. Sono spese detraibili con il bonus ristrutturazione se relative a interventi agevolabili. Alcune imprese chiavi in mano le includono nel pacchetto."),
    ],
    sources="Testo Unico dell'edilizia e Glossario unico dell'edilizia libera; normativa sismica e circolari applicative; regolamenti edilizi comunali tipo; giurisprudenza su parti comuni e decoro architettonico. Aggiornato al 2 luglio 2026: verificare sempre il regolamento del proprio Comune. Contenuto a scopo informativo, non sostituisce la consulenza di un tecnico abilitato.",
    tags=[
        ("/ristrutturazioni/", "Permessi ristrutturazione"),
        ("/normative/", "CILA e SCIA"),
        ("/ristrutturazioni/", "Edilizia libera"),
        ("/normative/", "Titoli edilizi"),
    ],
    related=REL_PERMESSI, **SC,
),
]
