import tkinter as tk
import sqlite3


def StoricoTransazioni(nome,cognome):
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()

    transazioniPage = tk.Tk()
    transazioniPage.title("MENU'")
    transazioniPage.geometry("600x600")
    transazioniPage.resizable(False, False)
    transazioniPage.configure(background="#00008B")  
    parte_superiore = tk.Frame(transazioniPage, bg="#FFFFFF")
    parte_superiore.place(relx=0, rely=0, relwidth=1, relheight=0.2)
    button_style = {
            "font": ("Arial", 14),
            "width": 15,
            "height": 2,
            "bg": "#FFFFFF",
            "fg": "#000000",
            "activebackground": "#A9D2FF",
            "bd": 0,
        }
    
    def avvia_ricerca():
        result = ricerca_Transazioni(Id)
        if result:
            print(result)  # Stampa la riga restituita dalla query
        else:
            print("Nessun risultato trovato.")
    select_query = "SELECT IDutenti FROM UTENTI WHERE nome = ? and cognome = ? "
    cursor.execute(select_query, (nome,cognome))
    Id = cursor.fetchone()
    
    avvia_ricerca_button = tk.Button(transazioniPage, command=avvia_ricerca(),text="Avvia la ricerca", **button_style)
    titolo_label = tk.Label(parte_superiore, text="THE BANK", font=("Arial", 30, "bold", "italic"), bg="#FFFFFF")
   
    avvia_ricerca_button.pack(pady=(320, 0))
    titolo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    transazioniPage.mainloop()


def ricerca_Transazioni(Id):
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    
    # Esegui la query SELECT per verificare se il nome esiste già
    select_query = "SELECT * FROM ContoCorrente WHERE IDutente==?"
    cursor.execute(select_query, (Id))
    
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    # Restituisci True se il nome esiste già, altrimenti False
    return result is not None

