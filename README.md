# Osservatorio dei falsi sconti

Ogni mese, quante offerte di elettronica ed elettrodomestici presentate come sconti nei volantini delle catene italiane costano meno in un negozio online, quante costano più o meno uguale e quante convengono davvero in volantino.

I dati vengono dall'[Osservatorio dei falsi sconti](https://www.prezzinvista.it/falsi-sconti/) di [Prezzi in Vista](https://www.prezzinvista.it/), che legge i volantini ufficiali delle catene il giorno in cui escono. Questo repository ne conserva una copia, aggiornata ogni mattina.

**Un esempio, ottobre 2026:** 938 offerte scontate confrontate. Il 33% costava meno online e il 41% costava meno in volantino; per il 26% il prezzo era simile. In 129 casi lo sconto era battuto da almeno due negozi online diversi. I numeri di ogni mese, catena per catena, sono nella [pagina del mese](https://www.prezzinvista.it/falsi-sconti/2026-10/).

## I file

| File | Che cosa c'è |
|---|---|
| [`data/falsi-sconti.json`](data/falsi-sconti.json) | Il file completo: definizioni, e per ogni mese riepilogo, imbuto, catene e casi |
| [`data/mesi.csv`](data/mesi.csv) | Un mese per riga: offerte confrontate, quote online / volantino / simili, sconti battuti |
| [`data/catene.csv`](data/catene.csv) | Un mese e una catena per riga |
| [`data/casi.csv`](data/casi.csv) | I casi del mese: gli sconti peggiori (`worst_case`) e quelli dove il volantino conviene (`flyer_win`), con il link alla pagina del volantino |
| [`data/black-friday-2026-prezzi.csv`](data/black-friday-2026-prezzi.csv) | [Black Friday 2026](https://www.prezzinvista.it/falsi-sconti/black-friday-2026/): il prezzo di ogni prodotto nei volantini prima del Black Friday e poi in quello del Black Friday |

Le colonne sono spiegate nel campo `definitions` del JSON. Gli importi sono in euro, le date in formato ISO.

## Come si calcola, in breve

- Entrano solo le offerte con il prezzo precedente stampato e con il **codice del modello** stampato nel volantino, quando lo stesso codice compare nell'offerta del negozio online: è l'unico modo per essere certi che sia lo stesso oggetto. Usati e ricondizionati non contano.
- «Costa meno online» vale da 3% in giù rispetto al prezzo del volantino, «costa meno in volantino» da 3% in su.
- «Sconto battuto»: almeno due negozi online diversi ad almeno il 5% in meno, e mai meno di 5 € di differenza. Non dice che il prezzo precedente stampato sia falso: quello non si verifica.
- Lo stesso modello nei volantini di più catene conta una volta sola. Le regole valgono per tutti i mesi, che vengono ricalcolati quando una regola cambia.

Il metodo completo è sulla [pagina dell'osservatorio](https://www.prezzinvista.it/falsi-sconti/#metodo). Le singole offerte dei volantini sono anche nell'[API pubblica](https://www.prezzinvista.it/developers/), senza chiave.

## Licenza e citazione

Dati sotto licenza [CC BY 4.0](LICENSE): si possono ripubblicare, anche in parte e per uso commerciale, citando **Prezzi in Vista** con il link a https://www.prezzinvista.it/falsi-sconti/ (o alla pagina del mese).

Per giornalisti: [stampa e dati](https://www.prezzinvista.it/stampa/). Contatti: redazione@prezzinvista.it

---

## English

Monthly open data on fake discounts in Italian retail flyers: for consumer electronics and home appliances advertised as discounted (with a printed previous price and a printed model code), the share that was cheaper in an online shop, about the same, or cheaper in the flyer. Source: the [Fake Discounts Observatory](https://www.prezzinvista.it/falsi-sconti/) by Prezzi in Vista, which reads the official flyers of Italian chains on the day they are published. The files in `data/` are refreshed every morning by a GitHub Action. Field definitions are in the `definitions` object of the JSON file.

License: CC BY 4.0. Please credit **Prezzi in Vista** with a link to https://www.prezzinvista.it/falsi-sconti/.
