import tkinter as tk
from tkinter import messagebox

# def schermata_iniziale(finestra, domande):
#     for widget in finestra.winfo_children():
#         widget.destroy()

#     titolo = tk.Label(finestra, text="Quiz Simulatore Patente", font=("Arial", 24))
#     titolo.pack(pady=20)

#     bottone_inizia = tk.Button(finestra, text="Inizia Quiz", font=("Arial", 16), command=lambda: schermata_quiz(finestra, domande))
#     bottone_inizia.pack(pady=10)

# def schermata_quiz(finestra, domande):
#     for widget in finestra.winfo_children():
#         widget.destroy()

#     domanda = domande[0][0]
#     risposta_corretta = domande[0][1]

#     label_domanda = tk.Label(finestra, text=domanda, font=("Arial", 18), wraplength=800)
#     label_domanda.pack(pady=20)

#     entry_risposta = tk.Entry(finestra, font=("Arial", 16))
#     entry_risposta.pack(pady=10)

#     def verifica_risposta():
#         risposta_utente = entry_risposta.get().strip()
#         if risposta_utente.lower() == risposta_corretta.lower():
#             messagebox.showinfo("Risultato", "Risposta corretta!")
#         else:
#             messagebox.showerror("Risultato", f"Risposta errata! La risposta corretta è: {risposta_corretta}")

#     bottone_verifica = tk.Button(finestra, text="Verifica Risposta", font=("Arial", 16), command=verifica_risposta)
#     bottone_verifica.pack(pady=10)


def leggi_domande():
    domande = []
    with open("domande_rev_v2.txt", "r") as file:
        for linea in file:
            parti = linea.strip().split("|")
            domande.append([parti[1].strip(), parti[0].strip()])
    return domande

def schermata_iniziale(finestra, domande):
    scritta_principale = tk.Label(finestra, text="Benvenuto/a nel Quiz Simulatore Patente", font=("San Francisco", 24), )

def main():
    finestra = tk.Tk()
    finestra.title("Quiz Simulatore Patente")

    finestra.geometry("900x600")
    finestra.resizable(False, False)
    domande = leggi_domande()

    schermata_iniziale(finestra, domande)
    finestra.mainloop()

if __name__ == "__main__":
    main()