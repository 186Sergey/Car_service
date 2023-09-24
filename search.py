import tkinter as tk
import sqlite3 as sql
  

conn = sql.connect("carservice.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS persone(id integer primary key, surname TEXT, 
            username TEXT,  patronymic TEXT, city TEXT, street TEXT, phfone INTEGER, email TEXT,
            sts integer, marka_auto text, model text, gos_nomer text, odometr integer, mydata text,
            description text)''')
conn.commit()


def search():
    gos_nomer = search_entry.get()
    conn.cur.execute('''SELECT * FROM persone WHERE gos_nomer LIKE ?''', gos_nomer)

    print("gos_nomer")

root = tk.Tk()
root.title("Поиск записи")
root.geometry("390x180+350+200")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="logo.png"))

user_frame = tk.Frame(root)
user_frame.pack(fill=tk.BOTH)

new_user = tk.Label(user_frame, text="Поиск записи по гос номеру", font=("Times New Roman", 18), fg="red")
new_user.grid(row=0, column=0, columnspan=2, padx=55, pady=15)

search_lbl = tk.Label(user_frame, text="Поиск записи", font=("Times New Roman", 12))
search_lbl.grid(row=1, column=0, sticky=tk.W, padx=18, pady=8)

search_entry = tk.Entry(user_frame, width=27)
search_entry.grid(row=1, column=1, padx=18, pady=15, sticky=tk.W)


btn_submit = tk.Button(user_frame, text="Поиск", bg="lightblue", width=23, command=search)
btn_submit.grid(row=4, column=1, padx=18, pady=15, sticky=tk.W)


root.mainloop()