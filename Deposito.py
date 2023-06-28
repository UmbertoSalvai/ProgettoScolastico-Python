import tkinter as tk
import sqlite3
from tkinter import messagebox
from Scrivere import *
from OraDiOggi import *
from Prelievo import *


def Deposito(aggiungiPage,aggiunta_entry,nome,cognome):
    ora=str(oraCorrente())
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    
    aggiunti=aggiunta_entry.get()
     
    aggiunta_entry.delete(0, 'end')

    if not aggiunti():
        messagebox.showerror("Errore in inserimento", "Inserire un valore numerico")
        return
    aggiunti = float(aggiunti)
    if  aggiunti ==0  :
       
        messagebox.showerror("Errore in inserimento", "saldo inserito = 0")
        return
    else:
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
        aggiungiPage.destroy()
        
   

def Aggiungi_Saldo(nome,cognome):#funzione per aggiungere il saldo
        
    aggiungiPage = tk.Tk()
    aggiungiPage.title("Saldo")
    aggiungiPage.geometry("400x400")
    aggiungiPage.resizable(False, False)
    aggiungiPage.configure(background="#00008B")

    validation_numeri = aggiungiPage.register(solo_numeri)

    aggiunta_label = tk.Label(aggiungiPage, text="Quanto vuoi aggiungere al tuo conto?", font=("Arial", 14), bg="#00008B",
                            fg="#FFFFFF")
    aggiunta_label.pack(pady=(50, 10))

    aggiunta_entry = tk.Entry(aggiungiPage, validate="key", validatecommand=(validation_numeri, '%S'), font=("Arial", 14))
    aggiunta_entry.pack(pady=(0, 10))

    button_style = {
        "font": ("Arial", 12),
        "width": 15,
        "height": 2,
        "bg": "#FFFFFF",
        "fg": "#000000",
        "activebackground": "#A9D2FF",
        "bd": 0,
    }

    aggiungi_button = tk.Button(aggiungiPage, text="Aggiungi saldo", command=lambda: Deposito(aggiungiPage, aggiunta_entry, nome, cognome),
                                **button_style)
    aggiungi_button.pack(pady=(0, 10))

    esci_button = tk.Button(aggiungiPage, text="Chiudi", command=aggiungiPage.destroy, **button_style)
    esci_button.pack(pady=(0, 20))

    aggiungiPage.mainloop()
