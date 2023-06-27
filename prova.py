import tkinter as tk
from tkinter import messagebox





# Create the main page window
mainPage = tk.Tk()
mainPage.title("Home")
mainPage.geometry("800x800")
mainPage.resizable(False, False)
mainPage.configure(background="#000000")

# Create a frame for the content
content_frame = tk.Frame(mainPage, bg="#000000")
content_frame.pack(pady=100)

# Create labels and buttons
welcome_label = tk.Label(content_frame, text="Welcome!", font=("Arial", 24), bg="#000000", fg="#FFFFFF")
welcome_label.pack(pady=20)

reg_button = tk.Button(content_frame, text="Register",  font=("Arial", 18), bg="#444444", fg="#FFFFFF", padx=20, pady=10)
reg_button.pack(pady=10)

login_button = tk.Button(content_frame, text="Login", font=("Arial", 18), bg="#444444", fg="#FFFFFF", padx=30, pady=10)
login_button.pack(pady=10)

exit_button = tk.Button(mainPage, text="Exit", command=mainPage.destroy, font=("Arial", 12), bg="#444444", fg="#FFFFFF", padx=10, pady=5)
exit_button.pack(pady=30)

mainPage.mainloop()
