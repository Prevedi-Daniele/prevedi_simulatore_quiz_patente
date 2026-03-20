# 🚗 Simulatore Quiz Patente (Python + Tkinter)

Questo progetto consiste nello sviluppo di un simulatore del quiz per la patente A e B realizzato in **Python** utilizzando la libreria **Tkinter** per l'interfaccia grafica.

## 📌 Obiettivo

L'obiettivo dell'applicazione è fornire un ambiente di esercitazione realistico che permetta agli utenti di:

- Allenarsi con domande simili a quelle ufficiali
- Simulare un vero esame di teoria
- Migliorare la propria preparazione in modo interattivo

---

## 🖥️ Funzionamento dell'applicazione

L'applicazione è strutturata in diverse schermate principali.

### 1. 🏠 Schermata Home

È la schermata iniziale del programma.

**Elementi presenti:**
- Titolo dell'applicazione
- Campo di inserimento nome utente
- Pulsanti:
  - ▶️ Simulazione
  - 📝 Esame
  - ❌ Esci

**Funzioni:**
- **Simulazione** → avvia una modalità senza pressione di tempo
- **Esame** → avvia una simulazione reale con timer
- **Esci** → chiude il programma

---

### 2. ❓ Schermata Quiz

Qui vengono mostrate le domande.

**Contenuti:**
- Numero domanda (es. 3/15)
- Testo della domanda
- Eventuale immagine (es. segnali stradali)
- Risposte:
  - ✔️ VERO
  - ❌ FALSO

**Controlli:**
- ⬅️ Domanda precedente
- ➡️ Domanda successiva
- 📤 Invia quiz

**Funzionalità:**
- Navigazione tra le domande
- Possibilità di modificare le risposte
- Visualizzazione delle domande già compilate
- Timer (30 minuti)
- Barra di avanzamento

---

### 3. ⚠️ Conferma Invio

Quando l'utente tenta di consegnare il quiz, appare una finestra di conferma:

> "Sei sicuro di voler consegnare il quiz?"

**Opzioni:**
- ✔️ Sì
- ❌ No

---

### 4. 📊 Risultato Finale

Al termine del quiz viene mostrato un riepilogo.

**Informazioni visualizzate:**
- Nome utente
- Numero risposte corrette
- Numero risposte sbagliate
- Punteggio finale
- Esito:
  - ✅ Esame superato
  - ❌ Esame non superato

**Azioni disponibili:**
- 🔍 Rivedi risposte
- 🏠 Torna alla home
- ❌ Esci


---

## 🧩 Tecnologie Utilizzate

- **Python**
- **Tkinter**

---

## 🛠️ Componenti dell'interfaccia (Tkinter)

L'applicazione utilizza diversi widget:

- `Label` → testi e domande
- `Button` → azioni utente
- `Radiobutton` → selezione Vero/Falso
- `Entry` → inserimento nome
- `Frame` → organizzazione layout
- `Messagebox` → notifiche e conferme

---

## ⏱️ Struttura del Quiz

- Durata totale: **30 minuti**
- Nessun limite per singola domanda
- Risposte:
  - VERO / FALSO
- Possibilità di modificare le risposte fino alla consegna

---

## 🎯 Funzionalità principali

- Salvataggio risposte utente
- Calcolo automatico del punteggio
- Feedback finale
- Interfaccia intuitiva e user-friendly
- Supporto per immagini nelle domande
- Barra di avanzamento del tempo

---

## 🚀 Possibili miglioramenti

- Database di domande
- Statistiche dei risultati
- Modalità multiplayer o sfida
- Salvataggio progressi utente

---

## 📚 Scopo didattico

Questo progetto è pensato come esercizio di:

- Educazione civica (preparazione alla patente)
- Informatica (sviluppo GUI con Python)
