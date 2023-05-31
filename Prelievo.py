import tkinter as tk
from tkinter import messagebox
import sqlite3
from Scrivere import *

def Prelievo(prelievopage,aggiunta_entry,nome,cognome):
    
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    aggiunti=aggiunta_entry.get()
     
    query="UPDATE UTENTI SET Saldo = Saldo - ? WHERE nome=? AND cognome=?"
    cursor.execute(query, (aggiunti,nome, cognome))
    
    conn.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo("OPERAZIONE RIUSCITA","prelievo andato a buon fine")

    prelievopage.destroy()

    
   
   
    
def open_Prelievopage(nome,cognome):
    prelievopage =tk.Tk()
    prelievopage.title("prelievo")
    prelievopage.geometry("600x600")
    prelievopage.resizable(False,False)

    
    validation_numeri = prelievopage.register(solo_numeri)
    aggiunta_label = tk.Label(prelievopage, text="qaunto vuoi prelevare dal tuo conto?")
    aggiunta_label.pack()
    aggiunta_entry = tk.Entry(prelievopage, validate="key", validatecommand=(validation_numeri, '%S'))
    aggiunta_entry.pack()
    
    
    
    aggiungi_button= tk.Button(prelievopage, text="togli saldo",command=lambda:Prelievo(prelievopage,aggiunta_entry,nome,cognome))
    aggiungi_button.pack()
    Esci_button = tk.Button(prelievopage, text="Chiudi", command=prelievopage.destroy)
    Esci_button.pack()
    
    #cursor.execute(query, (nome, cognome))
    #conn.commit()
    prelievopage.mainloop()


















