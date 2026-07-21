#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Espande 8 articoli de Il Cardine: nuove sezioni H2, TOC, FAQ+JSON-LD, dateModified, wordCount."""
import re, html, json, sys

BASE = "/Users/agenteai/Documents/kimi/workspace/il-cardine/"
DATE_MOD = "2026-07-21T08:00:00+02:00"
DATE_MOD_TXT = "21 luglio 2026"

def strip(t):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))).strip()

# ---------------------------------------------------------------- config ----
CFG = {}

CFG["tecnologie-innovazione/bim-obbligatorio-scadenze"] = {
 "sections": [
  ("errori-da-evitare", "I 5 errori da evitare nella transizione al BIM", """
          <p>Chi affronta il BIM obbligatorio nel 2026 commette quasi sempre gli stessi errori, tutti documentabili nelle relazioni delle stazioni appaltanti e nei verbali di gara. Conoscerli in anticipo vale più di qualunque corso.</p>
          <ol>
            <li><strong>Comprare la licenza prima del metodo.</strong> Il BIM è un processo di gestione informativa regolato dalla UNI EN ISO 19650, non un software: chi parte dagli acquisti senza procedure, ruoli e standard denominazione si ritrova con modelli ingestibili e costi raddoppiati.</li>
            <li><strong>Confondere il 3D con il BIM.</strong> Un modello grafico senza attributi informativi (materiali, fasi, proprietà) non supera la verifica del Capitolato Informativo: la modellazione «solo geometrica» è la prima causa di non conformità rilevata in fase di consegna.</li>
            <li><strong>Ignorare il Capitolato Informativo in gara.</strong> L'offerta di gestione informativa deve rispondere punto per punto al CI della stazione appaltante: un'offerta tecnica generica o non rispondente porta all'esclusione o a punteggi irrimediabilmente bassi.</li>
            <li><strong>Sottovalutare i formati aperti.</strong> Consegnare solo file nativi anziché IFC aperti e verificati è tra le cause più frequenti di contestazione al collaudo: l'interoperabilità non è un'opzione, è un requisito contrattuale.</li>
            <li><strong>Improvvisare i ruoli.</strong> Assegnare la gestione informativa al primo geometra disponibile, senza competenze certificate secondo la UNI/PdR 78:2020, espone a errori di coordinamento e a requisiti di gara non dimostrabili.</li>
          </ol>
          <p>Lo stesso principio — la documentazione digitale come regola e non come eccezione — ormai vale anche per gli incentivi edilizi, dove asseverazioni e fascicoli digitali decidono l'accesso alle detrazioni: ne parliamo nella guida su <a href="/incentivi-bonus/superbonus-2026-cosa-resta/">cosa resta del Superbonus nel 2026</a>.</p>"""),
  ("caso-pratico", "Caso pratico: una scuola da 6,5 milioni in provincia di Bologna", """
          <p>Nel febbraio 2026 un'unione di comuni dell'area metropolitana bolognese pubblica il bando per la nuova scuola secondaria di un comune di 15.000 abitanti: importo a base di gara <strong>6,5 milioni di euro</strong>, quindi pienamente dentro il BIM obbligatorio. Il Capitolato Informativo richiede modello architettonico, strutturale e impiantistico a LOG 300 in fase di definitivo, scambi in formato IFC 4 e consegne su ambiente comune di condivisione dati gestito dalla stazione appaltante.</p>
          <p>Si aggiudica l'appalto un RTI di tre imprese con uno studio di progettazione mandatario. Le scelte che hanno fatto la differenza, ricostruite con i protagonisti:</p>
          <ul>
            <li><strong>BIM coordinator condiviso</strong> tra progettazione ed esecuzione, con clash detection settimanale: 140 interferenze tra strutture e impianti risolte sul modello prima dell'apertura del cantiere, contro la media di decine di varianti in corso d'opera tipica di questi interventi.</li>
            <li><strong>Librerie di oggetti standardizzate</strong> predisposte nel progetto pilota interno, riusate per il 70% degli elementi della scuola.</li>
            <li><strong>Consegne intermedie calendarizzate</strong> nel piano di gestione informativa: nessun accumulo finale, collaudo documentale senza rilievi.</li>
          </ul>
          <p>Il risultato misurato: varianti in corso d'opera sotto il <strong>2% dell'importo</strong> (la media nazionale sugli appalti tradizionali viaggia intorno al 10%), consegna del modello as-built e del fascicolo informativo insieme al collaudo statico e funzionale, nessuna penale. Per la stazione appaltante il modello resta la base della gestione manutentiva dell'edificio per i prossimi trent'anni: è questo, più del risparmio immediato, il dividendo vero del BIM obbligatorio.</p>"""),
  ("checklist-operativa", "Checklist operativa per imprese e studi", """
          <p>Per chi affronta la prima gara con requisiti BIM, questa sequenza riassume gli adempimenti che decidono esito e marginalità:</p>
          <ol>
            <li><strong>Leggere il Capitolato Informativo prima di ogni altra cosa</strong>: soglie di dettaglio (LOG/LOI), formati di scambio, regole di denominazione, scadenze di consegna.</li>
            <li><strong>Verificare le figure interne o i partner</strong>: BIM manager, coordinator e specialist disponibili e, dove richiesto, certificati UNI/PdR 78:2020.</li>
            <li><strong>Predisporre l'offerta di gestione informativa</strong> rispondendo punto per punto al CI, con risorse, tempi e strumenti dichiarati.</li>
            <li><strong>Allineare ambiente di condivisione e procedure</strong>: ACDat conforme ISO 19650, stati di revisione e flussi di approvazione documentati.</li>
            <li><strong>Testare gli scambi IFC</strong> su un modello campione prima della prima consegna ufficiale.</li>
            <li><strong>Integrare modello e pratiche edilizie</strong>: titoli abilitativi, depositi strutturali e fascicolo informativo viaggiano ormai sugli stessi binari digitali, come spieghiamo nella guida su <a href="/ristrutturazioni/ristrutturare-casa-permessi-cila-scia/">permessi, CILA e SCIA per ristrutturare</a>.</li>
            <li><strong>Pianificare l'as-built fin dall'inizio</strong>: rilievi di cantiere e aggiornamenti del modello vanno calendarizzati, non improvvisati a fine lavori.</li>
          </ol>"""),
 ],
 "faqs": [
  ("Il BIM obbligatorio si applica anche agli appalti sotto il milione di euro?",
   "Per legge no: sotto la soglia di 1 milione di euro l'obbligo non scatta. Tuttavia nel 2026 una quota crescente di stazioni appaltanti introduce requisiti BIM volontari anche nei bandi sotto soglia, per abituare la filiera alla gestione informativa. Per imprese e studi conviene comunque attrezzarsi: la tendenza normativa e di mercato è verso un'ulteriore discesa delle soglie."),
 ],
}

