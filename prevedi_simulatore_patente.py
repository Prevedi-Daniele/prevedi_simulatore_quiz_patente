# Quiz Simulatore Patente
# © 2026 Daniele Prevedi. Soggetto a licenza CC BY-NC-SA 4.0

import tkinter as tk
import support.prevedi_patente_modulo as funzioni

def main():
    finestra = tk.Tk()
    finestra.title("Quiz Simulatore Patente")

    finestra.geometry("1080x720")
    finestra.resizable(False, False)
    finestra.configure(bg="white")

    domande = funzioni.leggi_domande()

    funzioni.schermata_iniziale(finestra, domande)
    finestra.mainloop()

if __name__ == "__main__":
    main()