
import tkinter as tk
import tkinter.font as tkFont

from Registrazione import RegistrazionePage
from Accedi import AccediPage

def click1():
    mainPage.destroy()
    RegistrazionePage()

def click2():
    mainPage.destroy()
    AccediPage()

# CREATION OF THE MAIN PAGE
mainPage = tk.Tk()
mainPage.title("Bank Website")
mainPage.geometry("800x800")
mainPage.resizable(False, False)
mainPage.configure(background="#00008B")  # Light blue background color

# Styling for buttons
button_style = {
    "font": ("Arial", 14),
    "width": 15,
    "height": 2,
    "bg": "#FFFFFF",  # Light blue background color
    "fg": "#000000",  # Black text color
    "activebackground": "#A9D2FF",  # Lighter shade of blue when button is clicked
    "bd": 0,  # Border width
}

parte_superiore = tk.Frame(mainPage, bg="#FFFFFF")
parte_superiore.place(relx=0, rely=0, relwidth=1, relheight=0.2)


nome_banca_label = tk.font.Font(family="Arial", size=30, weight="bold", slant="italic")
nome_banca_label_label = tk.Label(parte_superiore, text="THE BANK", font=nome_banca_label,bg=parte_superiore["bg"])
nome_banca_label_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# First button - REGISTRATI!
primo_bottone = tk.Button(text="REGISTRATI!", command=click1, **button_style)
primo_bottone.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Second button - ACCEDI!
secondo_bottone = tk.Button(text="ACCEDI!", command=click2, **button_style)
secondo_bottone.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Close button
chiudi_bottone = tk.Button(text="Chiudi", command=mainPage.destroy, bg="#FF0000", fg="#FFFFFF", font=("Arial", 12))
chiudi_bottone.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

mainPage.mainloop()
