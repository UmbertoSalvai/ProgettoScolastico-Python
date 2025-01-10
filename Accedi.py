from  Registrazione import ricerca_nome
from tkinter import messagebox
from Menu import *
from tkinter import *
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
  accediPage = tk.Tk()
  accediPage.title("Accedi")
  accediPage.geometry("800x800")
  accediPage.resizable(False, False)
  accediPage.configure(background="#00008B")

  validation_lettere = accediPage.register(solo_lettere)
  validation_numeri = accediPage.register(solo_numeri)

  parte_superiore = tk.Frame(accediPage, bg="#FFFFFF")
  parte_superiore.place(relx=0, rely=0, relwidth=1, relheight=0.2)

  nome_banca_label = tk.font.Font(family="Arial", size=30, weight="bold", slant="italic")
  nome_banca_label_label = tk.Label(parte_superiore, text="THE BANK", font=nome_banca_label, bg=parte_superiore["bg"])
  nome_banca_label_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

  nome_label = tk.Label(accediPage, text="Nome", font=("Arial", 14), bg="#00008B", fg="#FFFFFF")
  nome_entry = tk.Entry(accediPage, validate="key", validatecommand=(validation_lettere, '%S'), font=("Arial", 14))
  cognome_label = tk.Label(accediPage, text="Cognome", font=("Arial", 14), bg="#00008B", fg="#FFFFFF")
  cognome_entry = tk.Entry(accediPage, validate="key", validatecommand=(validation_lettere, '%S'), font=("Arial", 14))

  button_style = {
      "font": ("Arial", 14),
      "width": 15,
      "height": 2,
      "bg": "#FFFFFF",
      "fg": "#000000",
      "activebackground": "#A9D2FF",
      "bd": 0,
  }

  inserisci_button = tk.Button(accediPage, text="Inserisci", command=lambda: ricerca(nome_entry, cognome_entry, accediPage), **button_style)

  nome_label.pack(pady=(220, 0))
  nome_entry.pack(pady=(5, 0))
  cognome_label.pack(pady=(5, 0))
  cognome_entry.pack(pady=(5, 0))
  inserisci_button.pack(pady=(20, 10))

  chiudi_bottone = tk.Button(accediPage, text="Chiudi", command=accediPage.destroy, bg="#FF0000", fg="#FFFFFF", font=("Arial", 12))
  chiudi_bottone.pack(pady=(2, 20))
  
  accediPage.mainloop()