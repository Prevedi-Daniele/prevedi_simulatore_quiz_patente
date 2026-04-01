# Quiz Simulatore Patente
# © 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0

import tkinter as tk
from tkinter import messagebox
import platform
import random

try:
    if platform.system() == "Windows":
        MODELLO_FONT = 'Segoe UI'
    elif platform.system() == "Linux":
        MODELLO_FONT = "Arial"
    elif platform.system() == "Darwin":
        MODELLO_FONT = "San Francisco"
    else:
        MODELLO_FONT = "Arial"
except Exception as e:
    MODELLO_FONT = "Arial"

FG_COLOR = "black"
BG_COLOR = "white"
PULSANTE_BG_COLOR = "#dddddd"
ACT_PULSANTE_BG_COLOR = "#aaaaaa"
VERO_COLORE = "#16a34a"
ACT_VERO_COLORE = "#15803d"
FALSO_COLORE = "#ef4444"
ACT_FALSO_COLORE = "#dc2626"

TEMPO = 20 * 60

def crea_pulsante_vero(finestra, funzione):
    try:
        return tk.Button(
            finestra,
            text="Vero",
            font=(MODELLO_FONT, 15, "bold"),
            bg=VERO_COLORE,
            fg=BG_COLOR,
            activebackground=ACT_VERO_COLORE,
            activeforeground=BG_COLOR,
            width=12,
            height=2,
            bd=0,
            command=funzione
        )
    except Exception as e:
        messagebox.showerror("Errore", f"Errore pulsante: {e}")
        return None


def crea_pulsante_falso(finestra, funzione):
    try:
        return tk.Button(
            finestra,
            text="Falso",
            font=(MODELLO_FONT, 15, "bold"),
            bg=FALSO_COLORE,
            fg=BG_COLOR,
            activebackground=ACT_FALSO_COLORE,
            activeforeground=BG_COLOR,
            width=12,
            height=2,
            bd=0,
            command=funzione
        )
    except Exception as e:
        messagebox.showerror("Errore", f"Errore pulsante: {e}")
        return None


def leggi_domande():
    domande = []
    try:
        with open("support/domande_rev_v5.txt", "r", encoding="utf-8") as file:
            for linea in file:
                parti = linea.strip().split("|")
                if len(parti) >= 2:
                    domanda_testo = parti[1].strip()
                    risposta = parti[0].strip().upper()
                    if len(parti) == 2:
                        domande.append([domanda_testo, risposta])
                    if len(parti) == 3:
                        percorso_immagine = parti[2].strip()
                        domande.append([domanda_testo, risposta, percorso_immagine])

    except FileNotFoundError:
        messagebox.showerror("Errore", "File delle domande non trovato.")
    except Exception as e:
        messagebox.showerror("Errore", f"Errore durante la lettura: {e}")
    return domande


def preleva_domande(domande):
    try:
        if not domande:
            return []
        num_domande = min(30, len(domande))
        return random.sample(domande, num_domande)
    except Exception as e:
        messagebox.showerror("Errore", f"Errore prelievo domande: {e}")
        return []


