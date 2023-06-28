import tkinter as tk
from tkinter import messagebox
import sqlite3
from Scrivere import *
from OraDiOggi import *

def Prelievo(prelievopage,tolti_entry,nome,cognome):
    ora=str(oraCorrente())
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    tolti=tolti_entry.get()

  

    select_query = "SELECT (IDutenti) FROM Utenti WHERE Nome = ? and Cognome = ? "
    cursor.execute(select_query, (nome,cognome))
    result = cursor.fetchone()
    Id=result[0]

    saldo_query = "SELECT (Saldo) FROM ContoCorrente WHERE IDutente=? "
    cursor.execute(saldo_query, (Id,))
    result = cursor.fetchone()
    saldo_attuale=result[0]

    if not tolti_entry.get():
        messagebox.showerror("Errore in inserimento", "Inserire un valore numerico")
        tolti_entry.delete(0, 'end')
        return
    
    tolti = float(tolti)
    if  tolti ==0  :
       
        messagebox.showerror("Errore in inserimento", "saldo inserito = 0")
        tolti_entry.delete(0, 'end') 
        return
    elif tolti>saldo_attuale:
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
    prelievopage = tk.Tk()
    prelievopage.title("Prelievo")
    prelievopage.geometry("400x400")
    prelievopage.resizable(False, False)
    prelievopage.configure(background="#00008B")

    validation_numeri = prelievopage.register(solo_numeri)

    tolti_label = tk.Label(prelievopage, text="Quanto vuoi prelevare dal tuo conto?", font=("Arial", 14),bg="#00008B",
                            fg="#FFFFFF")
    tolti_label.pack(pady=(50, 10))

    tolti_entry = tk.Entry(prelievopage, validate="key", validatecommand=(validation_numeri, '%S'), font=("Arial", 14))
    tolti_entry.pack(pady=(0, 10))

    button_style = {
        "font": ("Arial", 12),
        "width": 15,
        "height": 2,
        "bg": "#FFFFFF",
        "fg": "#000000",
        "activebackground": "#A9D2FF",
        "bd": 0,
    }

    tolti_button = tk.Button(prelievopage, text="Togli saldo",
                            command=lambda: Prelievo(prelievopage, tolti_entry, nome, cognome), **button_style)
    tolti_button.pack(pady=(0, 10))

    chiudi_bottone = tk.Button(prelievopage, text="Chiudi", command=prelievopage.destroy,
                            bg="#FF0000", fg="#FFFFFF", font=("Arial", 12))
    chiudi_bottone.pack(pady=(100, 20))

    prelievopage.mainloop()



















