# Quiz Simulatore Patente
# © 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0

import tkinter as tk
from tkinter import messagebox
from platform import system

if system == "Windows":
    MODELLO_FONT = 'Cambria'
elif system == "Linux":
    MODELLO_FONT = "Arial"
elif system == "Darwin":
    MODELLO_FONT = "San Francisco"
else:
    MODELLO_FONT = "Arial"

FG_COLOR = "black"
BG_COLOR = "white"
PULSANTE_BG_COLOR = "#dddddd"
ACT_PULSANTE_BG_COLOR = "#aaaaaa"
VERO_COLORE = "#16a34a"
ACT_VERO_COLORE = "#15803d"
FALSO_COLORE = "#ef4444"
ACT_FALSO_COLORE = "#dc2626"

TEMPO = 20*60
tempo_rimanente = TEMPO

def crea_pulsante_vero(finestra, funzione):
    return tk.Button(
        finestra,
        text = "Vero",
        font = (MODELLO_FONT, 15, "bold"),
        bg = VERO_COLORE,
        fg = BG_COLOR,
        activebackground = ACT_VERO_COLORE,
        activeforeground = BG_COLOR,
        width = 12,
        height = 2,
        bd = 0,
        command = funzione
    )

def crea_pulsante_falso(finestra, funzione):
    return tk.Button(
        finestra,
        text = "Falso",
        font = (MODELLO_FONT, 15, "bold"),
        bg = FALSO_COLORE,
        fg = BG_COLOR,
        activebackground = ACT_FALSO_COLORE,
        activeforeground = BG_COLOR,
        width = 12,
        height = 2,
        bd = 0,
        command = funzione
    )

def leggi_domande():
    domande = []
    with open("domande.txt", "r") as file:
        for linea in file:
            parti = linea.strip().split("|")
            domande.append([parti[1].strip(), parti[0].strip()])
    return domande


def preleva_domande(domande):
    import random
    domande_selezionate = random.sample(domande, 5)
    return domande_selezionate


def timer(finestra, label_timer):
    global tempo_rimanente
    if tempo_rimanente > 0:
        tempo_rimanente -= 1
        minuti = tempo_rimanente // 60
        secondi = tempo_rimanente % 60
        label_timer.config(text=f"Tempo rimanente: {minuti:02d}:{secondi:02d}")
        finestra.after(1000, timer)
    else:
        messagebox.showinfo("Tempo scaduto", "Il tempo è scaduto! Il quiz è terminato.")
        finestra.destroy()


def schermata_iniziale(finestra, domande):
    scritta_principale = tk.Label(finestra, text="Benvenuto/a nel Quiz Simulatore Patente", font=(MODELLO_FONT, 24), fg=FG_COLOR, bg=BG_COLOR)
    scritta_principale.pack(pady=20)

    pulsante_inizia_quiz_a_tempo = tk.Button(finestra, 
                                     text="Inizia Prova a Tempo", 
                                     font=(MODELLO_FONT, 14), 
                                     fg=FG_COLOR, 
                                     bg=PULSANTE_BG_COLOR,
                                     bd = 0,
                                     activebackground=ACT_PULSANTE_BG_COLOR,
                                     activeforeground=FG_COLOR,
                                     width = 18,
                                     height = 2,
                                     command=lambda: inizia_quiz(finestra, domande, True))
    pulsante_inizia_quiz_a_tempo.pack(pady=10)

    pulsante_inizia_simulazione = tk.Button(finestra, 
                                     text="Inizia Simulazione", 
                                     font=(MODELLO_FONT, 14), 
                                     fg=FG_COLOR, 
                                     bg=PULSANTE_BG_COLOR,
                                     bd = 0,
                                     activebackground=ACT_PULSANTE_BG_COLOR,
                                     activeforeground=FG_COLOR,
                                     width = 18,
                                     height = 2,
                                     command=lambda: inizia_quiz(finestra, domande, False))
    pulsante_inizia_simulazione.pack(pady=10)

    scritta_crediti = tk.Label(finestra, text="© 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0", font=(MODELLO_FONT, 10), fg=FG_COLOR, bg="#f1f1f1", padx=1000, pady=10)
    scritta_crediti.pack(side=tk.BOTTOM)


def inizia_quiz(finestra, domande, tempo):
    domande_selezionate = preleva_domande(domande)

    finestra.destroy()
    finestra_quiz = tk.Tk()
    finestra_quiz.title("Quiz Simulatore Patente")
    finestra_quiz.geometry("900x600")
    finestra_quiz.resizable(False, False)
    finestra_quiz.configure(bg=BG_COLOR)

    if tempo == True:
        quiz_a_tempo(finestra_quiz, domande_selezionate)
    else:
        quiz_libero(finestra_quiz, domande_selezionate)