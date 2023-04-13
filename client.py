import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3 as sq



root = tk.Tk()
root.title("Информация об автомобиле и клиенте")
root.geometry("750x480")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="logo.png"))



root.mainloop()