def mostra_risultato(finestra, domande, risposte_utente):
    try:
        for widget in finestra.winfo_children():
            widget.destroy()
        
        errori = 0
        for i in range(len(domande)):
            if risposte_utente[i] != domande[i][1]:
                errori = errori + 1
 
        if errori <= 3:
            esito = "PROMOSSO/A"
            colore_esito = VERO_COLORE
        else:
            esito = "BOCCIATO/A"
            colore_esito = FALSO_COLORE

        label_titolo = tk.Label(finestra, text="Risultato del Quiz", font=(MODELLO_FONT, 24, "bold"), bg=BG_COLOR, fg=FG_COLOR)
        label_titolo.pack(pady=30)
        
        label_esito = tk.Label(finestra, text=esito, font=(MODELLO_FONT, 30, "bold"), bg=BG_COLOR, fg=colore_esito)
        label_esito.pack(pady=10)
        
        label_errori = tk.Label(finestra, text=f"Hai commesso {errori} errori su {len(domande)} domande.", font=(MODELLO_FONT, 18), bg=BG_COLOR, fg=FG_COLOR)
        label_errori.pack(pady=20)
        
        btn_esci = tk.Button(finestra, text="Chiudi Simulatore", font=(MODELLO_FONT, 15), bg=PULSANTE_BG_COLOR, command=finestra.destroy, width=20)
        btn_esci.pack(pady=40)
    except Exception as e:
        messagebox.showerror("Errore", f"Errore nel mostrare il risultato: {e}")


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
                                         activebackground=ACT_PULSANTE_BG_COLOR,
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
                                         activebackground=ACT_PULSANTE_BG_COLOR,
                                         activeforeground=FG_COLOR,
                                         width=18,
                                         height=2,
                                         command=lambda: inizia_quiz(finestra, domande, False))
        pulsante_inizia_simulazione.pack(pady=10)

        scritta_crediti = tk.Label(finestra, text="© 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0", font=(MODELLO_FONT, 10), fg=FG_COLOR, bg="#f1f1f1", padx=1000, pady=10)
        scritta_crediti.pack(side=tk.BOTTOM)
    except Exception as e:
        messagebox.showerror("Errore", f"Errore schermata iniziale: {e}")


def inizia_quiz(finestra, domande, tempo):
    try:
        if not domande:
            messagebox.showerror("Errore", "Nessuna domanda disponibile.")
            return

        domande_selezionate = preleva_domande(domande)

        finestra.destroy()
        finestra_quiz = tk.Tk()
        finestra_quiz.title("Quiz Simulatore Patente")
        finestra_quiz.geometry("900x600")
        finestra_quiz.resizable(False, False)
        finestra_quiz.configure(bg=BG_COLOR)

        gestisci_quiz(finestra_quiz, domande_selezionate, a_tempo=tempo)
    except Exception as e:
        messagebox.showerror("Errore", f"Errore inizio quiz: {e}")


