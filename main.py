#import mysql.connector
import tkinter as tk
import sqlite3
from Registrazione import  open_window2


#CREAZIONE PRIMA PAGINA
window =tk.Tk()
window.title("home")
window.geometry("800x800")

window.resizable(False,False)
window.configure(background="CYAN")
#Primo bottone
primo_bottone=tk.Button(text="REGISTRATI!",command=open_window2)
primo_bottone.pack()

window.mainloop()



