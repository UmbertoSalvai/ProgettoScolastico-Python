from  Registrazione import ricerca_nome
from tkinter import messagebox
from Menu import *
import tkinter as tk
from Scrivere import *


def ricerca(nome_entry,cognome_entry,accediPage):
   x=True 
   while x:
     nome = nome_entry.get()
     cognome = cognome_entry.get()
     
     nome_entry.delete(0, 'end')
     cognome_entry.delete(0, 'end')
     if ricerca_nome(nome, cognome):
       messagebox.showinfo("UTENTE TROVATO", "Accesso eseguito")
       accediPage.destroy()
       MenuPage(nome,cognome)

       break       

     else:
        x=False
        messagebox.showerror("ERRORE","Utente non trovato,riprovare")
        break


   

def AccediPage():
    accediPage =tk.Tk()
    accediPage.title("Accedi")
    accediPage.geometry("600x600")
    accediPage.resizable(False,False)


    validation_lettere = accediPage.register(solo_lettere) 
    validation_numeri = accediPage.register(solo_numeri)

    nome_label = tk.Label(accediPage, text="Nome")
    nome_entry = tk.Entry(accediPage, validate="key", validatecommand=(validation_lettere, '%S'))
    cognome_label = tk.Label(accediPage, text="Cognome")
    cognome_entry = tk.Entry(accediPage, validate="key", validatecommand=(validation_lettere, '%S'))
   
    inserisci_button = tk.Button(accediPage, text="Inserisci", command=lambda:ricerca(nome_entry,cognome_entry,accediPage))
    
        
    nome_label.pack()
    nome_entry.pack()
    cognome_label.pack()
    cognome_entry.pack()
    inserisci_button.pack()
    accediPage.mainloop()