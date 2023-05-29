#import mysql.connector
import tkinter as tk
import sqlite3
def primo_bottone():
    testo="Ciao mondo"
    text_output=tk.Label(window,text=testo)
    text_output.grid(row=0,column=1)





#PAGINA2
#CREAZIONE PRIMA PAGINA
window =tk.Tk()

window.geometry("800x800")
window.title("home")
window.resizable(False,False)
window.configure(background="blue")
#Primo bottone
primo_bottone=tk.Button(text="REGISTRATI!",command=primo_bottone )
primo_bottone.grid(row=2,column=2)










