import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3 as sq


def verification_users():
    """
    The function checks the user's login and password when logging in.\n
    Функция проверяет логин и пароль пользователя при входе в систему.
    """
    with  sq.connect("carservise.db") as conn:
        cur = conn.cursor()
        surname = ent_surname_user.get()
        username = ent_name_user.get()
        passwd = ent_password_user.get()
        x = f"SELECT surname, username, password FROM users WHERE surname == '{surname}' AND username == '{username}' AND password == '{passwd}';"
        cur.execute(x)
            
        if not cur.fetchall():
            mb.showinfo("Регистрация работника", "Логин или пароль не совпадает!")
            return False
        else:    
            mb.showinfo("Регистрация работника", "Вы авторизованы!")
            root.destroy()


root = tk.Tk()
root.title("Авторизация")
root.geometry("470x300")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="logo.png"))


lbl_new_user = ttk.Label(root, text="Авторизация работника")
lbl_new_user.grid(row=0, column=0, columnspan=2, padx=55, pady=15)
lbl_new_user.config(font=("Times New Roman", 16), foreground="red")

lbl_surname_user = ttk.Label(root, text="Фамилия")
lbl_surname_user.grid(row=1, column=0, padx=15, pady=10, sticky=tk.W)
lbl_surname_user.config(font=("Times New Roman", 12))
ent_surname_user = ttk.Entry(root)
ent_surname_user.grid(row=1, column=1, padx=15, pady=10)
ent_surname_user.config(font=("Times New Roman", 12), foreground="grey", width=30)

lbl_name_user = ttk.Label(root, text="Имя")
lbl_name_user.grid(row=2, column=0, padx=15, pady=10, sticky=tk.W)
lbl_name_user.config(font=("Times New Roman", 12))
ent_name_user = ttk.Entry(root)
ent_name_user.grid(row=2, column=1, padx=15, pady=10)
ent_name_user.config(font=("Times New Roman", 12), foreground="grey", width=30)

lbl_password_user = ttk.Label(root, text="Пароль*")
lbl_password_user.grid(row=3, column=0, padx=15, pady=10, sticky=tk.W)
lbl_password_user.config(font=("Times New Roman", 12))
ent_password_user = ttk.Entry(root, show="*")
ent_password_user.grid(row=3, column=1, padx=15, pady=10)
ent_password_user.config(font=("Times New Roman", 12), foreground="#000000", width=30)

lbl_new_user = ttk.Label(root, text="* Пароль должен состоять из строчных и заглавных букв, цифр и спецсимволов", foreground="blue")
lbl_new_user.grid(row=4, column=0, columnspan=2, padx=35, pady=5, sticky=tk.W)
lbl_new_user.config(font=("Times New Roman", 9, "italic"))

btn_submit_db = ttk.Button(root, text="Войти", width=25, command=verification_users)
btn_submit_db.grid(row=5, column=1, padx=35, pady=20, sticky=tk.NE)

root.mainloop()