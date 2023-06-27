import tkinter as tk
from tkinter import *
import sqlite3
from OraDiOggi import *
from Scrivere import *
from Menu import MenuPage
from tkinter import messagebox

    
def Aggiungi_Utente(registrazionePage,nome_entry,cognome_entry,saldo_entry,stipendio_entry):
    #connessione a db e inserimento dati
    # Stabilisci la connessione al database SQLite
 
 ora=str(oraCorrente())

 nome = nome_entry.get()
 cognome = cognome_entry.get()
 saldo_da_controllare=saldo_entry.get()
 stipendio=stipendio_entry.get()
 saldo=0
 if not nome_entry.get() or not cognome_entry.get() or not saldo_entry.get() or not stipendio_entry.get():
     messagebox.showerror("Errore", "Tutti i campi devono essere compilati")
     nome_entry.delete(0, 'end')  
     cognome_entry.delete(0, 'end') 
     saldo_entry.delete(0, 'end')  
     stipendio_entry.delete(0, 'end')
     return
     
 elif  int(saldo_da_controllare) == 0:
            messagebox.showerror("Errore in inserimento ", "saldo inserito =0")
            return
 elif  int(stipendio) == 0:
            messagebox.showerror("Errore in inserimento ", "stipendio inserito =0")
            return
 elif ricerca_nome(nome,cognome):
        # Ottieni il nome del campo e il tipo di dati dall'interfaccia utent
        messagebox.showerror("Errore", "Un utente con questo nome e cognome è già registrato")
        return
 saldo = saldo_da_controllare
 with sqlite3.connect('PYTHON.db') as conn:
        cursor = conn.cursor()
        
        insert_query = "INSERT INTO Utenti (nome, cognome) VALUES (?, ?) "
        cursor.execute(insert_query, (nome, cognome))
        select_query = "SELECT (IDutenti) FROM Utenti WHERE Nome = ? and Cognome = ? "
        cursor.execute(select_query, (nome,cognome))
        result = cursor.fetchone()
        Id=result[0]
        
        
        insert_query1 = "INSERT INTO ContoCorrente (saldo,DataApertura,IDutente,Stipendio) VALUES (?,?,?,?)"

        cursor.execute(insert_query1, (saldo,ora,Id,stipendio))
        conn.commit()  
        #conn.close()
        #cursor.close() 
        registrazionePage.destroy()
        MenuPage(nome,cognome)  
           
        
     



#PAGINA 

def  RegistrazionePage():
 registrazionePage =tk.Tk()
 registrazionePage.title("registrazione")
 registrazionePage.geometry("600x600")
 registrazionePage.resizable(False,False)

 validation_lettere = registrazionePage.register(solo_lettere) 
 validation_numeri = registrazionePage.register(solo_numeri)
 
 nome_label = tk.Label(registrazionePage, text="Nome")
 nome_entry = tk.Entry(registrazionePage, validate="key", validatecommand=(validation_lettere, '%S'))#inserimento solo lettere
 cognome_label = tk.Label(registrazionePage, text="Cognome")
 cognome_entry = tk.Entry(registrazionePage, validate="key", validatecommand=(validation_lettere, '%S'))#inserimento solo lettere
 saldo_label = tk.Label(registrazionePage, text="Inserisci il tuo saldo ")
 saldo_entry = tk.Entry(registrazionePage, validate="key", validatecommand=(validation_numeri, '%S'))#insermento solo numero
 stipendio_label = tk.Label(registrazionePage, text="Inserisci il tuo saldo ")
 stipendio_entry = tk.Entry(registrazionePage, validate="key", validatecommand=(validation_numeri, '%S'))#insermento solo numero

 

 inserisci_button = tk.Button(registrazionePage, text="Inserisci", command=lambda: Aggiungi_Utente(registrazionePage,nome_entry,cognome_entry,saldo_entry,stipendio_entry))
 TornaIndietro_button = tk.Button(registrazionePage, text="Torna indietro", command=registrazionePage.destroy)
# Posiziona i widget nella finestra

 nome_label.pack()
 nome_entry.pack()
 cognome_label.pack()
 cognome_entry.pack()
 saldo_label.pack()
 saldo_entry.pack()
 stipendio_label.pack()
 stipendio_entry.pack()
 inserisci_button.pack()
 TornaIndietro_button.pack()
 registrazionePage.mainloop()

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

