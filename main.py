# coding: utf-8
import tkinter as tk
from tkinter import messagebox as mb
import sqlite3 as sql



def myclose():
    """
    The function asks the user if he really wants to shut down the application\n
    Функция спрашивает пользователя о том, точно ли он хочет завершить работу приложения
    """
    if mb.askokcancel("Выход из приложения", "Вы точно хотите завершить работу приложения?"):
        root.destroy()


with sql.connect("db/avtoservise.db") as requisites:
    cur = requisites.cursor()
    cur.execute('''SELECT organisation FROM service''')
    x = cur.fetchone()



with sql.connect("db/avtoservise.db") as client:
    cur = client.cursor()
    klient = ('''SELECT rowid, mydata, surname, username, patronymic, city, street,
                        phfone, email, sts, marka_auto, model, gos_nomer, odometr, 
                        description FROM persone''')
    cur.execute(klient)
    records = cur.fetchall()
    for rez in records:
        c = list(rez)
        print("Запись №:", c[0])
        print("Дата:", c[1])
        print("Фамилия:", c[2])
        print("Имя:", c[3])
        print("Отчество:", c[4])
        print("Город:", c[5])
        print("Улица:", c[6])
        print("Телефон:", c[7])
        print("Email:", c[8])
        print("СТС:", c[9])
        print("Марка автомобиля:", c[10])
        print("Модель автомобиля:", c[11])
        print("Гос. номер:", c[12])
        print("Одометр:", c[13])
        print("Неисправность:", c[14])
        print("\n\n")
        print("="*84+"\n\n")

        



def table_klient():
    main_text.insert(tk.END, "Запись №:", c[0:])
    main_text.insert(tk.END, "\nДата:", c[1:])
    main_text.insert(tk.END, "\nФамилия:", c[2])
    main_text.insert(tk.END, "\nИмя:", c[3])
    main_text.insert(tk.END, "\nОтчество:", c[4])
    main_text.insert(tk.END, "\nГород:", c[5])
    main_text.insert(tk.END, "\nУлица:", c[6])
    main_text.insert(tk.END, "\nТелефон:", c[7])
    main_text.insert(tk.END, "\nEmail:", c[8])
    main_text.insert(tk.END, "\nСТС:", c[9])
    main_text.insert(tk.END, "\nМарка автомобиля:", c[10])
    main_text.insert(tk.END, "\nМодель автомобиля:", c[11])
    main_text.insert(tk.END, "\nГос. номер:", c[11])
    main_text.insert(tk.END, "\nОдометр:", c[12])
    main_text.insert(tk.END, "\nНеисправность:", c[13])
    main_text.insert(tk.END, "\n\n")
    main_text.insert(tk.END, "="*84+"\n")

with sql.connect("db/avtoservise.db") as bqbd:
        cur = bqbd.cursor()

def backupdb():
    """
    The function should make a backup copy of the database (completely)\n
    Функция должна делать резервную копию БД (полностью)
    """
    with open("sql_damp.sql", "w") as f:
        for sql in bqbd.iterdump():
            f.write(sql)

# def restore():
    """
    The function should restore the database from a backup\n
    Функция должна восстанавливать БД из резервной копии 
    """
#     with open("sql_damp.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)   
    

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW', myclose)
root.title("Сведения о реквизитах СТО и собственнике")
root.geometry("825x900+250+20")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="service.png"))

maim_menu = tk.Menu(root)
root.configure(menu = maim_menu)

first_column = tk.Menu(maim_menu, tearoff=0)
maim_menu.add_cascade(label = "Файл", menu=first_column)
first_column.add_command(label="Добавить реквизиты")
first_column.add_command(label="Добавить работника")
first_column.add_command(label="Добавить запись")
first_column.add_separator()
first_column.add_command(label="Выход", command=myclose)

second_column = tk.Menu(maim_menu, tearoff=0)
maim_menu.add_cascade(label = "Редактирование", menu=second_column)
second_column.add_command(label="Редактировать реквизиты")
second_column.add_command(label="Редактировать запись")

third_column = tk.Menu(maim_menu, tearoff=0)
maim_menu.add_cascade(label = "Сервис", menu=third_column)
third_column.add_command(label="Восстановить пароль")
third_column.add_command(label="Бэкап БД", command=backupdb)
third_column.add_command(label="Восстановить БД")

fourth_column = tk.Menu(maim_menu, tearoff=0)
maim_menu.add_cascade(label = "Помощь", menu=fourth_column)
fourth_column.add_command(label="О программе")
fourth_column.add_command(label="Помощь")

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, columnspan=5)

main_text_lbl = tk.Label(main_frame, text=x[0].upper(), font=("Times New Roman", 20, "bold"), fg="green")
main_text_lbl.grid(row=1, column=0, columnspan=5, padx=20, pady=20)

main_text = tk.Text(main_frame, width=95, height=30, wrap=tk.WORD)
main_text.grid(row=2, column=0, padx=15, pady=5)
table_klient()
#table_klient()


scroll = tk.Scrollbar(main_frame, orient="vertical", command=main_text.yview)
scroll.grid(row=2, column=0, sticky="ens")
main_text.config(font=("Times New Roman", 12), padx=15, pady=10, yscrollcommand=scroll.set)

statusBar = tk.Label(root, relief="sunken", anchor="w", fg="green", font=("Times New Roman", 14))
statusBar.grid(row=10, column=0, columnspan=5, sticky="w", padx=10)

               
root.mainloop()