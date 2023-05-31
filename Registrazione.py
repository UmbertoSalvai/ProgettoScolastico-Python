import tkinter as tk
from tkinter import *
import sqlite3
from Scrivere import *
from Menu import MenuPage
from tkinter import messagebox

    
def Aggiungi_Utente(window2,nome_entry,cognome_entry,saldo_entry):#connessione a db e inserimento dati
    # Stabilisci la connessione al database SQLite
 
 
 nome = nome_entry.get()
 cognome = cognome_entry.get()
 saldo_da_controllare=saldo_entry.get()
 saldo=0
 if not nome_entry.get() or not cognome_entry.get() or not saldo_entry.get():
     messagebox.showerror("Errore", "Tutti i campi devono essere compilati")
     return
     
 elif  int(saldo_da_controllare) == 0:
            messagebox.showerror("Errore in inserimento ", "saldo inserito =0")
            return
            
 elif ricerca_nome(nome,cognome):
        
    # Ottieni il nome del campo e il tipo di dati dall'interfaccia utente
    
        messagebox.showerror("Errore", "Un utente con questo nome e cognome è già registrato")
        return
 saldo = int(saldo_da_controllare)
 with sqlite3.connect('PYTHON.db') as conn:
        cursor = conn.cursor()

        
        insert_query = "INSERT INTO UTENTI (nome, cognome, saldo) VALUES (?, ?, ?)"
        cursor.execute(insert_query, (nome, cognome, saldo))
        conn.commit()
      #window2.destroy()
     



#PAGINA 

def  RegistrazionePage():
 window2 =tk.Tk()
 window2.title("registrazione")
 window2.geometry("600x600")
 window2.resizable(False,False)

 validation_lettere = window2.register(solo_lettere) 
 validation_numeri = window2.register(solo_numeri)
 
 nome_label = tk.Label(window2, text="Nome")
 nome_entry = tk.Entry(window2, validate="key", validatecommand=(validation_lettere, '%S'))#inserimento solo lettere
 cognome_label = tk.Label(window2, text="Cognome")
 cognome_entry = tk.Entry(window2, validate="key", validatecommand=(validation_lettere, '%S'))#inserimento solo lettere
 saldo_label = tk.Label(window2, text="Inserisci il tuo saldo ")
 saldo_entry = tk.Entry(window2, validate="key", validatecommand=(validation_numeri, '%S'))#insermento solo numero

 

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

