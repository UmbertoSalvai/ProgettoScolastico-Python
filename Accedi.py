from  Registrazione import ricerca_nome
from tkinter import messagebox
from Menu import open_window4
import tkinter as tk
from Registrazione import solo_lettere
from Registrazione import solo_numeri


def ricerca(nome_entry,cognome_entry,window3):
   x=True 
   while x:
     nome = nome_entry.get()
     cognome = cognome_entry.get()
     
     nome_entry.delete(0, tk.END)
     cognome_entry.delete(0, tk.END)
     if ricerca_nome(nome, cognome):
       messagebox.showinfo("UTENTE TROVATO", "Accesso eseguito")
       window3.destroy()
       open_window4(nome_entry,cognome_entry)

       break       

     else:
        x=False
        messagebox.showerror("ERRORE","Utente non trovato,riprovare")
        break


   

def open_window3():
    window3 =tk.Tk()
    window3.title("Accedi")
    window3.geometry("600x600")
    window3.resizable(False,False)


    validation_lettere = window3.register(solo_lettere) 
    validation_numeri = window3.register(solo_numeri)

    nome_label = tk.Label(window3, text="Nome")
    nome_entry = tk.Entry(window3, validate="key", validatecommand=(validation_lettere, '%S'))
    cognome_label = tk.Label(window3, text="Cognome")
    cognome_entry = tk.Entry(window3, validate="key", validatecommand=(validation_lettere, '%S'))
   
    inserisci_button = tk.Button(window3, text="Inserisci", command=lambda:ricerca(nome_entry,cognome_entry,window3))
    
        
    nome_label.pack()
    nome_entry.pack()
    cognome_label.pack()
    cognome_entry.pack()
    inserisci_button.pack()
    window3.mainloop()