# Quiz Simulatore Patente
# © 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0

import tkinter as tk
from tkinter import messagebox
import platform
import random
from PIL import Image, ImageTk
import os

try:
    if platform.system() == "Windows":
        MODELLO_FONT = 'Segoe UI'
    elif platform.system() == "Linux":
        MODELLO_FONT = "Arial"
    elif platform.system() == "Darwin":
        MODELLO_FONT = "San Francisco"
    else:
        MODELLO_FONT = "Arial"
except Exception as errore:
    MODELLO_FONT = "Arial"

RISOLUZIONE = "1080x720"
FG_COLOR = "black"
BG_COLOR = "white"
PULSANTE_BG_COLOR = "#dddddd"
ACTIVE_PULSANTE_BG_COLOR = "#aaaaaa"
VERO_COLORE = "#16a34a"
ACTIVE_VERO_COLORE = "#15803d"
FALSO_COLORE = "#ef4444"
ACTIVE_FALSO_COLORE = "#dc2626"

TEMPO = 20 * 60

def crea_pulsante_vero(finestra, funzione):
    try:
        return tk.Button(
            finestra,
            text="Vero",
            font=(MODELLO_FONT, 15, "bold"),
            bg=VERO_COLORE,
            fg=BG_COLOR,
            activebackground=ACTIVE_VERO_COLORE,
            activeforeground=BG_COLOR,
            width=12,
            height=2,
            bd=0,
            command=funzione
        )
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore nella creazione del pulsante: {errore}")


def crea_pulsante_falso(finestra, funzione):
    try:
        return tk.Button(
            finestra,
            text="Falso",
            font=(MODELLO_FONT, 15, "bold"),
            bg=FALSO_COLORE,
            fg=BG_COLOR,
            activebackground=ACTIVE_FALSO_COLORE,
            activeforeground=BG_COLOR,
            width=12,
            height=2,
            bd=0,
            command=funzione
        )
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore nella creazione del pulsante: {errore}")


def leggi_domande():
    domande = []
    try:
        with open("support/domande_rev_v6.txt", "r", encoding="utf-8") as file:
            for linea in file:
                parti = linea.strip().split("|")

                if len(parti) >= 2:
                    testo_domanda_attuale = parti[1].strip()
                    risposta = parti[0].strip().upper()
                
                    if len(parti) == 2:
                        domande.append([testo_domanda_attuale, risposta])
                
                    if len(parti) == 3:
                        percorso_immagine = parti[2].strip()
                        domande.append([testo_domanda_attuale, risposta, percorso_immagine])

    except FileNotFoundError:
        messagebox.showerror("Errore", "File delle domande non trovato o danneggiato.")
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore durante la lettura del file: {errore}")
    return domande


def preleva_domande(domande):
    try:
        if len(domande) == 0:
            return []

        # Se ci sono meno di 30 domande, prendile tutte        
        num_domande = min(30, len(domande))
        return random.sample(domande, num_domande)
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore nella presa random delle domande: {errore}")
        return []


