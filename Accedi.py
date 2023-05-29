from  Registrazione import ricerca_nome
from tkinter import messagebox
import tkinter as tk

def open_window3():
    window3 =tk.Tk()
    window3.title("Accedi")
    window3.geometry("600x600")
    window3.resizable(False,False)

    nome_label = tk.Label(window3, text="Nome")
    nome_entry = tk.Entry(window3)
    cognome_label = tk.Label(window3, text="Cognome")
    cognome_entry = tk.Entry(window3)
    inserisci_button = tk.Button(window3, text="Invia")
    
    nome_label.pack()
    nome_entry.pack()
    cognome_label.pack()
    cognome_entry.pack() 
    inserisci_button.pack()
    window3.mainloop()

#def ricerca_account(nome,cognome):  
 #   if ricerca_nome(nome,cognome):
  #      messagebox.showerror("ok", "utente  trovato" )
   # else:
    #    messagebox.showerror("Errore", "utente non trovato" )