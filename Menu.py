import tkinter as tk
import sqlite3
from VisualizzazioneSaldo import Saldo
from Scrivere import *
from Deposito import Aggiungi_Saldo
from Prelievo import open_Prelievopage

    

def MenuPage(nome,cognome,):
    menupage =tk.Tk()
    menupage.title("MENU'")
    menupage.geometry("800x800")
    menupage.resizable(False,False)
    

    TornaIndietro_button= tk.Button(menupage, text="Inserisci")
    VisualizzaSaldo_button= tk.Button(menupage, text="Visualizza il tuo saldo",command=lambda:Saldo(nome,cognome))
    AggiungiSaldo_button= tk.Button(menupage, text="Aggiungi saldo",command=lambda:Aggiungi_Saldo(nome,cognome))
    PrelievoSaldo=tk.Button(menupage,text="Prelievo",command=lambda:open_Prelievopage(nome,cognome))
    TornaIndietro_button.pack()
    VisualizzaSaldo_button.pack()
    AggiungiSaldo_button.pack()
    PrelievoSaldo.pack()
   
    menupage.mainloop()