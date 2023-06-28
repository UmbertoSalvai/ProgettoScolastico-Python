import tkinter as tk
from tkinter import *
import sqlite3
from OraDiOggi import *
from Scrivere import *
from Menu import MenuPage
from tkinter import messagebox

    
def Aggiungi_Utente(registrazionePage, nome_entry, cognome_entry, saldo_entry, stipendio_entry):
    ora = str(oraCorrente())

    nome = nome_entry.get()
    cognome = cognome_entry.get()
    saldo_da_controllare = saldo_entry.get()
    stipendio = stipendio_entry.get()
    saldo = 0

    if not nome_entry.get() or not cognome_entry.get() or not saldo_entry.get() or not stipendio_entry.get():
        messagebox.showerror("Errore", "Tutti i campi devono essere compilati")
        nome_entry.delete(0, 'end')
        cognome_entry.delete(0, 'end')
        saldo_entry.delete(0, 'end')
        stipendio_entry.delete(0, 'end')
        return

    elif int(saldo_da_controllare) == 0:
        messagebox.showerror("Errore in inserimento", "saldo inserito = 0")
        return

    elif int(stipendio) == 0:
        messagebox.showerror("Errore in inserimento", "stipendio inserito = 0")
        return

    elif ricerca_nome(nome, cognome):
        messagebox.showerror("Errore", "Un utente con questo nome e cognome è già registrato")
        return

    saldo = saldo_da_controllare

    with sqlite3.connect('PYTHON.db') as conn:
        cursor = conn.cursor()

        insert_query = "INSERT INTO Utenti (nome, cognome) VALUES (?, ?)"
        cursor.execute(insert_query, (nome, cognome))

        select_query = "SELECT (IDutenti) FROM Utenti WHERE Nome = ? and Cognome = ?"
        cursor.execute(select_query, (nome, cognome))
        result = cursor.fetchone()
        Id = result[0]

        insert_query1 = "INSERT INTO ContoCorrente (saldo, DataApertura, IDutente, Stipendio) VALUES (?,?,?,?)"
        cursor.execute(insert_query1, (saldo, ora, Id, stipendio))
        conn.commit()

        registrazionePage.destroy()
        MenuPage(nome, cognome)


def RegistrazionePage():
    registrazionePage = tk.Tk()
    registrazionePage.title("Bank Website - Registrazione")
    registrazionePage.geometry("800x800")
    registrazionePage.resizable(False, False)
    registrazionePage.configure(background="#00008B")
    validation_lettere = registrazionePage.register(solo_lettere)
    validation_numeri = registrazionePage.register(solo_numeri)

    parte_superiore = tk.Frame(registrazionePage, bg="#FFFFFF")
    parte_superiore.place(relx=0, rely=0, relwidth=1, relheight=0.2)


    nome_banca_label = tk.font.Font(family="Arial", size=30, weight="bold", slant="italic")
    nome_banca_label_label = tk.Label(parte_superiore, text="THE BANK", font=nome_banca_label,bg=parte_superiore["bg"])
    nome_banca_label_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    nome_label = tk.Label(registrazionePage, text="Nome", font=("Arial", 14), bg="#00008B", fg="#FFFFFF")
    nome_entry = tk.Entry(registrazionePage, validate="key", validatecommand=(validation_lettere, '%S'),
                          font=("Arial", 14))
    cognome_label = tk.Label(registrazionePage, text="Cognome", font=("Arial", 14), bg="#00008B", fg="#FFFFFF")
    cognome_entry = tk.Entry(registrazionePage, validate="key", validatecommand=(validation_lettere, '%S'),
                             font=("Arial", 14))
    saldo_label = tk.Label(registrazionePage, text="Inserisci il tuo saldo", font=("Arial", 14), bg="#00008B",
                           fg="#FFFFFF")
    saldo_entry = tk.Entry(registrazionePage, validate="key", validatecommand=(validation_numeri, '%S'),
                           font=("Arial", 14))
    stipendio_label = tk.Label(registrazionePage, text="Inserisci il tuo stipendio", font=("Arial", 14), bg="#00008B",
                               fg="#FFFFFF")
    stipendio_entry = tk.Entry(registrazionePage, validate="key", validatecommand=(validation_numeri, '%S'),
                               font=("Arial", 14))
    button_style = {
        "font": ("Arial", 14),
        "width": 15,
        "height": 2,
        "bg": "#FFFFFF",
        "fg": "#000000",
        "activebackground": "#A9D2FF",
        "bd": 0,
    }

    inserisci_button = tk.Button(registrazionePage, text="Inserisci",
                                command=lambda: Aggiungi_Utente(registrazionePage, nome_entry, cognome_entry,
                                                                saldo_entry, stipendio_entry), **button_style)
    
    nome_label.pack(pady=(220,0))
    nome_entry.pack(pady=(5, 0))
    cognome_label.pack(pady=(5, 0))
    cognome_entry.pack(pady=(5, 0))
    saldo_label.pack(pady=(5, 0))
    saldo_entry.pack(pady=(5, 0))
    stipendio_label.pack(pady=(5, 0))
    stipendio_entry.pack(pady=(5, 0))

    inserisci_button.pack(pady=(20,10))


    chiudi_bottone = tk.Button(registrazionePage, text="Chiudi", command=registrazionePage.destroy,
                               bg="#FF0000", fg="#FFFFFF", font=("Arial", 12))
    chiudi_bottone.pack(pady=(100,20))

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