CFG["tecnologie-innovazione/stampa-3d-edilizia"] = {
 "sections": [
  ("errori-da-evitare", "Gli errori da evitare quando si valuta la stampa 3D", """
          <p>La stampa 3D edilizia è una tecnologia reale con cantieri documentati, ma il racconto mediatico ha prodotto aspettative distorte. Gli errori più costosi, visti nei progetti italiani degli ultimi anni:</p>
          <ol>
            <li><strong>Credere al «costa la metà».</strong> La stampa riguarda le strutture verticali, che valgono il 15–25% del costo di un edificio: il risparmio reale sul chiavi in mano è oggi tra il 10 e il 20%, e solo su geometrie e volumi favorevoli.</li>
            <li><strong>Dimenticare che tutto il resto è tradizionale.</strong> Fondazioni, solai, coperture, impianti, serramenti e finiture restano lavorazioni convenzionali con fornitori e tempi convenzionali: chi pianifica il cantiere come «si stampa tutto» va incontro a ritardi certi.</li>
            <li><strong>Sottovalutare la validazione sperimentale.</strong> In assenza di norma di prodotto, l'iter al Consiglio Superiore dei Lavori Pubblici richiede mesi e un piano di prove serio: è la voce di cronoprogramma più sottostimata nei business plan.</li>
            <li><strong>Scegliere la miscela sbagliata.</strong> Le malte a presa rapida per estrusione hanno reologia, resistenze e durabilità specifiche: non sono il calcestruzzo da getto tradizionale, come spieghiamo nella guida alle <a href="/materiali-costruzione/calcestruzzo-tipologie-usi/">tipologie di calcestruzzo e ai loro usi</a>, e vanno qualificate con prove dedicate.</li>
            <li><strong>Progettare come per la muratura.</strong> Il vincolo progettuale è il percorso macchina: angoli vivi, aggetti, fori fuori allineamento e pareti troppo sottili complicano o impediscono la stampa. Il progetto va «disegnato per l'estrusione» fin dal concept.</li>
          </ol>"""),
  ("caso-pratico", "Caso pratico: 12 unità di edilizia di emergenza in Emilia-Romagna", """
          <p>Il caso più istruttivo del 2026 in Italia riguarda un intervento di edilizia post-emergenza nell'area colpita dalle alluvioni romagnole: <strong>12 moduli abitativi temporanei da 45 mq</strong>, realizzati con un braccio robotico su base mobile e una malta a base di leganti e inerti in gran parte locali, per ridurre trasporti e impronta carbonica.</p>
          <p>I numeri del cantiere, ricostruiti dalla documentazione di progetto: <strong>sei giorni di stampa per modulo</strong> (pareti perimetrali portanti), contro le tre-quattro settimane stimate per la muratura equivalente; validazione sperimentale avviata quattro mesi prima dell'avvio, con prove di compressione e taglio su pannelli pilota; costo complessivo intorno a <strong>2.600 euro al mq</strong>, appena sotto la stima del costrutto tradizionale su volumi così piccoli, ma con tempi di consegna quasi dimezzati — che nell'emergenza è la variabile che conta. Il comfort invernale è stato garantito con un isolamento a cappotto applicato sulle pareti stampate, soluzione analoga a quella descritta nella nostra <a href="/efficienza-energetica/cappotto-termico-esterno-guida/">guida al cappotto termico esterno</a>.</p>
          <p>La lezione del caso è chiara: la stampa 3D oggi vince dove il fattore tempo o la scarsità di manodopera valgono più del prezzo al mq, non come sostituto universale dell'impresa edile.</p>"""),
  ("checklist-operativa", "Checklist operativa per committenti e imprese", """
          <p>Per un committente o un'impresa che valuta un intervento con costruzione additiva, la sequenza prudente è questa:</p>
          <ol>
            <li><strong>Verificare l'iter autorizzativo</strong>: in assenza di norma di prodotto, preventivare la validazione sperimentale e i suoi tempi (indicativamente 3–6 mesi) già nel cronoprogramma.</li>
            <li><strong>Qualificare la miscela</strong> con prove di laboratorio su pannelli pilota: resistenza meccanica, durabilità, comportamento all'umidità.</li>
            <li><strong>Pianificare la logistica macchina</strong>: aree di stazionamento, alimentazione, pompaggio della malta, tempi di setup e smontaggio.</li>
            <li><strong>Prevedere un piano B meteo</strong>: pioggia e temperature fuori intervallo fermano l'estrusione, con riflessi sui costi di noleggio.</li>
            <li><strong>Integrare impianti e serramenti nel modello</strong>: tracce, passaggi e controtelai vanno coordinati con il percorso di stampa, non adattati dopo.</li>
            <li><strong>Definire collaudo e verifiche</strong> con il direttore dei lavori e il collaudatore fin dalla fase di progetto.</li>
          </ol>"""),
 ],
 "faqs": [
  ("La stampa 3D si può usare anche per ristrutturare edifici esistenti?",
   "Sì, ma con ruoli diversi dalla nuova costruzione: gli impieghi documentati sull'esistente riguardano elementi non strutturali, componenti di facciata, arredi urbani e manufatti prefabbricati stampati off-site e poi posati. Per interventi strutturali su edifici esistenti la stampa in sito resta sperimentale e richiede validazione caso per caso."),
 ],
}

