# Quiz Simulatore Patente
# © 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0

# Cose mancanti:
# - Schermata del quiz con domande e risposte
# - Logica per verificare le risposte e tenere traccia del punteggio
# - Schermata finale con il punteggio e un messaggio di congratulazioni o incoraggiamento
# - Tornare indietro nelle domande finché il tempo non è scaduto

import tkinter as tk
from tkinter import messagebox
import prevedi_patente_modulo as funzioni

FG_COLOR = "black"
BG_COLOR = "white"
TEMPO = 20*60
tempo_rimanente = TEMPO

def main():
    finestra = tk.Tk()
    finestra.title("Quiz Simulatore Patente")

    finestra.geometry("900x600")
    finestra.resizable(False, False)
    finestra.configure(bg="white")

    domande = funzioni.leggi_domande()

    funzioni.schermata_iniziale(finestra, domande)
    finestra.mainloop()

if __name__ == "__main__":
    main()