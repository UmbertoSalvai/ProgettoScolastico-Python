import tkinter as tk
import sqlite3

def StoricoTransazioni(nome, cognome):
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()

    transazioniPage = tk.Tk()
    transazioniPage.title("STORICO TRANSAZIONI")
    transazioniPage.geometry("500x600")
    transazioniPage.resizable(False, False)
    transazioniPage.configure(background="#00008B")

    intestazione = ["ID ","Tipo ", "       Data       " , "Importo "  ]    
    stringa_sopra = tk.Label(transazioniPage, text="STORICO TRANSAZIONI", font=("Arial", 16, "bold"), bg="#00008B", fg="white")
    stringa_sopra.grid(row=0, column=0, columnspan=2, pady=10)

    transazioni_listbox = tk.Listbox(transazioniPage, width=50, height=30)
    transazioni_listbox.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    select_query = "SELECT IDutenti FROM UTENTI WHERE nome = ? and cognome = ? "
    cursor.execute(select_query, (nome, cognome))
    row = cursor.fetchone()

    if row:
        id_utente = row[0]
        select_query = "SELECT * FROM Transazioni WHERE IDUtente = ?"
        cursor.execute(select_query, (id_utente,))

        transazioni_listbox.insert(tk.END, intestazione)

        transazioni = cursor.fetchall()
        if transazioni:
            for transazione in transazioni:
                transazioni_listbox.insert(tk.END, transazione[:-1])
        else:
            transazioni_listbox.insert(tk.END, "Nessuna transazione trovata.")
    

    cursor.close()
    conn.close()

    transazioniPage.mainloop()
