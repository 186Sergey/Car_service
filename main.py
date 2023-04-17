# coding: utf-8
import tkinter as tk
from tkinter import messagebox as mb
import sqlite3 as sql



def myclose():
    if mb.askokcancel("Выход из приложения", "Вы точно хотите завершить работу приложения?"):
        root.destroy()

def table_klient():
    main_text.insert(tk.END, "Запись №:")
    main_text.insert(tk.END, "\nДата:")
    main_text.insert(tk.END, "\nФамилия:")
    main_text.insert(tk.END, "\nИмя:")
    main_text.insert(tk.END, "\nОтчество:")
    main_text.insert(tk.END, "\nГород:")
    main_text.insert(tk.END, "\nУлица:")
    main_text.insert(tk.END, "\nТелефон:")
    main_text.insert(tk.END, "\nEmail:")
    main_text.insert(tk.END, "\nСТС:")
    main_text.insert(tk.END, "\nМарка автомобиля:")
    main_text.insert(tk.END, "\nМодель автомобиля:")
    main_text.insert(tk.END, "\nГос. номер:")
    main_text.insert(tk.END, "\nОдометр:")
    main_text.insert(tk.END, "\nНеисправность:")
    main_text.insert(tk.END, "\n\n")
    main_text.insert(tk.END, "="*84+"\n\n")


with sql.connect("bases/service.db") as requisites:
    cur = requisites.cursor()
    cur.execute('''SELECT organisation FROM sto''')
    x = cur.fetchone()



with sql.connect("db/avtoservice.db") as client:
    cur = client.cursor()
    klient = ('''SELECT rowid, mydata,surname, username, patronymic, city, street,
                                       phfone, email, sts, marka_auto, model, gos_nomer, 
                                       odometr, description FROM persone''')
    cur.execute(klient)
    records = cur.fetchall()
    
    

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW', myclose)
root.title("Сведения о реквизитах СТО и собственнике")
root.geometry("825x900+250+20")
root.resizable(False, False)
root.iconphoto(True, tk.PhotoImage(file="service.png"))

maim_menu = tk.Menu(root)
root.configure(menu = maim_menu)

pervaja_kolonka = tk.Menu(maim_menu, tearoff=0)
maim_menu.add_cascade(label = "Файл", menu=pervaja_kolonka)
pervaja_kolonka.add_command(label="Добавить реквизиты")
pervaja_kolonka.add_command(label="Добавить работника")
pervaja_kolonka.add_command(label="Добавить запись")
pervaja_kolonka.add_separator()
pervaja_kolonka.add_command(label="Выход", command=myclose)

vtoraja_kolonka = tk.Menu(maim_menu, tearoff=0)
maim_menu.add_cascade(label = "Редактирование", menu=vtoraja_kolonka)
vtoraja_kolonka.add_command(label="Редактировать реквизиты")
vtoraja_kolonka.add_command(label="Редактировать запись")

tretya_kolonka = tk.Menu(maim_menu, tearoff=0)
maim_menu.add_cascade(label = "Сервис", menu=tretya_kolonka)
tretya_kolonka.add_command(label="Бэкап БД")
tretya_kolonka.add_command(label="Восстановить БД")

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, columnspan=5)

main_text_lbl = tk.Label(main_frame, text=x[0].upper(), font=("Times New Roman", 20, "bold"), fg="green")
main_text_lbl.grid(row=1, column=0, columnspan=5, padx=20, pady=20)

main_text = tk.Text(main_frame, width=95, height=30, wrap=tk.WORD)
main_text.grid(row=2, column=0, padx=15, pady=5)
main_text.insert(tk.END, records)


scroll = tk.Scrollbar(main_frame, orient="vertical", command=main_text.yview)
scroll.grid(row=2, column=0, sticky="ens")
main_text.config(font=("Times New Roman", 12), padx=15, pady=10, yscrollcommand=scroll.set)

statusBar = tk.Label(root, relief="sunken", anchor="w", 
                     fg="green", font=("Times New Roman", 14))
statusBar.grid(row=10, column=0, columnspan=5, sticky="w", padx=10)




               
root.mainloop()