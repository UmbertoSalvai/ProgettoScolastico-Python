import tkinter as tk
from tkinter import messagebox
import sqlite3

def Aggiungi_Utente(window2,nome_entry,cognome_entry,saldo_entry):#connessione a db e inserimento dati
    # Stabilisci la connessione al database SQLite
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    
    nome = nome_entry.get()
    cognome = cognome_entry.get()
    if saldo_entry == 0:
            messagebox.showerror("Errore in inserimento ", "saldo inserito =0")
            saldo=0
    else:
     saldo=saldo_entry.get()
    # Ottieni il nome del campo e il tipo di dati dall'interfaccia utente
    if ricerca_nome(nome,cognome):
       messagebox.showerror("Errore", "Un utente con questo nome e cognome è già registrato")
    else:
    # Esegui la query ALTER TABLE per aggiungere il nuovo campo
     insert_query = "INSERT INTO UTENTI (nome, cognome,saldo) VALUES (? , ?, ?)"
     cursor.execute(insert_query, (nome, cognome,saldo))
    
    # Chiudi la connessione al database
    conn.commit()
    cursor.close()
    conn.close()
    window2.destroy() 



#PAGINA 

def open_window2():
 window2 =tk.Tk()
 window2.title("registrazione")
 window2.geometry("600x600")
 window2.resizable(False,False)


 nome_label = tk.Label(window2, text="Nome")
 nome_entry = tk.Entry(window2)
 cognome_label = tk.Label(window2, text="Cognome")
 cognome_entry = tk.Entry(window2)
 saldo_label = tk.Label(window2, text="Inserisci il tuo saldo ")
 saldo_entry = tk.Entry(window2)

 inserisci_button = tk.Button(window2, text="Inserisci", command=lambda: Aggiungi_Utente(window2,nome_entry,cognome_entry,saldo_entry))
 TornaIndietro_button = tk.Button(window2, text="Torna indietro", command=window2.destroy)
# Posiziona i widget nella finestra

 nome_label.pack()
 nome_entry.pack()
 cognome_label.pack()
 cognome_entry.pack()
 saldo_label.pack()
 saldo_entry.pack()
 inserisci_button.pack()
 TornaIndietro_button.pack()
 window2.mainloop()

def ricerca_nome(nome,cognome):
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    
    # Esegui la query SELECT per verificare se il nome esiste già
    select_query = "SELECT * FROM UTENTI WHERE nome = ? and cognome = ? "
    cursor.execute(select_query, (nome,cognome))
    
    # Ottieni il risultato della query
    result = cursor.fetchone()
    
    # Chiudi la connessione al database
    cursor.close()
    conn.close()
    
    # Restituisci True se il nome esiste già, altrimenti False
    return result is not None
