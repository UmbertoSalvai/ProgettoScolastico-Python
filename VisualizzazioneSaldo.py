import tkinter as tk
import sqlite3
 

def Saldo(nome, cognome):#funzione per visualizzare il saldo
    saldopage=tk.Tk()
    saldopage.title("saldo")
    saldopage.geometry("200x200")
    saldopage.resizable(False,False)
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()


    select_query = "SELECT (IDutenti) FROM Utenti WHERE Nome = ? and Cognome = ? "
    cursor.execute(select_query, (nome,cognome))
    result = cursor.fetchone()
    Id=result
        
    query="SELECT Saldo FROM ContoCorrente WHERE IDutente=?"
    cursor.execute(query, (Id))
    result1 = cursor.fetchone()
    
    if result1:
        saldo = result1[0]
        saldo_label = tk.Label(saldopage, text=f"Il tuo saldo attuale è: {saldo} €")
        saldo_label.pack()
    else:
        errore_label = tk.Label(saldopage, text="Non è presente il saldo")
        errore_label.pack()
    Esci_button = tk.Button(saldopage, text="Chiudi", command=saldopage.destroy)
    Esci_button.pack()
    saldopage.mainloop()