def gestisci_quiz(finestra, domande, a_tempo):
    try:
        stato = {"indice": 0, "tempo": TEMPO, "timer_id": None}
        risposte_utente = [None] * len(domande)

        frame_top = tk.Frame(finestra, bg=BG_COLOR)
        frame_top.pack(fill=tk.X, pady=20, padx=20)
        
        label_info = tk.Label(frame_top, text="", font=(MODELLO_FONT, 14, "bold"), bg=BG_COLOR, fg=FG_COLOR)
        label_info.pack(side=tk.LEFT)
        
        label_timer = tk.Label(frame_top, text="", font=(MODELLO_FONT, 14, "bold"), bg=BG_COLOR, fg=FALSO_COLORE)
        if a_tempo:
            label_timer.pack(side=tk.RIGHT)

        label_domanda = tk.Label(finestra, text="", font=(MODELLO_FONT, 18), fg=FG_COLOR, bg=BG_COLOR, wraplength=800, justify="center")
        label_domanda.pack(pady=40, expand=True)

        frame_pulsanti = tk.Frame(finestra, bg=BG_COLOR)
        frame_pulsanti.pack(pady=20)

        def set_risposta(risp):
            try:
                risposte_utente[stato["indice"]] = risp
                aggiorna_vista()
            except Exception as e:
                messagebox.showerror("Errore", f"Errore risposta: {e}")

        pulsante_vero = crea_pulsante_vero(frame_pulsanti, lambda: set_risposta("V"))
        if pulsante_vero:
            pulsante_vero.pack(side=tk.LEFT, padx=30)
        
        pulsante_falso = crea_pulsante_falso(frame_pulsanti, lambda: set_risposta("F"))
        if pulsante_falso:
            pulsante_falso.pack(side=tk.RIGHT, padx=30)

        frame_nav = tk.Frame(finestra, bg=BG_COLOR)
        frame_nav.pack(side=tk.BOTTOM, pady=40, fill=tk.X, padx=50)

        def vai_indietro():
            try:
                if stato["indice"] > 0:
                    stato["indice"] -= 1
                    aggiorna_vista()
            except Exception as e:
                messagebox.showerror("Errore", f"Errore navigazione: {e}")

        def vai_avanti():
            try:
                if stato["indice"] < len(domande) - 1:
                    stato["indice"] += 1
                    aggiorna_vista()
            except Exception as e:
                messagebox.showerror("Errore", f"Errore navigazione: {e}")

        def consegna():
            try:
                if stato.get("timer_id"):
                    finestra.after_cancel(stato["timer_id"])
                non_risposte = risposte_utente.count(None)
                if non_risposte > 0:
                    risp = messagebox.askyesno("Attenzione", f"Hai ancora {non_risposte} domande a cui non hai risposto. Vuoi consegnare lo stesso?")
                    if not risp:
                        if a_tempo:
                            aggiorna_timer()
                        return
                mostra_risultato(finestra, domande, risposte_utente)
            except Exception as e:
                messagebox.showerror("Errore", f"Errore consegna: {e}")

        btn_indietro = tk.Button(frame_nav, text="<< Indietro", font=(MODELLO_FONT, 14), bg=PULSANTE_BG_COLOR, command=vai_indietro, width=12)
        btn_indietro.pack(side=tk.LEFT)
        
        btn_consegna = tk.Button(frame_nav, text="Consegna", font=(MODELLO_FONT, 14, "bold"), bg="#3b82f6", fg="white", command=consegna, width=12)
        btn_consegna.pack(side=tk.LEFT, padx=160)
        
        btn_avanti = tk.Button(frame_nav, text="Avanti >>", font=(MODELLO_FONT, 14), bg=PULSANTE_BG_COLOR, command=vai_avanti, width=12)
        btn_avanti.pack(side=tk.RIGHT)

        def aggiorna_vista():
            try:
                idx = stato["indice"]
                domanda_testo, _ = domande[idx]
                label_info.config(text=f"Domanda {idx + 1} di {len(domande)}")
                label_domanda.config(text=domanda_testo)
                
                if pulsante_vero and pulsante_falso:
                    if risposte_utente[idx] == "V":
                        pulsante_vero.config(bg=ACT_VERO_COLORE, fg="white")
                        pulsante_falso.config(bg=FALSO_COLORE, fg=BG_COLOR)
                    elif risposte_utente[idx] == "F":
                        pulsante_vero.config(bg=VERO_COLORE, fg=BG_COLOR)
                        pulsante_falso.config(bg=ACT_FALSO_COLORE, fg="white")
                    else:
                        pulsante_vero.config(bg=VERO_COLORE, fg=BG_COLOR)
                        pulsante_falso.config(bg=FALSO_COLORE, fg=BG_COLOR)
                    
                btn_indietro.config(state=tk.NORMAL if idx > 0 else tk.DISABLED)
                btn_avanti.config(state=tk.NORMAL if idx < len(domande) - 1 else tk.DISABLED)
            except Exception as e:
                messagebox.showerror("Errore", f"Errore aggiornamento vista: {e}")

        def aggiorna_timer():
            try:
                if stato["tempo"] > 0:
                    minuti = stato["tempo"] // 60
                    secondi = stato["tempo"] % 60
                    label_timer.config(text=f"Tempo rimanente: {minuti:02d}:{secondi:02d}")
                    stato["tempo"] -= 1
                    stato["timer_id"] = finestra.after(1000, aggiorna_timer)
                else:
                    messagebox.showinfo("Tempo scaduto", "Il tempo è scaduto! Il quiz verrà consegnato automaticamente.")
                    mostra_risultato(finestra, domande, risposte_utente)
            except Exception as e:
                pass

        aggiorna_vista()
        
        if a_tempo:
            aggiorna_timer()
            
    except Exception as e:
        messagebox.showerror("Errore", f"Errore gestore quiz: {e}")