def mostra_risultato(finestra, domande, risposte_utente, non_risposte_conta=0):
    try:
        finestra.destroy()
        finestra_schermata_risultato = tk.Tk()
        finestra_schermata_risultato.title("Risultato Quiz Simulatore Patente")
        finestra_schermata_risultato.geometry(RISOLUZIONE)
        finestra_schermata_risultato.resizable(False, False)
        finestra_schermata_risultato.configure(bg=BG_COLOR)
        
        errori = 0
        for i in range(len(domande)):
            if (risposte_utente[i] == None) or (risposte_utente[i].strip() != domande[i][1].strip()):
                errori = errori + 1
 
        if errori <= 3:
            esito_quiz = "PROMOSSO/A"
            colore_esito = VERO_COLORE
        else:
            esito_quiz = "BOCCIATO/A"
            colore_esito = FALSO_COLORE

        scritta_titolo = tk.Label(finestra_schermata_risultato, text="Risultato del Quiz", font=(MODELLO_FONT, 24, "bold"), bg=BG_COLOR, fg=FG_COLOR)
        scritta_titolo.pack(pady=30)
        
        scritta_esito = tk.Label(finestra_schermata_risultato, text=esito_quiz, font=(MODELLO_FONT, 30, "bold"), bg=BG_COLOR, fg=colore_esito)
        scritta_esito.pack(pady=10)
        
        scritta_quantita_errori = tk.Label(finestra_schermata_risultato, text=f"Hai commesso {errori} errori su {len(domande)} domande.", font=(MODELLO_FONT, 18), bg=BG_COLOR, fg=FG_COLOR)
        scritta_quantita_errori.pack(pady=20)

        scritta_domande_non_risposte = tk.Label(finestra_schermata_risultato, text=f"Di questi errori, ci sono {non_risposte_conta} domande senza risposta.", font=(MODELLO_FONT, 18), bg=BG_COLOR, fg=FG_COLOR)
        scritta_domande_non_risposte.pack(pady=10)
        
        pulsante_esci = tk.Button(finestra_schermata_risultato, text="Chiudi Simulatore", font=(MODELLO_FONT, 15), bg=PULSANTE_BG_COLOR, command=finestra_schermata_risultato.destroy, width=20)
        pulsante_esci.pack(pady=40)

        finestra_schermata_risultato.mainloop()
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore nel mostrare il risultato: {errore}")


def schermata_iniziale(finestra, domande):
    try:
        scritta_principale = tk.Label(finestra, text="Benvenuto/a nel Quiz Simulatore Patente", font=(MODELLO_FONT, 24), fg=FG_COLOR, bg=BG_COLOR)
        scritta_principale.pack(pady=20)

        pulsante_inizia_quiz_a_tempo = tk.Button(finestra, 
                                         text="Inizia Prova a Tempo", 
                                         font=(MODELLO_FONT, 14), 
                                         fg=FG_COLOR, 
                                         bg=PULSANTE_BG_COLOR,
                                         bd=0,
                                         activebackground=ACTIVE_PULSANTE_BG_COLOR,
                                         activeforeground=FG_COLOR,
                                         width=18,
                                         height=2,
                                         command=lambda: inizia_quiz(finestra, domande, True))
        pulsante_inizia_quiz_a_tempo.pack(pady=10)

        pulsante_inizia_simulazione = tk.Button(finestra, 
                                         text="Inizia Simulazione", 
                                         font=(MODELLO_FONT, 14), 
                                         fg=FG_COLOR, 
                                         bg=PULSANTE_BG_COLOR,
                                         bd=0,
                                         activebackground=ACTIVE_PULSANTE_BG_COLOR,
                                         activeforeground=FG_COLOR,
                                         width=18,
                                         height=2,
                                         command=lambda: inizia_quiz(finestra, domande, False))
        pulsante_inizia_simulazione.pack(pady=10)

        scritta_crediti = tk.Label(finestra, text="© 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0", font=(MODELLO_FONT, 10), fg=FG_COLOR, bg="#f1f1f1", padx=1000, pady=10)
        scritta_crediti.pack(side=tk.BOTTOM)
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore schermata iniziale: {errore}")


def inizia_quiz(finestra, domande, a_tempo):
    try:
        if len(domande) == 0:
            messagebox.showerror("Errore", "Nessuna domanda disponibile.")
            return

        domande_selezionate = preleva_domande(domande)

        finestra.destroy()
        finestra_quiz = tk.Tk()
        finestra_quiz.title("Quiz Simulatore Patente")
        finestra_quiz.geometry(RISOLUZIONE)
        finestra_quiz.resizable(False, False)
        finestra_quiz.configure(bg=BG_COLOR)

        gestisci_quiz(finestra_quiz, domande_selezionate, a_tempo)
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore inizio quiz: {errore}")


def dividi_testo_domanda(testo):
    elenco_parole_domanda = testo.split(" ")
    nuovo_testo_domanda = ""
    lunghezza_linea_attuale_domanda = 0
    for parola in elenco_parole_domanda:
        if lunghezza_linea_attuale_domanda + len(parola) > 70:
            nuovo_testo_domanda = nuovo_testo_domanda + "\n"
            lunghezza_linea_attuale_domanda = 0
        nuovo_testo_domanda = nuovo_testo_domanda + parola + " "
        lunghezza_linea_attuale_domanda = lunghezza_linea_attuale_domanda + len(parola) + 1
    return nuovo_testo_domanda


