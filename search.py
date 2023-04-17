import tkinter as tk
import sqlite3 as sql


def search(gos_nomer):
    gos_nomer = ("%" + gos_nomer + "%",)
    conn.cur.execute('''SELECT * FROM service WHERE gos_nomer LIKE ?''', gos_nomer)
    

conn = sql.connect("db/avtoservice.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS persone(id integer primary key, surname TEXT, 
            username TEXT,  patronymic TEXT, city TEXT, street TEXT, phfone INTEGER, email TEXT,
            sts integer, marka_auto text, model text, gos_nomer text, odometr integer, mydata text,
            description text)''')
conn.commit()

root = tk.Tk()
root.title("Поиск записи")
root.geometry("380x180+350+200")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="service.png"))

user_frame = tk.Frame(root)
user_frame.pack(fill=tk.BOTH)

new_user = tk.Label(user_frame, text="Поиск записи по гос номеру", font=("Times New Roman", 14), fg="green")
new_user.grid(row=0, column=0, columnspan=2, padx=55, pady=15)

search = tk.Label(user_frame, text="Поиск записи")
search.grid(row=1, column=0, sticky=tk.W, padx=18, pady=8)

search_entry = tk.Entry(user_frame, width=25)
search_entry.grid(row=1, column=1, padx=15, pady=8)


btn_submit = tk.Button(user_frame, text="Поиск", bg="lightblue", command=search)
btn_submit.grid(row=4, column=1, padx=18, pady=15, sticky=tk.E)

root.mainloop()