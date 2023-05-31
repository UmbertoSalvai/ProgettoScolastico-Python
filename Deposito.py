import tkinter as tk
import sqlite3

from Scrivere import *

from Prelievo import *


def Aggiunta(window6,aggiunta_entry,nome,cognome):
    
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    aggiunti=aggiunta_entry.get()
     
    query="UPDATE UTENTI SET Saldo = Saldo + ? WHERE nome=? AND cognome=?"
    cursor.execute(query, (aggiunti,nome, cognome))
    
    conn.commit()
    cursor.close()
    conn.close()
    messagebox.showinfo("OPERAZIONE RIUSCITA","importo inserito correttamente")
    window6.destroy()
    
   

def Aggiungi_Saldo(nome,cognome):#funzione per aggiungere il saldo
    #window4.destroy()
    window6=tk.Tk()
    window6.title("saldo")
    window6.geometry("400x400")
    window6.resizable(False,False)
    
    validation_numeri = window6.register(solo_numeri)
    aggiunta_label = tk.Label(window6, text="qaunto vuoi aggiungere al tuo conto?")
    aggiunta_label.pack()
    aggiunta_entry = tk.Entry(window6, validate="key", validatecommand=(validation_numeri, '%S'))
    aggiunta_entry.pack()
    
    
    
    aggiungi_button= tk.Button(window6, text="aggiungi saldo",command=lambda:Aggiunta(window6,aggiunta_entry,nome,cognome))
    aggiungi_button.pack()
    Esci_button = tk.Button(window6, text="Chiudi", command=window6.destroy)
    Esci_button.pack()
    
    #cursor.execute(query, (nome, cognome))
    #conn.commit()
    window6.mainloop()