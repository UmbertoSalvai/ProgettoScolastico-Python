#import mysql.connector
import tkinter as tk
import sqlite3
from Registrazione import  open_window2
from Accedi import  open_window3


def click1():#funzioni per far prima chiudere la pgina e poi aprire quella nuova
    window.destroy()
    open_window2()
def click2():
    window.destroy()
    open_window3()
    

    
    

#CREAZIONE PRIMA PAGINA
window =tk.Tk()
window.title("home")
window.geometry("800x800")

window.resizable(False,False)
window.configure(background="white")
#Primo bottone
primo_bottone=tk.Button(text="REGISTRATI!",command=click1)
primo_bottone.pack()
secondo_bottone=tk.Button(text="ACCEDI!",command=click2)
secondo_bottone.pack()
chiudi_bottone=tk.Button(text="chiudi",command=window.destroy)
chiudi_bottone.pack()
window.mainloop()



