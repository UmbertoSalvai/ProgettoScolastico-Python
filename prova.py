import tkinter as tk
import sqlite3

def ricerca_Transazioni(Id):
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()

    select_query = "SELECT * FROM ContoCorrente WHERE IDutente=?"
    cursor.execute(select_query, (Id,))

    result = cursor.fetchall()
    cursor.close()
    conn.close()

    # Restituisce la lista di righe restituite dalla query
    return result


def avvia_ricerca():
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    text_area = tk.Text(transazioniPage, font=("Arial", 12))
    text_area.pack(pady=(100, 0))

    select_query = "SELECT IDutenti FROM UTENTI WHERE nome = ? and cognome = ?"
    cursor.execute(select_query, ('io', 'io'))
    Id = cursor.fetchone()

    if Id:
        result = ricerca_Transazioni(Id[0])
        if result:
            for row in result:
                text_area.insert(tk.END, str(row) + "\n")  
        else:
            text_area.insert(tk.END, "Nessun risultato trovato.\n")
    else:
        text_area.insert(tk.END, "Nessun ID utente trovato.\n")

    cursor.close()
    conn.close()


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



avvia_ricerca_button = tk.Button(transazioniPage, command=avvia_ricerca, text="Avvia la ricerca", **button_style)
titolo_label = tk.Label(parte_superiore, text="THE BANK", font=("Arial", 30, "bold", "italic"), bg="#FFFFFF")

avvia_ricerca_button.pack(pady=(320, 0))
titolo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

transazioniPage.mainloop()
