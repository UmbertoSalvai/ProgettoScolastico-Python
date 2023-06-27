import tkinter as tk
import sqlite3
from tkinter import messagebox
from Scrivere import *
from OraDiOggi import *
from Prelievo import *


def Aggiunta(saldoPage,aggiunta_entry,nome,cognome):
    ora=str(oraCorrente())
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    aggiunti=aggiunta_entry.get()

    select_query = "SELECT (IDutenti) FROM Utenti WHERE Nome = ? and Cognome = ? "
    cursor.execute(select_query, (nome,cognome))
    result = cursor.fetchone()
    Id=result[0]
    
    query="UPDATE ContoCorrente SET Saldo = Saldo + ? WHERE IDutente=?"
    cursor.execute(query, (aggiunti,Id))
    
    query2="INSERT INTO Transazioni(Tipo, Data,Importo,IDutente) VALUES ('Deposito',? ,?,?) "
    cursor.execute(query2, (ora,aggiunti,Id ))

    conn.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo("OPERAZIONE RIUSCITA","importo inserito correttamente")
    saldoPage.destroy()
    
   

def Aggiungi_Saldo(nome,cognome):#funzione per aggiungere il saldo
    
    saldoPage=tk.Tk()
    saldoPage.title("saldo")
    saldoPage.geometry("400x400")
    saldoPage.resizable(False,False)
    
    validation_numeri = saldoPage.register(solo_numeri)
    aggiunta_label = tk.Label(saldoPage, text="qaunto vuoi aggiungere al tuo conto?")
    aggiunta_label.pack()
    aggiunta_entry = tk.Entry(saldoPage, validate="key", validatecommand=(validation_numeri, '%S'))
    aggiunta_entry.pack()
    
    
    
    aggiungi_button= tk.Button(saldoPage, text="aggiungi saldo",command=lambda:Aggiunta(saldoPage,aggiunta_entry,nome,cognome))
    aggiungi_button.pack()
    Esci_button = tk.Button(saldoPage, text="Chiudi", command=saldoPage.destroy)
    Esci_button.pack()
    
    
    saldoPage.mainloop()