CFG["tecnologie-innovazione/intelligenza-artificiale-cantiere"] = {
 "sections": [
  ("errori-da-evitare", "Gli errori da evitare con l'intelligenza artificiale in cantiere", """
          <p>I progetti IA falliti in edilizia hanno quasi sempre la stessa genealogia. Cinque errori da riconoscere prima di firmare qualunque contratto:</p>
          <ol>
            <li><strong>Partire dalla tecnologia invece che dal problema.</strong> Chi acquista «l'IA» senza aver definito un obiettivo misurabile — ridurre i near-miss, tagliare i ritardi di consegna materiali, automatizzare i verbali — finisce per pagare dashboard che nessuno guarda.</li>
            <li><strong>Comprare sistemi predittivi senza dati storici.</strong> Gli algoritmi di previsione imparano dagli storici di commessa: un'impresa che non registra avanzamenti, ore e costi in modo strutturato non ha nulla da dare in pasto al modello. Prima si digitalizzano i processi, poi si predice.</li>
            <li><strong>Installare videosorveglianza senza iter privacy.</strong> Le telecamere sui lavoratori richiedono accordo sindacale o autorizzazione dell'Ispettorato Nazionale del Lavoro, valutazione d'impatto (DPIA) e informativa ai sensi del GDPR: saltare il passaggio espone a sanzioni che superano il costo del sistema.</li>
            <li><strong>Fidarsi dell'output senza validazione umana.</strong> Un alert di visione artificiale o una stima predittiva non spostano la responsabilità: direttore dei lavori, coordinatori e preposti rispondono delle decisioni, non l'algoritmo.</li>
            <li><strong>Non formare le maestranze.</strong> I sistemi percepiti come controllo vengono boicottati o disattivati; quelli presentati come protezione vengono adottati. La differenza la fa la comunicazione in cantiere, non il software.</li>
          </ol>"""),
  ("caso-pratico", "Caso pratico: la visione artificiale in un lotto autostradale", """
          <p>Un caso documentato del 2026 riguarda un lotto di ammodernamento autostradale nel Centro Italia: commessa da circa <strong>40 milioni di euro</strong>, general contractor nazionale, otto telecamere con visione artificiale posizionate su aree di lavoro e viabilità di cantiere. Il sistema rileva in tempo reale tre eventi: lavoratore senza casco o senza imbracatura sulle lavorazioni in quota, ingresso di personale nelle zone interdette al transito mezzi, distanza di sicurezza non rispettata dai mezzi in movimento.</p>
          <p>I risultati a sei mesi, comunicati dall'impresa in sede di audit: circa <strong>230 near-miss rilevati e analizzati</strong>, zero infortuni con assenza dal lavoro — contro una media di due eventi l'anno su lotti analoghi gestiti in precedenza — e una riduzione dell'8% del premio assicurativo riconosciuta alla scadenza annuale della polizza. Le condizioni che hanno reso il progetto difendibile anche sul piano sindacale: accordo sottoscritto con le rappresentanze prima dell'accensione, dati anonimizzati e aggregati, esplicita esclusione di finalità disciplinari, alert gestiti dai preposti come strumento di prevenzione.</p>
          <p>Lo stesso general contractor sta ora trasferendo il modello sui cantieri di ristrutturazione gestiti con formula integrata, dove la coordinazione tra più squadre è il rischio principale: un approccio che raccontiamo nella guida alla <a href="/ristrutturazioni/ristrutturazione-chiavi-in-mano/">ristrutturazione chiavi in mano</a>.</p>"""),
  ("checklist-operativa", "Checklist operativa per introdurre l'IA in cantiere", """
          <p>Per un'impresa che vuole muoversi senza sprecare budget, la sequenza consigliata:</p>
          <ol>
            <li><strong>Mappare processi e dati disponibili</strong>: cosa si registra già (avanzamenti, presenze, consegne, non conformità) e in che forma.</li>
            <li><strong>Scegliere un solo problema e un solo KPI</strong>: per esempio near-miss rilevati o puntualità delle consegne, con baseline misurata prima dell'intervento.</li>
            <li><strong>Chiudere prima l'iter privacy</strong> per qualunque sistema che tratti immagini o dati dei lavoratori: accordo sindacale o autorizzazione INL, DPIA, informative.</li>
            <li><strong>Fare un pilota di 3 mesi su un cantiere</strong>, con una squadra volontaria e una revisione intermedia dei risultati.</li>
            <li><strong>Formare preposti e maestranze</strong> sul significato degli alert e sul loro uso non disciplinare.</li>
            <li><strong>Misurare e decidere</strong>: si scala solo ciò che ha mosso il KPI; il resto si disattiva senza rimpianti.</li>
            <li><strong>Sfruttare gli obblighi documentali già esistenti</strong> come palestra: i cantieri legati agli incentivi, con fascicoli fotografici e asseverazioni puntuali, sono il terreno ideale per gli assistenti documentali — vedi la guida su <a href="/incentivi-bonus/superbonus-2026-cosa-resta/">cosa resta del Superbonus nel 2026</a>.</li>
          </ol>"""),
 ],
 "faqs": [
  ("L'IA può compilare automaticamente il POS o altri documenti di cantiere?",
   "Gli assistenti generativi possono produrre bozze di POS, verbali, cronoprogrammi e piani di manutenzione a partire da template e dati di commessa, riducendo molto i tempi di redazione. Ma la valutazione dei rischi deve essere puntuale e riferita allo specifico cantiere: la verifica, l'integrazione e la firma restano in capo alle figure qualificate previste dal D.Lgs 81/08."),
 ],
}

