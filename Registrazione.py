import tkinter as tk
import sqlite3

def Aggiungi_Utente():#connessione a db e inserimento dati
    # Stabilisci la connessione al database SQLite
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    
    # Ottieni il nome del campo e il tipo di dati dall'interfaccia utente
   
    nome = nome_entry.get()
    cognome = cognome_entry.get()
    
    # Esegui la query ALTER TABLE per aggiungere il nuovo campo
    insert_query = "INSERT INTO UTENTI (nome, cognome) VALUES (? , ?)"
    cursor.execute(insert_query, (nome, cognome))
    
    # Chiudi la connessione al database
    conn.commit()
    cursor.close()
    conn.close()



#PAGINA 2
#secondo bottone CHE APRE UNA NUOVA PAGINA
window2 =tk.Tk()
window2.title("registrazione")
window2.geometry("600x600")
window2.resizable(False,False)


nome_label = tk.Label(window2, text="Nome")
nome_entry = tk.Entry(window2)
cognome_label = tk.Label(window2, text="Cognome")
cognome_entry = tk.Entry(window2)

inserisci_button = tk.Button(window2, text="Inserisci", command=Aggiungi_Utente)

# Posiziona i widget nella finestra

nome_label.pack()
nome_entry.pack()
cognome_label.pack()
cognome_entry.pack()
inserisci_button.pack()



window2.mainloop()

