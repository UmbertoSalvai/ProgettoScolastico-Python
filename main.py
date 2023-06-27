#import mysql.connector
import tkinter as tk

from Registrazione import  RegistrazionePage
from Accedi import  AccediPage


def click1():#funzioni per far prima chiudere la pgina e poi aprire quella nuova
    mainPage.destroy()
    RegistrazionePage()
def click2():
    mainPage.destroy()
    AccediPage()
    
  
    
    

#CREAZIONE PRIMA PsAGINA
mainPage =tk.Tk()
mainPage.title("home")
mainPage.geometry("800x800")

mainPage.resizable(False,False)
mainPage.configure(background="white")
#Primo bottone
primo_bottone=tk.Button(text="REGISTRATI!",command=click1)
primo_bottone.pack()
secondo_bottone=tk.Button(text="ACCEDI!",command=click2)
secondo_bottone.pack()
chiudi_bottone=tk.Button(text="chiudi",command=mainPage.destroy)
chiudi_bottone.pack()
mainPage.mainloop()