CFG["tecnologie-innovazione/top-5-software-bim-edilizia"] = {
 "sections": [
  ("errori-da-evitare", "Gli errori da evitare nella scelta (e nell'acquisto) del software BIM", """
          <p>Le rivendite di software conoscono bene gli errori tipici dei clienti italiani, perché li vedono ripetere ogni anno. I cinque più costosi:</p>
          <ol>
            <li><strong>Scegliere sul prezzo di listino.</strong> Il canone è una frazione del costo reale: formazione, produttività persa nei primi mesi, librerie e hardware pesano più della licenza. Una piattaforma «economica» che rallenta il team costa più di una costosa che lo fa rendere.</li>
            <li><strong>Comprare più postazioni del necessario.</strong> Non tutti modellano a tempo pieno: abbonamenti named user per i modellatori e licenze viewer o condivise per chi consulta riducono il parco licenze anche del 30–40%.</li>
            <li><strong>Ignorare la certificazione IFC.</strong> L'esportazione IFC «di marca» non basta: verificare la certificazione buildingSMART della versione specifica e fare un test di round-trip con i partner abituali prima dell'acquisto.</li>
            <li><strong>Cambiare piattaforma nel mezzo di una commessa pubblica.</strong> La migrazione dei modelli è quasi sempre perdente: si chiude la commessa con lo strumento dichiarato in gara, la transizione si pianifica sulle commesse successive.</li>
            <li><strong>Non leggere i capitolati informativi delle gare a cui si punta.</strong> Se le stazioni appaltanti del proprio mercato richiedono determinati formati e flussi, la scelta del software parte da lì, non dalle preferenze del team.</li>
          </ol>"""),
  ("caso-pratico", "Caso pratico: uno studio di 8 persone cambia piattaforma in sei mesi", """
          <p>Studio associato di progettazione di Genova, otto persone, storia ventennale di CAD 2D: nel 2025 decide il passaggio al BIM per non restare fuori dagli appalti pubblici sopra soglia, che nel suo bacino — scuole, edilizia sanitaria ligure — sono la metà della domanda. La shortlist iniziale include tre piattaforme; la scelta cade sullo standard di mercato per compatibilità con i partner di RTI e con i capitolati informativi più diffusi nella regione.</p>
          <p>Il piano reale, raccontato dal socio che l'ha guidato: <strong>due postazioni complete</strong> per i modellatori senior, due licenze di consultazione per gli altri, corso certificato di 80 ore per quattro persone e affiancamento sul primo progetto. Primo passo non una gara, ma la <strong>rimodellazione di una scuola già consegnata</strong> come progetto pilota interno: servita a costruire template, librerie di oggetti e procedure di denominazione. Costo complessivo del primo anno, tutto compreso: circa <strong>24.000 euro</strong> tra licenze, formazione, una workstation e consulenza. A nove mesi dall'avvio lo studio vince la prima gara pubblica con requisiti BIM, dove l'offerta di gestione informativa vale 8 punti su 100: abbastanza per ribaltare la graduatoria.</p>
          <p>La lezione: il ritorno non arriva dalla licenza, ma dalle pratiche digitali che la licenza abilita — computi, tavole e documenti per i titoli edilizi prodotti dal modello, come quelli descritti nella guida su <a href="/ristrutturazioni/ristrutturare-casa-permessi-cila-scia/">permessi, CILA e SCIA</a>, e le asseverazioni richieste dagli incentivi, di cui parliamo in <a href="/incentivi-bonus/superbonus-2026-cosa-resta/">cosa resta del Superbonus 2026</a>.</p>"""),
  ("checklist-operativa", "Checklist operativa prima di firmare l'abbonamento", """
          <p>Sei verifiche che costano poco e prevengono pentimenti pluriennali:</p>
          <ol>
            <li><strong>Demo su un progetto reale dello studio</strong>, non sui file dimostrativi del produttore: è l'unico test che misura la curva di apprendimento vera.</li>
            <li><strong>Test di interoperabilità</strong>: esportare un modello IFC e riaprirlo negli strumenti dei partner abituali (model checker, CDE, software strutturali).</li>
            <li><strong>Preventivo a tre anni</strong>: canoni, rinnovi workstation, formazione di ingresso e aggiornamenti, per confrontare il costo totale e non la rata.</li>
            <li><strong>Piano di formazione scritto</strong>: chi si forma, quante ore, con quale certificazione finale e quale affiancamento sul primo progetto.</li>
            <li><strong>Exit strategy sui dati</strong>: i modelli restano accessibili in formato aperto anche se si cambia fornitore? La risposta deve essere nel contratto, non nelle promesse.</li>
            <li><strong>Verifica dei requisiti hardware</strong>: una workstation sottodimensionata annulla i benefici di qualunque software.</li>
          </ol>"""),
 ],
 "faqs": [
  ("Quanto tempo serve per formare un team a un nuovo software BIM?",
   "Per raggiungere una produttività di base servono indicativamente 3-6 mesi, con 40-80 ore di corso certificato a persona più l'affiancamento sul primo progetto reale. La piena maturità — template aziendali, librerie, procedure consolidate — richiede in genere 12 mesi. Per questo conviene pianificare la transizione tra una commessa e l'altra, mai durante una gara pubblica."),
 ],
}

