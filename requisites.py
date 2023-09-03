import tkinter as tk
from tkinter import messagebox as mb
import sqlite3 as sql




conn = sql.connect("db/avtoservise.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS service(id integer primary key, organisation TEXT, 
            region TEXT, city TEXT, street TEXT, myindex integer, surname TEXT, username TEXT, 
            patronymic TEXT, phfone INTEGER, fax INTEGER, email TEXT)''')
conn.commit()

'''Сведения о реквизитах СТО и собственнике'''

def records():
    organisation = entry_organisation.get()
    region = entry_region.get()
    city = entry_city.get()
    street = entry_street.get()
    myindex = entry_myindex.get()
    surname = entry_surname.get()
    username = entry_username.get()
    patronymic = entry_patronymic.get()
    phfone = entry_phfone.get()
    fax = entry_fax.get()
    email = entry_email.get()
    cur.execute('''INSERT INTO service(organisation, region, city, street, myindex, 
                                       surname, username, patronymic,
                                       phfone, fax, email) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (organisation, region, city, street, myindex, surname, username, patronymic,
                    phfone, fax, email))
    conn.commit()
    mb.showinfo("Всё получилось", "Данные записаны в базу данных!")
    root.destroy()


root = tk.Tk()
root.title("Сведения о реквизитах СТО и собственнике")
root.geometry("1200x550+50+200")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="service.png"))

# def validate(input):
#     """
#     The function checks the Entry field for characters entered by the user from the keyboard,\
#         letters must be entered.\n
#     Функция проверяет поле Entry на вводимые символы пользователем с клавиатуры,\
#         должны быть введены буквы.
#     """
#     return input.isalpha()
# valid = root.register(validate)

topframe = tk.Frame(root)
topframe.pack(side=tk.TOP)

label = tk.Label(topframe, text="Сведения о реквизитах СТО и собственнике", font=("Times New Roman", 14),
                 fg="green")
label.grid(row=0, column=0, columnspan=6, padx=150, pady=20)

'''Первый ряд'''

service_detal = tk.LabelFrame(topframe, text="Сведения о собственнике и реквизитах СТО")
service_detal.grid(row=1, column=0, columnspan=6, padx=10, pady=20)

'''Второй ряд НАЗВАНИЕ ОРГАНИЗАЦИИ'''

organisation = tk.Label(service_detal, text="Организация")
organisation.grid(row=2, column=0, sticky=tk.W, padx=10, pady=8)
entry_organisation = tk.Entry(service_detal, width=128)
entry_organisation.grid(row=2, column=1, columnspan=6, sticky=tk.E, padx=10, pady=8)

'''Третий ряд НАЗВАНИЕ РЕГИОНА СТРАНЫ'''

region = tk.Label(service_detal, text="Регион")
region.grid(row=3, column=0, sticky=tk.W, padx=10, pady=8)
entry_region = tk.Entry(service_detal, width=128)
entry_region.grid(row=3, column=1, columnspan=6, sticky=tk.E, padx=10, pady=8)

'''Четвёртый ряд НАЗВАНИЕ ГОРОДА'''

city = tk.Label(service_detal, text="Город")
city.grid(row=4, column=0, sticky=tk.W, padx=10, pady=8)
entry_city = tk.Entry(service_detal, width=30, validate="key")#,validatecommand=(valid,"%S")
entry_city.grid(row=4, column=1, sticky=tk.E, padx=10, pady=8)

'''Четвёртый ряд НАЗВАНИЕ УЛИЦЫ'''

street = tk.Label(service_detal, text="Улица, дом, корпус")
street.grid(row=4, column=2, sticky=tk.W, padx=10, pady=8)
entry_street = tk.Entry(service_detal, width=30)
entry_street.grid(row=4, column=3, sticky=tk.E, padx=10, pady=8)

'''Четвёртый ряд  Индекс'''

myindex = tk.Label(service_detal, text="Индекс")
myindex.grid(row=4, column=4, sticky=tk.W, padx=10, pady=8)
entry_myindex = tk.Entry(service_detal, width=30)
entry_myindex.grid(row=4, column=5, sticky=tk.E, padx=10, pady=8)

'''Пятый ряд ФАМИЛИЯ'''

surname = tk.Label(service_detal, text="Фамилия")
surname.grid(row=5, column=0, sticky=tk.W, padx=10, pady=8)
entry_surname = tk.Entry(service_detal, width=30, validate="key")#,validatecommand=(valid,"%S")
entry_surname.grid(row=5, column=1, sticky=tk.E, padx=10, pady=8)

'''Пятый ряд ИМЯ'''


username = tk.Label(service_detal, text="Имя")
username.grid(row=5, column=2, sticky=tk.W, padx=10, pady=8)
entry_username = tk.Entry(service_detal, width=30, validate="key")#,validatecommand=(valid,"%S")
entry_username.grid(row=5, column=3, sticky=tk.E, padx=10, pady=8)

'''Пятый ряд ОТЧЕСТВО'''


patronymic = tk.Label(service_detal, text="Отчество")
patronymic.grid(row=5, column=4, sticky=tk.W, padx=10, pady=8)
entry_patronymic = tk.Entry(service_detal, width=30, validate="key")#,validatecommand=(valid,"%S"))
entry_patronymic.grid(row=5, column=5, sticky=tk.E, padx=10, pady=8)

'''ШЕСТОЙ РЯД ТЕЛЕФОН'''

phfone = tk.Label(service_detal, text="Телефон")
phfone.grid(row=6, column=0, sticky=tk.W, padx=10, pady=8)
entry_phfone = tk.Entry(service_detal, width=30)
entry_phfone.grid(row=6, column=1, sticky=tk.E, padx=10, pady=8)

'''ШЕСТОЙ РЯД ФАКС'''


fax = tk.Label(service_detal, text="Факс")
fax.grid(row=6, column=2, sticky=tk.W, padx=10, pady=8)
entry_fax = tk.Entry(service_detal, width=30)
entry_fax.grid(row=6, column=3, sticky=tk.E, padx=10, pady=8)

'''ШЕСТОЙ РЯД EMAIL'''


email = tk.Label(service_detal, text="Email")
email.grid(row=6, column=4, sticky=tk.W, padx=10, pady=8)
entry_email = tk.Entry(service_detal, width=30)
entry_email.grid(row=6, column=5, sticky=tk.E, padx=10, pady=8)

'''СЕДЬМОЙ РЯД КНОПКА ЗАПИСИ'''


btn_send = tk.Button(service_detal, text="Сохранить", width=25, bg="lightblue", command=records)
btn_send.grid(row=7, column=5, columnspan=6, sticky=tk.E, padx=10, pady=8)


root.mainloop()
