import tkinter as tk
from tkinter import messagebox as mb
import sqlite3 as sql
  

with  sql.connect("carservise.db") as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS oplata
                (id INTEGER PRIMARY KEY,
                kol INTEGER,
                payment TEXT)''')
    conn.commit()


def pay():
    """
    The function adds data about payment and repair costs\n
    Функция добавляет данные об оплате и затратах на ремонт
    """
    payment = pay_entry.get()
    kolich = kol_entry.get()
    cur.execute('''INSERT INTO oplata (kol, payment)
                VALUES (?, ?)''', 
                (kolich, payment))
    conn.commit()
    root.destroy()  


root = tk.Tk()
root.title("Оплата работы")
root.geometry("1085x240+350+200")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="logo.png"))

user_frame = tk.Frame(root)
user_frame.pack(fill=tk.BOTH)

payment_lbl = tk.Label(user_frame, text="Оплата работы", font=("Times New Roman", 18), fg="red")
payment_lbl.grid(row=0, column=0, columnspan=2, padx=55, pady=15)

kol_lbl = tk.Label(user_frame, text="Запчасти", font=("Times New Roman", 12))
kol_lbl.grid(row=1, column=0, sticky=tk.W, padx=18, pady=8)
kol_entry = tk.Entry(user_frame, width=150)
kol_entry.grid(row=1, column=1, padx=18, pady=15, sticky=tk.W)

pay_lbl = tk.Label(user_frame, text="Оплата работы", font=("Times New Roman", 12))
pay_lbl.grid(row=2, column=0, sticky=tk.W, padx=18, pady=8)
pay_entry = tk.Entry(user_frame, width=20)
pay_entry.grid(row=2, column=1, padx=18, pady=15, sticky=tk.W)




btn_submit = tk.Button(user_frame, text="Сохранить", bg="lightblue", width=16, command=pay)
btn_submit.grid(row=3, column=1, padx=18, pady=15, sticky=tk.W)


root.mainloop()