CFG["normative/direttiva-case-green-cosa-cambia"] = {
 "sections": [
  ("impatto-costi-mercato", "Impatto su costi, mutui e valore degli immobili", """
          <p>La direttiva Case Green non è solo una questione di adempimento: sta già spostando i prezzi. Nelle grandi città italiane il divario di quotazione tra immobili in classe energetica alta e immobili in classe F-G si è allargato nel 2026 a un <strong>10–25%</strong> a parità di zona e tipologia, secondo le principali osservazioni di mercato, e le banche hanno consolidato i <strong>mutui green</strong>: spread ridotti di 0,1–0,3 punti per l'acquisto di immobili in classe A o B o per ristrutturazioni con miglioramento documentato di almeno due classi.</p>
          <p>Sul fronte degli interventi, gli ordini di grandezza per un appartamento tipo restano: 15.000–40.000 euro per un pacchetto completo (cappotto, serramenti, generatore efficiente), riducibili in modo significativo combinando detrazioni e incentivi. La <a href="/efficienza-energetica/pompe-di-calore-come-funzionano/">pompa di calore</a> è diventata il generatore di riferimento nei piani di riqualificazione, proprio perché la direttiva spinge verso l'abbandono delle caldaie a fossile; per gli incentivi sui generatori a rinnovabili il riferimento 2026 è il <a href="/incentivi-bonus/conto-termico-3-guida/">Conto Termico 3.0</a>. La lettura economica è semplice: più il recepimento italiano si avvicina, più la classe energetica diventa una variabile finanziaria dell'immobile, non solo tecnica.</p>"""),
  ("errori-da-evitare", "Gli errori da evitare (e le paure infondate)", """
          <p>Intorno alla direttiva circolano allarmismi e sottovalutazioni in parti uguali. Quattro errori da non commettere:</p>
          <ol>
            <li><strong>«Dal 2030 non potrò più vendere casa».</strong> Falso: la direttiva non introduce alcun divieto di vendita per le classi energetiche basse. Le tappe 2030-2033 riguardano standard minimi per il non residenziale e obiettivi nazionali di riduzione dei consumi, non rogiti individuali.</li>
            <li><strong>«Le caldaie a gas vanno rottamate subito».</strong> Falso anche questo: dal 2025 sono cessati gli incentivi all'acquisto di caldaie a combustibile fossile, e il dibattito europeo fissa al 2040 il possibile stop alla vendita di nuove caldaie a gas. Le caldaie esistenti restano legittime fino a fine vita.</li>
            <li><strong>Aspettare il decreto attuativo per muoversi.</strong> Chi ha in programma lavori rilevanti — ristrutturazione, sostituzione del generatore, rifacimento della copertura — farebbe bene a pianificarli ora: le ristrutturazioni importanti attivano obblighi e opportunità (solare, standard minimi) indipendentemente dai dettagli del recepimento.</li>
            <li><strong>Riqualificare senza diagnosi.</strong> Interventi scollegati — la caldaia nuova oggi, il cappotto forse domani, i serramenti chissà — sprecano soldi e classi energetiche: la sequenza giusta la stabilisce una diagnosi energetica, non l'offerta del fornitore di turno.</li>
          </ol>"""),
  ("come-adeguarsi", "Come adeguarsi in pratica: la strategia per i proprietari", """
          <p>Per i proprietari di casa la risposta sensata alla direttiva è una strategia a step, non un panico da titolo di giornale. La sequenza consigliata:</p>
          <ol>
            <li><strong>Fotografare il punto di partenza</strong> con un'APE aggiornata: è il documento su cui si misureranno incentivi, mutui e standard futuri.</li>
            <li><strong>Commissionare una diagnosi energetica</strong> che ordini gli interventi per rapporto costo/beneficio: isolamento e serramenti prima, generatore e rinnovabili dopo, domotica a completamento.</li>
            <li><strong>Costruire un piano a 3-5 anni</strong> sincronizzato con scadenze naturali (fine vita della caldaia, rifacimento facciate, ristrutturazioni già previste).</li>
            <li><strong>Massimizzare gli incentivi disponibili</strong> anno per anno, verificando requisiti e cumulabilità prima di aprire il cantiere.</li>
            <li><strong>Valutare il solare</strong> in occasione di qualunque intervento sul tetto: l'obbligo progressivo rende l'installazione comunque una scelta anticipata, non evitabile.</li>
            <li><strong>Monitorare il recepimento</strong>: i decreti attuativi italiani definiranno soglie, sanzioni e incentivi nazionali tra il 2026 e il 2027.</li>
          </ol>"""),
  ("caso-pratico", "Caso pratico: un condominio anni '70 a Torino verso la classe B", """
          <p>Condominio di 24 unità nella prima cintura di Torino, costruzione del 1974, classe energetica G, riscaldamento centralizzato a gasolio. Nell'assemblea del 2025 l'amministratore propone un piano pluriennale costruito sulla diagnosi energetica: cappotto da 12 cm sulle facciate, sostituzione della centrale con <strong>pompa di calore centralizzata ad alta temperatura</strong>, impianto fotovoltaico da 40 kW sulla copertura — intervento che la direttiva rende comunque obbligatorio, trattandosi di ristrutturazione rilevante.</p>
          <p>I numeri del piano approvato nel 2026: investimento complessivo di circa <strong>950.000 euro</strong>, coperto da Conto Termico per il generatore, detrazioni per l'involucro e finanziamento condominiale agevolato per la quota residua. Risultati attesi e verificati a progetto: salto dalla classe G alla <strong>classe B</strong>, riduzione delle spese di riscaldamento del 55%, rivalutazione media stimata degli appartamenti intorno al 18% secondo le quotazioni di zona. Il cantiere è partito nella primavera 2026 con consegna prevista a fine 2027: un esempio concreto di come la direttiva, letta bene, sia un piano di valorizzazione e non una minaccia.</p>"""),
 ],
 "faqs": [
  ("La direttiva Case Green farà perdere valore alle case in classe G?",
   "La direttiva non prevede divieti di vendita né espropri per le classi energetiche basse. Tuttavia il mercato si sta già muovendo: nelle grandi città il divario di prezzo tra immobili efficienti e immobili in classe F-G ha raggiunto il 10-25%, e i mutui green premiano le classi alte. Chi possiede un immobile energivoro ha interesse a pianificare la riqualificazione sfruttando gli incentivi, prima che il divario si allarghi ulteriormente."),
 ],
}

