import tkinter as tk
import sqlite3

    
def Saldo(nome, cognome):
    conn = sqlite3.connect('PYTHON.db')
    cursor = conn.cursor()
    query="SELECT saldo FROM UTENTI WHERE nome=? AND cognome=?"
    saldo=cursor.execute(query, (nome, cognome))
    return saldo


def open_window4(nome,cognome):
    window4 =tk.Tk()
    window4.title("MENU'")
    window4.geometry("800x800")
    window4.resizable(False,False)
    

    TornaIndietro_button= tk.Button(window4, text="Inserisci")
    VisualizzaSaldo_button= tk.Button(window4, text="Visualizza il tuo saldo",command=lambda:Saldo(nome,cognome))
    TornaIndietro_button.pack()
    VisualizzaSaldo_button.pack()

    window4.mainloop()