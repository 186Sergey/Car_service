import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3 as sq



with  sq.connect("db/avtoservise.db") as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, 
                surname TEXT,
                username TEXT, 
                password TEXT)''')


def fargout():
    """
    The function updates the password if the user has forgotten it.\n
    Функция обновляет пароль, если пользователь забыл его.
    """
    surname = ent_surname_user.get()
    passwd = ent_password_user.get()
    cur.execute("""UPDATE users SET password = ? WHERE surname = ?""", (passwd, surname))
    
    if len(passwd) < 6:
        mb.showinfo("Восстановление", "Длина пароля должна быть не менее 6 символов.") 
        return False
    else:
        mb.showinfo("Восстановление", "Пароль изменён!")
    
    conn.commit()    
    root.destroy()


root = tk.Tk()
root.title("Восстановление пароля")
root.geometry("450x250")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="logo.png"))


lbl_new_user = ttk.Label(root, text="Восстановление пароля")
lbl_new_user.grid(row=0, column=0, columnspan=2, padx=55, pady=15)
lbl_new_user.config(font=("Times New Roman", 18, "bold"), foreground="red")

lbl_surname_user = ttk.Label(root, text="Фамилия")
lbl_surname_user.grid(row=1, column=0, padx=15, pady=10, sticky=tk.W)
lbl_surname_user.config(font=("Times New Roman", 12, "bold"))
ent_surname_user = ttk.Entry(root)
ent_surname_user.grid(row=1, column=1, padx=15, pady=10)
ent_surname_user.config(font=("Times New Roman", 12), foreground="grey", width=30)

lbl_password_user = ttk.Label(root, text="Новый пароль")
lbl_password_user.grid(row=2, column=0, padx=15, pady=10, sticky=tk.W)
lbl_password_user.config(font=("Times New Roman", 12, "bold"))
ent_password_user = ttk.Entry(root, show="*")
ent_password_user.grid(row=2, column=1, padx=15, pady=10)
ent_password_user.config(font=("Times New Roman", 12), foreground="#000000", width=30)

lbl_new_user = ttk.Label(root, text="* Пароль должен состоять из строчных и заглавных букв,\
 цифр и спецсимволов")
lbl_new_user.grid(row=4, column=0, columnspan=2, padx=35, pady=5, sticky=tk.E)
lbl_new_user.config(font=("Times New Roman", 8, "bold"))

btn_submit_db = ttk.Button(root, text="Обновить", width=25, command=fargout)
btn_submit_db.grid(row=5, column=1, padx=35, pady=20, sticky=tk.NE)


root.mainloop()