#import mysql.connector
import tkinter as tk

from Registrazione import  RegistrazionePage
from Accedi import  AccediPage


def click1():#funzioni per far prima chiudere la pgina e poi aprire quella nuova
    window.destroy()
    RegistrazionePage()
def click2():
    window.destroy()
    AccediPage()
    
  
    
    

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