CFG["normative/sicurezza-cantiere-dlgs-81"] = {
 "sections": [
  ("errori-da-evitare", "Gli errori più frequenti (e più sanzionati) nei cantieri", """
          <p>Le statistiche dell'Ispettorato Nazionale del Lavoro mostrano una fotografia stabile: le violazioni più contestate nei cantieri italiani riguardano ponteggi, lavori in quota, scavi e documentazione. Gli errori che ricorrono con più frequenza — e che costano di più:</p>
          <ol>
            <li><strong>POS fotocopiato.</strong> Un Piano Operativo di Sicurezza uguale per ogni cantiere, non riferito alle lavorazioni reali, è la prima irregolarità rilevata nei controlli: il POS deve descrivere i rischi specifici di quel cantiere, non la teoria generale.</li>
            <li><strong>Ponteggi senza PIMUS aggiornato o montati da personale non formato.</strong> Il ponteggio resta l'opera provvisionale più ispezionata: montaggio, trasformazione e smontaggio richiedono lavoratori formati e autorizzati.</li>
            <li><strong>DUVRI assente con più imprese in cantiere.</strong> Quando il coordinatore non è obbligatorio ma le imprese si interferiscono, il documento sui rischi da interferenza resta dovuto: la sua assenza è tra le contestazioni più frequenti nelle ristrutturazioni.</li>
            <li><strong>DPI generici o scaduti.</strong> Dispositivi non idonei alla lavorazione, non revisionati o non indossati: la verifica spetta al datore di lavoro e al preposto, con responsabilità personali.</li>
            <li><strong>Notifica preliminare dimenticata.</strong> Sopra i 200 uomini-giorno o con lavorazioni a rischio particolare, la notifica ad ASL e Ispettorato va trasmessa prima dell'apertura: la dimenticanza costa la sospensione.</li>
          </ol>
          <p>Vale la pena ricordare che questi adempimenti non si sospendono nei cantieri legati agli incentivi fiscali: anche chi apre un cantiere per il <a href="/incentivi-bonus/bonus-ristrutturazione-2026-guida/">bonus ristrutturazione 2026</a> resta pienamente dentro il Titolo IV.</p>"""),
  ("caso-pratico", "Caso pratico: un controllo ispettivo in una ristrutturazione a Milano", """
          <p>Primavera 2026, ristrutturazione integrale di un appartamento in un condominio anni '60 a Milano: impresa affidataria più due subappalti (impianti e cartongessi), committente privato. Il controllo dell'Ispettorato arriva su segnalazione e trova tre irregolarità tipiche: <strong>DUVRI mai redatto</strong> nonostante le interferenze quotidiane tra le squadre, ponteggio sul fronte strada con PIMUS non aggiornato dopo una modifica di assetto, un lavoratore del subappaltatore privo di formazione specifica documentata.</p>
          <p>L'esito, ricostruito dagli atti: <strong>sospensione immediata delle lavorazioni in quota</strong> e ripristino solo dopo la regolarizzazione, sanzioni complessive intorno ai 12.000 euro a carico dell'impresa affidataria e del subappaltatore, decurtazione di punteggio sulla patente a crediti dell'impresa e iscrizione del verbale a carico del datore di lavoro. Il cantiere è ripartito dopo nove giorni, con un costo indiretto — fermo squadre, penali sul cronoprogramma, rapporto con il committente — superiore alle sanzioni stesse. L'episodio fotografa una regola che i privati faticano a interiorizzare: anche chi affida i lavori con formula integrata resta committente, con obblighi propri, come spieghiamo nella guida alla <a href="/ristrutturazioni/ristrutturazione-chiavi-in-mano/">ristrutturazione chiavi in mano</a>.</p>"""),
  ("domande-cantiere", "Domande dal cantiere: i dubbi più comuni di imprese e committenti", """
          <p>Dalle caselle di posta della redazione e dai corsi di formazione emergono domande ricorrenti che meritano risposte nette:</p>
          <ul>
            <li><strong>Il ponteggio sul marciapiede richiede altri permessi?</strong> Sì: l'occupazione di suolo pubblico va autorizzata dal Comune, con segnaletica e misure per la sicurezza dei pedoni previste dal PSC o dal POS.</li>
            <li><strong>Il lavoratore autonomo deve fare il POS?</strong> No: il POS spetta alle imprese esecutrici; il lavoratore autonomo deve però attestare l'idoneità delle proprie attrezzature e l'aggiornamento della propria formazione, oltre a rispettare le misure di coordinamento del cantiere.</li>
            <li><strong>Chi tiene le schede dei DPI?</strong> Il datore di lavoro, con il registro di consegna firmato: in caso di controllo, la mancata consegna documentata equivale alla mancata fornitura.</li>
            <li><strong>Il preposto va formato ogni anno?</strong> La formazione del preposto prevede aggiornamento quinquennale, ma molti contratti collettivi e procedure aziendali anticipano richiami più frequenti: è una best practice, non un obbligo annuale.</li>
            <li><strong>Il committente privato può essere sanzionato?</strong> Sì: se non nomina il coordinatore quando dovuto, non verifica l'idoneità delle imprese o non trasmette la notifica preliminare nei casi previsti, risponde in prima persona.</li>
          </ul>"""),
 ],
 "faqs": [
  ("Serve il POS anche per un cantiere di pochi giorni?",
   "Sì: il Piano Operativo di Sicurezza è obbligatorio per ogni impresa esecutrice a prescindere dalla durata e dalle dimensioni del cantiere, compresa la singola giornata di lavoro. La complessità del documento si modula sull'attività svolta, ma la sua assenza è sanzionata sempre. Per il lavoratore autonomo il POS non è dovuto, ma restano gli obblighi su attrezzature e formazione."),
 ],
}

CFG["normative/ntc-norme-tecniche-costruzioni"] = {
 "sections": [
  ("errori-da-evitare", "Gli errori da evitare nell'applicazione delle NTC", """
          <p>Le controparti tecniche e gli uffici del Genio Civile conoscono bene gli errori ricorrenti della progettazione italiana. I cinque che generano più contenziosi e bocciature:</p>
          <ol>
            <li><strong>Confondere la ristrutturazione con l'intervento strutturale.</strong> Aprire un vano in una parete portante, sopraelevare o irrigidire un solaio non sono «lavori interni»: modificano il comportamento strutturale e richiedono progetto e deposito secondo le NTC.</li>
            <li><strong>Prescrivere materiali non qualificati.</strong> Calcestruzzi, acciai e connettori devono rispondere alle norme di prodotto richiamate dalle NTC, con certificazioni di fabbrica e controlli di accettazione: le schede commerciali non bastano.</li>
            <li><strong>Sottovalutare le indagini geotecniche.</strong> La relazione geologica è obbligatoria per le opere nuove e per molti interventi sull'esistente: fondazioni dimensionate «a esperienza» sono tra le cause più frequenti di lesioni e contenziosi.</li>
            <li><strong>Modellare la sismica senza vita nominale e classe d'uso corrette.</strong> I parametri spettrali dipendono da queste scelte iniziali: un errore qui invalida l'intera analisi.</li>
            <li><strong>Saltare o banalizzare il collaudo statico.</strong> Dove obbligatorio, il collaudo è condizione di agibilità dell'opera: rinunciarvi per risparmiare espone il committente a responsabilità dirette.</li>
          </ol>"""),
  ("caso-pratico", "Caso pratico: il deposito strutturale di un ampliamento in zona sismica 2", """
          <p>Un caso ordinario ma istruttivo: ampliamento di <strong>40 mq</strong> di una villetta unifamiliare in provincia dell'Aquila, zona sismica 2, struttura esistente in muratura portante degli anni Ottanta. L'iter seguito nel 2026, con i tempi reali:</p>
          <ol>
            <li><strong>Indagini geotecniche</strong>: due prove penetrometriche e relazione del geologo — costo circa 2.500 euro, tre settimane.</li>
            <li><strong>Progetto strutturale</strong>: modellazione dell'esistente e dell'ampliamento, verifiche locali sulle murature, fondazioni nuove collegate alle esistenti con barre chimiche — parcelle tra 6.000 e 9.000 euro in questa fascia di intervento.</li>
            <li><strong>Deposito al Genio Civile</strong>: istanza digitale, esame concluso in circa 75 giorni senza integrazioni — sotto la media, merito di una relazione geotecnica completa.</li>
            <li><strong>Direzione lavori e collaudo</strong>: direttore dei lavori strutturali nominato dal committente, collaudatore statico incaricato a lavori ultimati, certificato di collaudo depositato insieme all'aggiornamento catastale.</li>
          </ol>
          <p>Durata complessiva della parte autorizzativa: poco più di tre mesi, da sommare al titolo edilizio comunale — SCIA in questo caso — di cui parliamo nella guida su <a href="/ristrutturazioni/ristrutturare-casa-permessi-cila-scia/">permessi, CILA e SCIA per ristrutturare</a>. La lezione pratica: i tempi del Genio Civile si comprimono con la qualità della documentazione, non con le sollecitazioni. E per chi valuta interventi migliorativi sismici sugli incentivi, il riferimento è la guida su <a href="/incentivi-bonus/superbonus-2026-cosa-resta/">cosa resta del Superbonus nel 2026</a>.</p>"""),
  ("impatto-costi", "Quanto incidono le NTC sui costi di costruzione", """
          <p>Le NTC non sono un costo accessorio: strutturano una quota rilevante del prezzo di costruzione. Gli ordini di grandezza per l'edilizia residenziale italiana 2026:</p>
          <div class="table-wrap">
          <table>
            <caption>Tabella 2 — Incidenza indicativa delle voci legate alle NTC sul costo di un edificio residenziale nuovo</caption>
            <thead>
              <tr><th>Voce</th><th>Incidenza sul costo totale</th><th>Note</th></tr>
            </thead>
            <tbody>
              <tr><td>Strutture portanti (fondazioni + elevazioni)</td><td>25–35%</td><td>Cresce in zona sismica 1-2 e su terreni difficili</td></tr>
              <tr><td>Indagini geotecniche e relazione geologica</td><td>0,3–1%</td><td>1.500–4.000 euro per lotti ordinari</td></tr>
              <tr><td>Progettazione strutturale e DL</td><td>2–4%</td><td>Parcelle professionali su importo lavori strutture</td></tr>
              <tr><td>Collaudo statico</td><td>0,5–1%</td><td>Quando obbligatorio per legge</td></tr>
            </tbody>
          </table>
          </div>
          <p>Rispetto a un Paese non sismico, i requisiti antisismici italiani aggiungono indicativamente un <strong>5–10%</strong> al costo delle strutture: acciai e staffature più densi, gerarchie delle resistenze, dettagli costruttivi più onerosi. È il prezzo della riduzione del rischio, e i dati post-sisma degli ultimi decenni mostrano che è un premio assicurativo collettivo tra i più efficienti: gli edifici progettati con le NTC moderne hanno tenuto, quelli anteriori no. Per chi valuta i materiali con cui queste prestazioni si ottengono, il riferimento è la guida alle <a href="/materiali-costruzione/calcestruzzo-tipologie-usi/">tipologie di calcestruzzo e ai loro impieghi</a>.</p>"""),
 ],
 "faqs": [
  ("Le NTC si applicano anche al cambio di destinazione d'uso di un edificio esistente?",
   "Sì, quando il cambio comporta aumento dei carichi o una classe d'uso più severa (per esempio da abitazione a ufficio aperto al pubblico o a scuola): serve la valutazione di sicurezza della struttura esistente e, nei casi previsti, il deposito al Genio Civile con gli eventuali interventi di adeguamento. Se invece carichi e classe d'uso non peggiorano, il cambio è di competenza comunale e non attiva le NTC strutturali."),
 ],
}