def aggiorna_vista(indice_domanda_tkvar, domande, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, risposte_utente):
    try:
        indice_domanda_attuale = indice_domanda_tkvar.get()
        domanda_corrente = domande[indice_domanda_attuale]
        testo_domanda_attuale = domanda_corrente[0]
        testo_formattato = dividi_testo_domanda(testo_domanda_attuale)
        
        indicatore_numero_di_domanda.config(text=f"Domanda {indice_domanda_attuale + 1} di {len(domande)}")
        testo_domanda.config(text=testo_formattato)

        if len(domanda_corrente) > 2:
            percorso_immagine = domanda_corrente[2]
            try:
                try:
                    immagine_file = Image.open(percorso_immagine)
                    img = ImageTk.PhotoImage(immagine_file)
                except Exception as errore:
                    img = tk.PhotoImage(file=percorso_immagine)

                label_immagine.config(image=img)
                label_immagine.image = img
            except Exception as errore:
                label_immagine.config(image="")
                label_immagine.image = None
        else:
            label_immagine.config(image="")
            label_immagine.image = None
        
        if pulsante_vero != None and pulsante_falso != None:
                if risposte_utente[indice_domanda_attuale] == "V":
                    pulsante_vero.config(bg=ACTIVE_VERO_COLORE, fg="white")
                    pulsante_falso.config(bg=FALSO_COLORE, fg=BG_COLOR)
                elif risposte_utente[indice_domanda_attuale] == "F":
                    pulsante_vero.config(bg=VERO_COLORE, fg=BG_COLOR)
                    pulsante_falso.config(bg=ACTIVE_FALSO_COLORE, fg="white")
                else:
                    pulsante_vero.config(bg=VERO_COLORE, fg=BG_COLOR)
                    pulsante_falso.config(bg=FALSO_COLORE, fg=BG_COLOR)

    except Exception as errore:
        messagebox.showerror("Errore", f"Errore aggiornamento vista: {errore}")


def set_risposta(risp, indice_domanda_tkvar, risposte_utente, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, domande):
    try:
        indice_corrente = indice_domanda_tkvar.get()
        risposte_utente[indice_corrente] = risp
        aggiorna_vista(indice_domanda_tkvar, domande, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, risposte_utente)
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore risposta: {errore}")


def vai_indietro(indice_domanda_tkvar, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, domande, risposte_utente):
    try:
        indice_attuale = indice_domanda_tkvar.get()
        if indice_attuale > 0:
            nuovo_indice = indice_attuale - 1
            indice_domanda_tkvar.set(nuovo_indice)
            aggiorna_vista(indice_domanda_tkvar, domande, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, risposte_utente)
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore navigazione: {errore}")


def vai_avanti(indice_domanda_tkvar, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, domande, risposte_utente):
    try:
        indice_attuale = indice_domanda_tkvar.get()
        limite_domande = len(domande) - 1
        if indice_attuale < limite_domande:
            nuovo_indice = indice_attuale + 1
            indice_domanda_tkvar.set(nuovo_indice)
            aggiorna_vista(indice_domanda_tkvar, domande, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, risposte_utente)
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore navigazione: {errore}")


def aggiorna_timer(tempo_gui, timer_id_gui, label_timer, finestra, domande, risposte_utente):
    try:
        tempo_rimanente = tempo_gui.get()
        if tempo_rimanente > 0:
            minuti = tempo_rimanente // 60
            secondi = tempo_rimanente % 60
            stringa_timer = f"Tempo rimanente: {minuti:02d}:{secondi:02d}"
            label_timer.config(text=stringa_timer)
            
            nuovo_tempo = tempo_rimanente - 1
            tempo_gui.set(nuovo_tempo)
            
            timer_id = finestra.after(1000, lambda: aggiorna_timer(tempo_gui, timer_id_gui, label_timer, finestra, domande, risposte_utente))
            timer_id_gui.set(timer_id)
        else:
            messagebox.showinfo("Tempo scaduto", "Il tempo è scaduto! Il quiz verrà consegnato automaticamente.")
            mostra_risultato(finestra, domande, risposte_utente)
    except Exception as errore:
        pass


