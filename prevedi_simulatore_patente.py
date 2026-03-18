# Quiz Simulatore Patente
# © 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0

# Cose mancanti:
# - Schermata del quiz con domande e risposte
# - Logica per verificare le risposte e tenere traccia del punteggio
# - Schermata finale con il punteggio e un messaggio di congratulazioni o incoraggiamento
# - Tornare indietro nelle domande finché il tempo non è scaduto

import tkinter as tk
from tkinter import messagebox

MODELLO_FONT = ("system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif")
FG_COLOR = "black"
BG_COLOR = "white"
TEMPO = 20*60
tempo_rimanente = TEMPO


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


def leggi_domande():
    domande = []
    with open("domande_rev_v2.txt", "r") as file:
        for linea in file:
            parti = linea.strip().split("|")
            domande.append([parti[1].strip(), parti[0].strip()])
    return domande


def preleva_domande(domande):
    import random
    domande_selezionate = random.sample(domande, 30)
    return domande_selezionate


def schermata_iniziale(finestra, domande):
    scritta_principale = tk.Label(finestra, text="Benvenuto/a nel Quiz Simulatore Patente", font=(MODELLO_FONT, 32), fg=FG_COLOR, bg=BG_COLOR)
    scritta_principale.pack(pady=20)

    pulsante_inizia_quiz = tk.Button(finestra, text="Inizia Quiz", font=(MODELLO_FONT, 16), fg=FG_COLOR, bg=BG_COLOR, command=lambda: inizia_quiz(finestra, domande))
    pulsante_inizia_quiz.pack(pady=10)

    scritta_crediti = tk.Label(finestra, text="© 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0", font=(MODELLO_FONT, 12), fg=FG_COLOR, bg="lightgray", padx=1000, pady=10)
    scritta_crediti.pack(side=tk.BOTTOM)


def inizia_quiz(finestra, domande):
    domande_selezionate = preleva_domande(domande)

def main():
    finestra = tk.Tk()
    finestra.title("Quiz Simulatore Patente")

    finestra.geometry("900x600")
    finestra.resizable(False, False)
    finestra.configure(bg="white")

    domande = leggi_domande()

    schermata_iniziale(finestra, domande)
    finestra.mainloop()

if __name__ == "__main__":
    main()