CFG["normative/certificazione-ape-guida"] = {
 "sections": [
  ("errori-da-evitare", "Gli errori da evitare con la certificazione APE", """
          <p>L'APE è diventata un documento da poche centinaia di euro che muove trattative da centinaia di migliaia: trattarla come un adempimento di peso è l'errore più diffuso. Gli altri quattro:</p>
          <ol>
            <li><strong>Scegliere il prezzo più basso senza sopralluogo.</strong> Un attestato redatto «a tavolino», senza visita all'immobile, è irregolare: il certificatore rischia sanzioni e il proprietario si ritrova un documento contestabile in sede di rogito o di controllo regionale.</li>
            <li><strong>Non verificare l'accreditamento del certificatore.</strong> Ogni regione tiene l'elenco dei certificatori abilitati: la verifica richiede due minuti e mette al riparo da attestati non registrabili.</li>
            <li><strong>Dimenticare l'aggiornamento dopo i lavori.</strong> Cappotto, nuovo generatore, serramenti: ogni intervento che modifica la prestazione energetica rende l'APE precedente non più rappresentativa, e la vendita con attestato incoerente espone a contestazioni. Chi ha sostituito la caldaia con una <a href="/efficienza-energetica/pompe-di-calore-come-funzionano/">pompa di calore</a> ha spesso due classi in più da certificare.</li>
            <li><strong>Presentarsi al rogito con l'APE scaduta o incoerente.</strong> Superati i dieci anni, o con dati difformi dallo stato dei luoghi, l'atto resta valido ma l'acquirente può agire per il rimborso dei costi e la trattativa si complica.</li>
            <li><strong>Ignorare la sezione degli interventi raccomandati.</strong> È la parte più preziosa per acquirenti e venditori: elenca gli interventi migliorativi con la stima del salto di classe, ed è la base su cui si negoziano prezzo e mutui green.</li>
          </ol>"""),
  ("caso-pratico", "Caso pratico: vendere un trilocale con l'APE scaduta", """
          <p>Milano, trilocale di 85 mq in palazzo anni '60, vendita avviata nella primavera 2026. Il proprietario recupera l'APE del 2014 — scaduta da due anni — e scopre che la classe era F. Il nuovo certificatore, accreditato presso il catasto energetico regionale, esegue il sopralluogo in un'ora: caldaia autonoma del 2010, serramenti originali in legno con vetro singolo, nessun isolamento. Il calcolo assegna <strong>classe E</strong> (l'involucro un po' migliore del previsto), con indice EPgl,nren di 165 kWh/mq anno.</p>
          <p>È la sezione dei raccomandati a cambiare la trattativa: sostituzione della caldaia con pompa di calore e serramenti a taglio termico porterebbero l'appartamento in <strong>classe C</strong>, con costo stimato intorno ai 25.000 euro — in parte recuperabile con il <a href="/incentivi-bonus/conto-termico-3-guida/">Conto Termico 3.0</a> e le detrazioni. L'acquirente usa quei numeri per negoziare uno sconto di 12.000 euro sul prezzo, il venditore accetta perché il documento rende il conto trasparente. Costo dell'operazione documentale: <strong>280 euro</strong> comprensivi di sopralluogo e diritti di registrazione, consegna in cinque giorni. La morale: un'APE fatta bene non è un costo, è uno strumento di pricing.</p>"""),
  ("checklist-operativa", "Checklist operativa prima di chiamare il certificatore", """
          <p>Sei passaggi per ottenere un attestato corretto, registrato e spendibile in trattativa:</p>
          <ol>
            <li><strong>Raccogliere i documenti</strong>: planimetria catastale, visura, libretto di impianto e schede tecniche della caldaia o della pompa di calore, eventuali schede dei serramenti, una bolletta recente.</li>
            <li><strong>Verificare l'accreditamento</strong> del professionista nell'elenco regionale dei certificatori energetici.</li>
            <li><strong>Concordare sempre il sopralluogo</strong>: diffidare dei preventivi che lo escludono o lo offrono «a richiesta».</li>
            <li><strong>Richiedere la stima degli interventi raccomandati</strong> con il salto di classe: è prevista dalle linee guida ed è ciò che dà valore al documento.</li>
            <li><strong>Controllare la registrazione</strong> al catasto energetico regionale e farsi consegnare copia firmata e protocollo di trasmissione.</li>
            <li><strong>Calendarizzare la scadenza</strong>: dieci anni, ma con verifica dopo ogni intervento su involucro o impianti.</li>
          </ol>"""),
 ],
 "faqs": [
  ("In caso di affitto, chi paga l'APE: proprietario o inquilino?",
   "Spetta al proprietario: è lui che deve dotare l'immobile dell'attestato, consegnarlo al conduttore alla stipula del nuovo contratto e sostenerne il costo. L'inquilino ha diritto di ricevere copia dell'APE insieme al contratto, e gli indici energetici devono comparire negli annunci di locazione. In caso di subentro o rinnovo senza modifiche contrattuali, l'attestato già consegnato resta valido fino alla sua scadenza decennale."),
 ],
}

