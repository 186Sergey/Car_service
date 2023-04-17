import tkinter as tk
from tkinter import messagebox as mb
import sqlite3 as sql


def verification():
    surname = new_user_surname_entry.get()
    username = new_user_username_entry.get()
    passwd = new_user_password_entry.get()
    x = f"SELECT surname, username, passwd FROM users WHERE surname = '{surname}' AND username = '{username}' AND passwd = '{passwd}';"
    cur.execute(x)
    
    if not cur.fetchall():
        mb.showinfo("Регистрация работника", f"{username}, пароль не совпадает!")
    else:    
        mb.showinfo("Регистрация работника", f"Вы авторизованы, {username}!")
        root.destroy()


conn = sql.connect("db/avtoservice.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users(id integer primary key, 
           surname TEXT, username TEXT, passwd TEXT)''')
conn.commit()


root = tk.Tk()
root.title("Вход работника")
root.geometry("380x250+350+200")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="service.png"))

user_frame = tk.Frame(root)
user_frame.pack(fill=tk.BOTH)

new_user = tk.Label(user_frame, text="Вход работника", font=("Times New Roman", 14), fg="green")
new_user.grid(row=0, column=0, columnspan=2, padx=55, pady=15)

new_user_surname = tk.Label(user_frame, text="Фамилия")
new_user_surname.grid(row=1, column=0, sticky=tk.W, padx=18, pady=8)

new_user_surname_entry = tk.Entry(user_frame, width=25)
new_user_surname_entry.grid(row=1, column=1, padx=15, pady=8)

new_user_username = tk.Label(user_frame, text="Имя")
new_user_username.grid(row=2, column=0, sticky=tk.W, padx=18, pady=8)

new_user_username_entry = tk.Entry(user_frame, width=25)
new_user_username_entry.grid(row=2, column=1, padx=15, pady=8)

new_user_password = tk.Label(user_frame, text="Пароль")
new_user_password.grid(row=3, column=0, sticky=tk.W, padx=18, pady=8)

new_user_password_entry = tk.Entry(user_frame, width=25, show="*")
new_user_password_entry.grid(row=3, column=1, padx=15, pady=8)

btn_submit = tk.Button(user_frame, text="Войти", width=23, bg="lightblue", command=verification)
btn_submit.grid(row=4, column=1, padx=18, pady=15, sticky=tk.E)

root.mainloop()