import tkinter as tk
import sqlite3
from VisualizzazioneSaldo import Saldo
from Scrivere import *
from Deposito import Aggiungi_Saldo
from Prelievo import open_Prelievopage

    

def MenuPage(nome,cognome,):
    menupage = tk.Tk()
    menupage.title("MENU'")
    menupage.geometry("800x800")
    menupage.resizable(False, False)
    menupage.configure(background="#00008B")

    parte_superiore = tk.Frame(menupage, bg="#FFFFFF")
    parte_superiore.place(relx=0, rely=0, relwidth=1, relheight=0.2)

    titolo_label = tk.Label(parte_superiore, text="THE BANK", font=("Arial", 30, "bold", "italic"), bg="#FFFFFF")
    titolo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    button_style = {
        "font": ("Arial", 14),
        "width": 15,
        "height": 2,
        "bg": "#FFFFFF",
        "fg": "#000000",
        "activebackground": "#A9D2FF",
        "bd": 0,
    }

    torna_indietro_button = tk.Button(menupage, text="Torna Indietro", **button_style)
    visualizza_saldo_button = tk.Button(menupage, text="Visualizza il tuo saldo", command=lambda: Saldo(nome, cognome),
                                    **button_style)
    aggiungi_saldo_button = tk.Button(menupage, text="Aggiungi saldo", command=lambda: Aggiungi_Saldo(nome, cognome),
                                    **button_style)
    prelievo_saldo_button = tk.Button(menupage, text="Prelievo", command=lambda: open_Prelievopage(nome, cognome),
                                    **button_style)

    torna_indietro_button.pack(pady=(220, 0))
    visualizza_saldo_button.pack(pady=(5, 0))
    aggiungi_saldo_button.pack(pady=(5, 0))
    prelievo_saldo_button.pack(pady=(5, 0))

    menupage.mainloop()