def consegna(finestra, risposte_utente, domande):
    try:
        non_risposte_conta = risposte_utente.count(None)
        mostra_risultato(finestra, domande, risposte_utente, non_risposte_conta)
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore consegna: {errore}")


def gestisci_quiz(finestra, domande, a_tempo):
    try:
        indice_domanda_tkvar = tk.IntVar(value=0)
        tempo_gui = tk.IntVar(value=TEMPO)
        timer_id_gui = tk.StringVar(value="")
        
        risposte_utente = [None] * len(domande)

        frame_principale = tk.Frame(finestra, bg=BG_COLOR)
        frame_principale.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        frame_principale.columnconfigure(0, weight=1)
        frame_principale.columnconfigure(1, weight=1)
        frame_principale.columnconfigure(2, weight=1)
        
        indicatore_numero_di_domanda = tk.Label(frame_principale, text="", font=(MODELLO_FONT, 14, "bold"), bg=BG_COLOR, fg=FG_COLOR)
        indicatore_numero_di_domanda.grid(row=0, column=0, sticky="w", pady=10)
        
        label_timer = tk.Label(frame_principale, text="", font=(MODELLO_FONT, 14, "bold"), bg=BG_COLOR, fg=FALSO_COLORE)
        if a_tempo == True:
            label_timer.grid(row=0, column=2, sticky="e", pady=10)

        testo_domanda = tk.Label(frame_principale, text="", font=(MODELLO_FONT, 18), fg=FG_COLOR, bg=BG_COLOR, justify="center", wraplength=800)
        testo_domanda.grid(row=1, column=0, columnspan=3, pady=(20, 10))

        label_immagine = tk.Label(frame_principale, bg=BG_COLOR, height=6)
        label_immagine.grid(row=2, column=0, columnspan=3, pady=10)
        
        pulsante_vero = crea_pulsante_vero(frame_principale, lambda: set_risposta("V", indice_domanda_tkvar, risposte_utente, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, domande))
        if pulsante_vero != None:
            pulsante_vero.grid(row=3, column=0, sticky="e", padx=30, pady=20)
        
        pulsante_falso = crea_pulsante_falso(frame_principale, lambda: set_risposta("F", indice_domanda_tkvar, risposte_utente, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, domande))
        if pulsante_falso != None:
            pulsante_falso.grid(row=3, column=2, sticky="w", padx=30, pady=20)

        pulsante_domanda_precedente = tk.Button(frame_principale, 
                                                text="Indietro", 
                                                font=(MODELLO_FONT, 14), 
                                                bg=PULSANTE_BG_COLOR, 
                                                command=lambda: vai_indietro(indice_domanda_tkvar, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, domande, risposte_utente), 
                                                width=12)
        pulsante_domanda_precedente.grid(row=4, column=0, sticky="w", pady=20)
        
        pulsante_consegna_quiz = tk.Button(frame_principale, 
                                            text="Consegna", 
                                            font=(MODELLO_FONT, 14, "bold"), 
                                            bg="#3b82f6", 
                                            fg="white", 
                                            command=lambda: consegna(finestra, risposte_utente, domande), 
                                            width=12)
        pulsante_consegna_quiz.grid(row=4, column=1, pady=20)
        
        pulsante_domanda_successiva = tk.Button(frame_principale, 
                                                text="Avanti", 
                                                font=(MODELLO_FONT, 14), 
                                                bg=PULSANTE_BG_COLOR, 
                                                command=lambda: vai_avanti(indice_domanda_tkvar, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, domande, risposte_utente), 
                                                width=12)
        pulsante_domanda_successiva.grid(row=4, column=2, sticky="e", pady=20)

        aggiorna_vista(indice_domanda_tkvar, domande, indicatore_numero_di_domanda, testo_domanda, label_immagine, pulsante_vero, pulsante_falso, risposte_utente)
        
        if a_tempo == True:
            aggiorna_timer(tempo_gui, timer_id_gui, label_timer, finestra, domande, risposte_utente)
            
    except Exception as errore:
        messagebox.showerror("Errore", f"Errore gestore quiz: {errore}")