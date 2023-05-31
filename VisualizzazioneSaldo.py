import tkinter as tk
import sqlite3
 

def Saldo(nome, cognome):#funzione per visualizzare il saldo
    saldopage=tk.Tk()
    saldopage.title("saldo")
    saldopage.geometry("200x200")
    saldopage.resizable(False,False)
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    query="SELECT Saldo FROM UTENTI WHERE nome=? AND cognome=?"
    cursor.execute(query, (nome, cognome))
    result = cursor.fetchone()
    
    if result:
        saldo = result[0]
        saldo_label = tk.Label(saldopage, text=f"Il tuo saldo attuale è: {saldo} €")
        saldo_label.pack()
    else:
        errore_label = tk.Label(saldopage, text="Non è presente il saldo")
        errore_label.pack()
    Esci_button = tk.Button(saldopage, text="Chiudi", command=saldopage.destroy)
    Esci_button.pack()
    saldopage.mainloop()
