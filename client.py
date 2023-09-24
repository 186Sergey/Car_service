import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import messagebox as mb
import sqlite3 as sql

current_date = date.today().strftime("%d-%m-%Y")

with sql.connect("carservise.db") as conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS persone(
        id INTEGER PRIMARY KEY, 
        surname TEXT, 
        username TEXT, 
        phfone INTEGER, 
        marka_auto TEXT, 
        model TEXT, 
        gos_nomer TEXT, 
        odometr INTEGER,
        email TEXT, 
        mydata TEXT, 
        description TEXT)''')
    conn.commit()


def client():
    '''Функция о сведениях о клиенте и транспортном средстве
    '''
    mydata = combo_mydata.get() #Дата текущая
    surname = entry_surname.get() #Фамилия
    username = entry_username.get() #Имя
    phfone = entry_phfone.get() #Телефон
    marka_auto = entry_marka_auto.get() # Марка автомобиля
    model = entry_model.get() # Модель автомобиля
    gos_nomer = entry_gos_nomer.get() #Государственный номер
    odometr = entry_odometr.get() #Пробег по одометру
    email = entry_email.get() #email
    description = field_problem.get("1.0", tk.END)# описание о неисправности
    cur.execute('''INSERT INTO persone(mydata, surname, username, phfone, marka_auto, model, gos_nomer, odometr, email, description) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (mydata, surname, username, phfone, marka_auto, model, gos_nomer, odometr, email, description))
    conn.commit()
    mb.showinfo("Всё получилось", "Данные записаны в базу данных!")
    root.destroy()

root = tk.Tk()
root.title("Сведения о клиенте и транспортном средстве")
root.geometry("1200x500+50+200")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="logo.png"))

def validate(input):
    """
    The function checks the Entry field for characters entered by the user from the keyboard,\
        letters must be entered.\n
    Функция проверяет поле Entry на вводимые символы пользователем с клавиатуры,\
        должны быть введены буквы.
    """
    return input.isalpha()
valid = root.register(validate)

topframe = tk.Frame(root)
topframe.pack(side=tk.TOP)

label = tk.Label(topframe, text="Сведения о клиенте и транспортном средстве", font=("Times New Roman", 14),
                 fg="green")
label.grid(row=0, column=0, columnspan=6, padx=150, pady=20)

'''Первый ряд'''

service_detal = tk.LabelFrame(topframe, text="Сведения о клиенте и транспортном средстве", fg='green', font=("Times New Roman", 12))
service_detal.grid(row=1, column=0, columnspan=6, padx=10, pady=20)

'''ФАМИЛИЯ'''

surname = tk.Label(service_detal, text="Фамилия")
surname.grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
entry_surname = tk.Entry(service_detal, width=30)#, validate="key",validatecommand=(valid,"%S")
entry_surname.grid(row=2, column=1, sticky=tk.W, padx=10, pady=8)

'''ИМЯ'''

username = tk.Label(service_detal, text="Имя")
username.grid(row=2, column=2, sticky=tk.W, padx=10, pady=8)
entry_username = tk.Entry(service_detal, width=30)#, validate="key",validatecommand=(valid,"%S")
entry_username.grid(row=2, column=3, sticky=tk.W, padx=10, pady=8)

'''ТЕЛЕФОН'''

phfone = tk.Label(service_detal, text="Телефон *")
phfone.grid(row=2, column=4, sticky=tk.W, padx=10, pady=8)
entry_phfone = tk.Entry(service_detal, width=30)
entry_phfone.grid(row=2, column=5, sticky=tk.W, padx=10, pady=8)


'''Марка'''

marka_auto = tk.Label(service_detal, text="Марка *")
marka_auto.grid(row=3, column=0, sticky=tk.W, padx=10, pady=8)
entry_marka_auto = tk.Entry(service_detal, width=30)#, validate="key",validatecommand=(valid,"%S")
entry_marka_auto.grid(row=3, column=1, sticky=tk.W, padx=10, pady=8)

'''Модель'''

model = tk.Label(service_detal, text="Модель *")
model.grid(row=3, column=2, sticky=tk.W, padx=10, pady=8)
entry_model = tk.Entry(service_detal, width=30)
entry_model.grid(row=3, column=3, sticky=tk.W, padx=10, pady=8)

'''Государственный номер'''

gos_nomer = tk.Label(service_detal, text="Гос. номер *")
gos_nomer.grid(row=3, column=4, sticky=tk.W, padx=10, pady=8)
entry_gos_nomer = tk.Entry(service_detal, width=30)
entry_gos_nomer.grid(row=3, column=5, sticky=tk.W, padx=10, pady=8)

'''Одометр'''

odometr = tk.Label(service_detal, text="Одометр *")
odometr.grid(row=4, column=0, sticky=tk.W, padx=10, pady=8)
entry_odometr = tk.Entry(service_detal, width=30)
entry_odometr.grid(row=4, column=1, sticky=tk.W, padx=10, pady=8)

'''EMAIL'''

email = tk.Label(service_detal, text="Email")
email.grid(row=4, column=2, sticky=tk.W, padx=10, pady=8)
entry_email = tk.Entry(service_detal, width=30)
entry_email.grid(row=4, column=3, sticky=tk.W, padx=10, pady=8)


'''Текущая дата'''

mydata = tk.Label(service_detal, text="Дата")
mydata.grid(row=4, column=4, sticky=tk.W, padx=10, pady=8)
combo_mydata = ttk.Combobox(service_detal, width=27, values=current_date, state='readonly')
combo_mydata.current("0")
combo_mydata.grid(row=4, column=5, sticky=tk.W, padx=10, pady=8)

problem = tk.LabelFrame(service_detal, text="Сведения о неисправности транспортного средства", fg='green', font=("Times New Roman", 12))
problem.grid(row=5, column=0, columnspan=6, padx=10, pady=20)

field_problem = tk.Text(problem, width=140, height=5, wrap=tk.WORD, padx=5, pady=5)
field_problem.grid(row=6, column=0, columnspan=6)

scroll = tk.Scrollbar(problem, orient="vertical", bg="lightblue", width=14, command=field_problem.yview)
scroll.grid(row=6, column=5, sticky="ENS")
field_problem.config(font=("Times New Roman", 12), yscrollcommand=scroll.set)


statusBar = tk.Label(service_detal, relief="flat", anchor="w", text="Поля отмеченные *, обязательны для заполнения",
                     fg="red", font=("Times New Roman", 10, "bold"))
statusBar.grid(row=7, column=0, columnspan=6, sticky=tk.E, padx=10)


'''КНОПКА ЗАПИСИ'''

btn_send = tk.Button(topframe, text="Сохранить", width=28, bg="lightblue", command=client)
btn_send.grid(row=8, column=5, columnspan=5, sticky=tk.E, padx=10, pady=8)


root.mainloop()
