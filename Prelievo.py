import tkinter as tk
from tkinter import messagebox
import sqlite3
from Scrivere import *
from OraDiOggi import *

def Prelievo(prelievopage,tolti_entry,nome,cognome):
    ora=str(oraCorrente())
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    tolti=int(tolti_entry.get())

  

    select_query = "SELECT (IDutenti) FROM Utenti WHERE Nome = ? and Cognome = ? "
    cursor.execute(select_query, (nome,cognome))
    result = cursor.fetchone()
    Id=result[0]

    saldo_query = "SELECT (Saldo) FROM ContoCorrente WHERE IDutente=? "
    cursor.execute(saldo_query, (Id,))
    result = cursor.fetchone()
    saldo_attuale=result[0]
    if tolti>saldo_attuale:
        messagebox.showerror("Errore  ", "L'importo che vuole prelevare è maggiore dell'importo disponibile")
        tolti_entry.delete(0, 'end') 
        return
    else:
        query="UPDATE ContoCorrente SET Saldo = Saldo - ? WHERE IDutente=?"
        cursor.execute(query, (tolti,Id))

        query2="INSERT INTO Transazioni(Tipo, Data,Importo,IDutente) VALUES ('Prelievo',? ,?,?) "
        cursor.execute(query2, (ora,tolti,Id ))


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
    tolti_label = tk.Label(prelievopage, text="qaunto vuoi prelevare dal tuo conto?")
    tolti_label.pack()
    tolti_entry = tk.Entry(prelievopage, validate="key", validatecommand=(validation_numeri, '%S'))
    tolti_entry.pack()
    
    
    
    tolti_button= tk.Button(prelievopage, text="togli saldo",command=lambda:Prelievo(prelievopage,tolti_entry,nome,cognome))
    tolti_button.pack()
    Esci_button = tk.Button(prelievopage, text="Chiudi", command=prelievopage.destroy)
    Esci_button.pack()
    
    #cursor.execute(query, (nome, cognome))
    #conn.commit()
    prelievopage.mainloop()


