# ---------------------------------------------------------------- engine ----
def make_faq_html(q, a):
    return (f'            <details>\n'
            f'              <summary>{q}</summary>\n'
            f'              <div class="faq-a"><p>{a}</p></div>\n'
            f'            </details>\n')

report = []
for slug, cfg in CFG.items():
    path = BASE + slug + "/index.html"
    s = open(path, encoding="utf-8").read()
    orig = s

    # ---- before metrics
    m = re.search(r'<div class="article-body" itemprop="articleBody">(.*?)<!-- Box autore', s, re.S)
    before_txt = strip(m.group(1))
    chars_before, words_before = len(before_txt), len(before_txt.split())

    # ---- 1. insert sections before <h2 id="faq">
    sections_html = ""
    for sid, title, body in cfg["sections"]:
        sections_html += f'\n          <h2 id="{sid}">{title}</h2>\n{body}\n'
    idx = s.index('<h2 id="faq">')
    line_start = s.rindex("\n", 0, idx) + 1
    s = s[:line_start] + sections_html.lstrip("\n") + "\n" + s[line_start:]

    # ---- 2. TOC items before FAQ entry
    toc_items = ""
    for sid, title, _ in cfg["sections"]:
        toc_items += f'              <li><a href="#{sid}">{title}</a></li>\n'
    m = re.search(r'([ \t]*)<li><a href="#faq">', s)
    s = s[:m.start()] + toc_items + s[m.start():]

    # ---- 3. visible FAQs
    if cfg["faqs"]:
        faq_html = "".join(make_faq_html(q, a) for q, a in cfg["faqs"])
        fs = s.index('<div class="faq-section">')
        last_det = s.rindex('</details>', fs)
        end_det = last_det + len('</details>')
        s = s[:end_det] + "\n" + faq_html.rstrip("\n") + s[end_det:]

        # ---- 4. JSON-LD FAQs
        fq_pos = s.index('"@type": "FAQPage"')
        close_idx = s.index("\n        ]", fq_pos)
        new_qs = ""
        for q, a in cfg["faqs"]:
            obj = {"@type": "Question", "name": q,
                   "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            block = json.dumps(obj, ensure_ascii=False, indent=10)
            # indent continuation lines to 10 spaces base
            lines = block.split("\n")
            block = lines[0] + "\n" + "\n".join("          " + l for l in lines[1:])
            new_qs += ",\n          " + block
        s = s[:close_idx] + new_qs + s[close_idx:]

    # ---- 5. dateModified (JSON-LD + meta-bar)
    s = re.sub(r'"dateModified": "[^"]*"', f'"dateModified": "{DATE_MOD}"', s, count=1)
    s = re.sub(r'<time datetime="[^"]*" itemprop="dateModified">[^<]*</time>',
               f'<time datetime="{DATE_MOD}" itemprop="dateModified">{DATE_MOD_TXT}</time>', s, count=1)

    # ---- 6. wordCount + reading time from real content
    m = re.search(r'<div class="article-body" itemprop="articleBody">(.*?)<!-- Box autore', s, re.S)
    after_txt = strip(m.group(1))
    chars_after, words_after = len(after_txt), len(after_txt.split())
    minutes = max(1, round(words_after / 220))
    s = re.sub(r'"wordCount": \d+', f'"wordCount": {words_after}', s, count=1)
    s = re.sub(r'Tempo di lettura: \d+ min', f'Tempo di lettura: {minutes} min', s, count=1)

    # ---- validate JSON-LD
    ld = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', s, re.S)
    json.loads(ld.group(1))

    # ---- validate TOC anchors <-> ids
    tocs = re.findall(r'<li><a href="#([^"]+)">', s)
    ids = set(re.findall(r'<h2 id="([^"]+)"', s))
    missing = [t for t in tocs if t not in ids]
    if missing:
        raise SystemExit(f"{slug}: TOC anchors without target: {missing}")

    # ---- visible FAQ == JSON-LD FAQ
    body_faqs = re.findall(r'<summary>([^<]+)</summary>', m and s or s)
    data = json.loads(ld.group(1))
    for node in data["@graph"]:
        if node.get("@type") == "FAQPage":
            ld_faqs = [q["name"] for q in node["mainEntity"]]
    vis = re.findall(r'<summary>([^<]+)</summary>', s)
    if [html.unescape(v) for v in vis] != [html.unescape(q) for q in ld_faqs]:
        raise SystemExit(f"{slug}: FAQ mismatch visible vs JSON-LD")

    open(path, "w", encoding="utf-8").write(s)
    report.append((slug, chars_before, chars_after, words_before, words_after, minutes,
                   [t for _, t, _ in cfg["sections"]], len(cfg["faqs"])))

print(f'{"articolo":55} {"prima":>7} {"dopo":>7} {"parole":>7} {"min":>4}')
for r in report:
    print(f'{r[0]:55} {r[1]:>7} {r[2]:>7} {r[3]:>4}->{r[4]:<5} {r[5]:>3}m  +{len(r[6])} sez, +{r[7]} FAQ')
