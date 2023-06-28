import tkinter as tk
import sqlite3
 

def Saldo(nome, cognome):#funzione per visualizzare il saldo
    saldopage = tk.Tk()
    saldopage.title("Saldo")
    saldopage.geometry("300x200")
    saldopage.resizable(False, False)
    saldopage.configure(background="#00008B")

    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()

    select_query = "SELECT IDutenti FROM Utenti WHERE Nome = ? and Cognome = ?"
    cursor.execute(select_query, (nome, cognome))
    result = cursor.fetchone()
    Id = result

    query = "SELECT Saldo FROM ContoCorrente WHERE IDutente = ?"
    cursor.execute(query, (Id))
    result1 = cursor.fetchone()

    if result1:
        saldo = result1[0]
        saldo_label = tk.Label(saldopage, text=f"Il tuo saldo attuale è: {saldo} €", font=("Arial", 14), bg="#00008B",
                            fg="#FFFFFF")
        saldo_label.pack(pady=(50, 10))
    else:
        errore_label = tk.Label(saldopage, text="Non è presente il saldo", font=("Arial", 14), bg="#00008B",
                                fg="#FFFFFF")
        errore_label.pack(pady=(50, 10))

    button_style = {
        "font": ("Arial", 12),
        "width": 10,
        "height": 1,
        "bg": "#FFFFFF",
        "fg": "#000000",
        "activebackground": "#A9D2FF",
        "bd": 0,
    }

    esci_button = tk.Button(saldopage, text="Chiudi", command=saldopage.destroy, **button_style)
    esci_button.pack(pady=(10, 0))

    saldopage.mainloop()

