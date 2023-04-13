import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3 as sq
import re
    

with  sq.connect("db/avtoservise.db") as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, 
                surname TEXT,
                username TEXT, 
                password TEXT)''')
    
def save_users():
    surname = ent_surname_user.get()
    username = ent_name_user.get()
    passwd = ent_password_user.get()
    cur.execute('''INSERT INTO users(surname, username, password) 
                   VALUES (?, ?, ?)''', 
                   (surname, username, passwd))
    conn.commit()
    
    if len(passwd) <7:
        mb.showinfo("Сохранение", f"Данные не сохранены {username}!\nДлина пароля должа быть не менее 7 символов.") 
    else:
        mb.showinfo("Сохранение", f"Данные записаны в базу данных {username}!")
    root.destroy()


root = tk.Tk()
root.title("Регистрация нового работника")
root.geometry("450x280")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="logo.png"))


lbl_new_user = ttk.Label(root, text="Регистрация нового работника")
lbl_new_user.grid(row=0, column=0, columnspan=2, padx=55, pady=15)
lbl_new_user.config(font=("Times New Roman", 18, "bold"), foreground="red")

lbl_surname_user = ttk.Label(root, text="Фамилия")
lbl_surname_user.grid(row=1, column=0, padx=15, pady=10, sticky=tk.W)
lbl_surname_user.config(font=("Times New Roman", 12, "bold"))
ent_surname_user = ttk.Entry(root)
ent_surname_user.grid(row=1, column=1, padx=15, pady=10)
ent_surname_user.config(font=("Times New Roman", 12), foreground="grey", width=30)

lbl_name_user = ttk.Label(root, text="Имя")
lbl_name_user.grid(row=2, column=0, padx=15, pady=10, sticky=tk.W)
lbl_name_user.config(font=("Times New Roman", 12, "bold"))
ent_name_user = ttk.Entry(root, validate="key")
ent_name_user.grid(row=2, column=1, padx=15, pady=10)
ent_name_user.config(font=("Times New Roman", 12), foreground="grey", width=30)

lbl_password_user = ttk.Label(root, text="Пароль")
lbl_password_user.grid(row=3, column=0, padx=15, pady=10, sticky=tk.W)
lbl_password_user.config(font=("Times New Roman", 12, "bold"))
ent_password_user = ttk.Entry(root, show="*")
ent_password_user.grid(row=3, column=1, padx=15, pady=10)
ent_password_user.config(font=("Times New Roman", 12), foreground="#000000", width=30)

btn_submit_db = ttk.Button(root, text="Сохранить", width=25, command=save_users)
btn_submit_db.grid(row=4, column=1, padx=35, pady=20, sticky=tk.NE)


root.mainloop()