import tkinter as tk


def open_window4():
    window4 =tk.Tk()
    window4.title("MENU'")
    window4.geometry("800x800")
    window4.resizable(False,False)
    sdaldo_button = tk.Button(window4, text="Inserisci")

    window4.mainloop()