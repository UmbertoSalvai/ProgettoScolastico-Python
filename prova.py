import tkinter as tk
from tkinter import messagebox




transazioniPage = tk.Tk()
transazioniPage.title("MENU'")
transazioniPage.geometry("600x600")
transazioniPage.resizable(False, False)
transazioniPage.configure(background="#00008B")

parte_superiore = tk.Frame(transazioniPage, bg="#FFFFFF")
parte_superiore.place(relx=0, rely=0, relwidth=1, relheight=0.2)

titolo_label = tk.Label(parte_superiore, text="THE BANK", font=("Arial", 30, "bold", "italic"), bg="#FFFFFF")
titolo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
button_style = {
    "font": ("Arial", 14),
    "width": 15,
    "height": 2,
    "bg": "#FFFFFF",
    "fg": "#000000",
    "activebackground": "#A9D2FF",
    "bd": 0,
}

avvia_ricerca_button = tk.Button(transazioniPage, command=,text="Avvia la ricerca", **button_style)


avvia_ricerca_button.pack(pady=(320, 0))

transazioniPage.mainloop()
