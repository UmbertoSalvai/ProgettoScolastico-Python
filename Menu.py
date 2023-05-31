import tkinter as tk
import sqlite3
from Registrazione import solo_numeri
from Prelievo import *
    
def Saldo(nome, cognome):#funzione per visualizzare il saldo
    window5=tk.Tk()
    window5.title("saldo")
    window5.geometry("200x200")
    window5.resizable(False,False)
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    query="SELECT Saldo FROM UTENTI WHERE nome=? AND cognome=?"
    cursor.execute(query, (nome, cognome))
    result = cursor.fetchone()
    
    if result:
        saldo = result[0]
        saldo_label = tk.Label(window5, text=f"Il tuo saldo attuale è: {saldo} €")
        saldo_label.pack()
    else:
        errore_label = tk.Label(window5, text="Non è presente il saldo")
        errore_label.pack()
    Esci_button = tk.Button(window5, text="Chiudi", command=window5.destroy)
    Esci_button.pack()
    window5.mainloop()

def Aggiunta(window6,aggiunta_entry,nome,cognome):
    
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    aggiunti=aggiunta_entry.get()
     
    query="UPDATE UTENTI SET Saldo = Saldo + ? WHERE nome=? AND cognome=?"
    cursor.execute(query, (aggiunti,nome, cognome))
    
    conn.commit()
    cursor.close()
    conn.close()
    Esci_button = tk.Button(window6, text="Chiudi", command=window6.destroy)
    Esci_button.pack()
   
   
    

    



def Aggiungi_Saldo(nome,cognome):#funzione per aggiungere il saldo
    #window4.destroy()
    window6=tk.Tk()
    window6.title("saldo")
    window6.geometry("400x400")
    window6.resizable(False,False)
    
    validation_numeri = window6.register(solo_numeri)
    aggiunta_label = tk.Label(window6, text="qaunto vuoi aggiungere al tuo conto?")
    aggiunta_label.pack()
    aggiunta_entry = tk.Entry(window6, validate="key", validatecommand=(validation_numeri, '%S'))
    aggiunta_entry.pack()
    
    
    
    aggiungi_button= tk.Button(window6, text="aggiungi saldo",command=lambda:Aggiunta(window6,aggiunta_entry,nome,cognome))
    aggiungi_button.pack()
    Esci_button = tk.Button(window6, text="Chiudi", command=window6.destroy)
    Esci_button.pack()
    
    #cursor.execute(query, (nome, cognome))
    #conn.commit()
    window6.mainloop()
    

    
    

def MenuPage(nome,cognome,):
    menupage =tk.Tk()
    menupage.title("MENU'")
    menupage.geometry("800x800")
    menupage.resizable(False,False)
    

    TornaIndietro_button= tk.Button(menupage, text="Inserisci")
    VisualizzaSaldo_button= tk.Button(menupage, text="Visualizza il tuo saldo",command=lambda:Saldo(nome,cognome))
    AggiungiSaldo_button= tk.Button(menupage, text="Aggiungi saldo",command=lambda:Aggiungi_Saldo(nome,cognome))
    PrelievoSaldo=tk.Button(menupage,text="Prelievo",command=lambda:open_Prelievopage(nome,cognome))
    TornaIndietro_button.pack()
    VisualizzaSaldo_button.pack()
    AggiungiSaldo_button.pack()
    PrelievoSaldo.pack()
   
    menupage.mainloop()