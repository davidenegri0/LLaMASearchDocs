# Open Large Language Model: Ricerca Semantica di Documenti con LLaMa 2

Questo progetto, sviluppato come tesi di laurea da **Davide Negri** presso l'Università degli Studi di Ferrara, presenta un sistema di ricerca documentale di natura semantica. L'obiettivo principale è superare i limiti dei motori di ricerca convenzionali basati su parole chiave (keyword search), permettendo di catalogare e interrogare i documenti in base al **significato intrinseco** del loro contenuto.

---

## 🎯 Obiettivi del Progetto

Il sistema è stato progettato per rispondere a tre esigenze fondamentali:
* **Catalogazione Semantica**: Organizzare i documenti non per termini esatti, ma per concetti, utilizzando rappresentazioni vettoriali note come *embeddings*.
* **Recupero Intelligente**: Effettuare ricerche all'interno del catalogo restituendo i documenti più affini all'argomento richiesto dall'utente.
* **Accessibilità Hardware**: Dimostrare che strumenti avanzati di Intelligenza Artificiale possono operare efficacemente su **dispositivi consumer** (computer di fascia media) utilizzando esclusivamente software open-source.

---

## 🏗️ Architettura del Sistema

L'applicativo è strutturato in tre strati principali per garantire portabilità, modularità e prestazioni:

1.  **Client (GUI)**: Un'interfaccia grafica intuitiva che permette all'utente di inserire query e visualizzare i risultati.
2.  **Server (REST API)**: Il "cervello" del sistema, che gestisce le richieste HTTP, coordina la generazione degli embeddings tramite il modello linguistico e interroga il database.
3.  **Database (Vector DB)**: Un motore di ricerca ottimizzato per la memorizzazione e il recupero di vettori ad alta dimensione.

---

## 🛠️ Tecnologie Utilizzate (Approfondimento)

Per garantire l'efficienza su hardware locale, sono state integrate le seguenti tecnologie:

### 1. LLaMa 2 (7B-chat)
Modello linguistico di nuova generazione sviluppato da **Meta**. La versione da 7 miliardi di parametri (7B) è ottimizzata per il dialogo e la comprensione del contesto. Nel progetto, viene utilizzato come motore di embedding per trasformare testi complessi in vettori numerici che ne rappresentano il significato.

### 2. Quantizzazione a 4-bit e LLaMa.cpp
La **quantizzazione** è una tecnica di compressione che riduce la precisione dei pesi del modello.
* **Vantaggio**: Riduce drasticamente l'occupazione di memoria (da circa 13 GB a soli 3.9 GB per il modello 7B).
* **LLaMa.cpp**: Grazie a questa implementazione in C++, il modello può essere eseguito con alte prestazioni sia su CPU che su GPU consumer, sfruttando formati efficienti come il GGUF.

### 3. Elasticsearch come Vector DB
**Elasticsearch** non è solo un motore di ricerca testuale, ma è configurato qui come database vettoriale.
* **Algoritmo kNN (k-Nearest Neighbors)**: Utilizzato per trovare i "vicini più prossimi" nello spazio vettoriale.
* **Somiglianza dei Coseni**: Una metrica matematica che misura l'angolo tra due vettori (query e documento). Più l'angolo è piccolo (valore vicino a 1), più i contenuti sono semanticamente simili.

### 4. Framework di Sviluppo
* **LangChain**: Un framework fondamentale per orchestrare i workflow dei Large Language Models. Facilita la gestione dei prompt e l'estrazione semplificata degli embeddings.
* **Flask**: Utilizzato per il backend, è un micro-framework Python leggero e flessibile, ideale per esporre le funzionalità del modello tramite API REST.
* **Qt (PyQt/PySide)**: Framework professionale per la creazione della GUI, scelto per la sua natura object-oriented e la facilità di creare interfacce performanti.
* **Docker**: Utilizzato per la containerizzazione di Elasticsearch, garantendo un ambiente isolato e facilmente replicabile.

---

## 🚀 Flusso di Funzionamento

Il processo si divide in due fasi operative:

1.  **Popolazione del Database**:
    * Lo script legge i documenti (es. file CSV con articoli scientifici).
    * LLaMa 2 genera un embedding (vettore) per ogni documento.
    * I vettori e i relativi metadati vengono caricati su Elasticsearch.
2.  **Ricerca Semantica**:
    * L'utente inserisce una domanda nella GUI.
    * Il server genera l'embedding della domanda in tempo reale.
    * Elasticsearch confronta il vettore della domanda con quelli nel database e restituisce i risultati più pertinenti.

---

## 📈 Risultati e Sviluppi Futuri

L'applicativo si è dimostrato funzionale e preciso. Le evoluzioni previste includono:
* **Gestione Asincrona**: Implementazione di processi in background nel client per evitare il "freeze" dell'interfaccia.
* **Coda di Gestione (Queue)**: Ottimizzazione dell'uso della RAM sul server per gestire più richieste contemporaneamente.
* **Metriche Alternative**: Sperimentazione con la distanza euclidea o il prodotto vettoriale per affinare la precisione.

---

**Autore:** Davide Negri  
**Relatore:** Prof. Ing. Mauro Tortonesi  
**Università:** Università degli Studi di Ferrara