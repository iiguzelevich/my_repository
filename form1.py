from tkinter import *

import re


def write_txt(data):
    with open('inf.txt', 'a') as file:
        file.write(data + '\n')


def clicked():
    txt_write_1 = txt_1.get()
    txt_write_2 = txt_2.get()
    txt_write_3 = txt_3.get()
    txt_write_4 = txt_4.get()
    txt_write_5 = txt_5.get()
    if not re.findall(r'[а-яА-Я]{2,20}', txt_write_1):
        lbl_6.configure(text='Фамилия введена неправильна')
    elif not re.findall(r'[а-яА-Я]{2,12}', txt_write_2):
        lbl_6.configure(text='Имя введено неправильно')
    elif not re.findall(r'[а-яА-Я]{2,20}', txt_write_3):
        lbl_6.configure(text='Отчествово введено неправильно')
    elif not re.findall(r'[0-9]{11}', txt_write_4):
        lbl_6.configure(text='Номер телефона введен неправильно')
    elif not re.findall(r'(\w+@\w+.\w+)', txt_write_5):
        lbl_6.configure(text='Email введен неправильно')
    else:
        with open('inf.txt', 'a') as file:
            file.write(
                f'{txt_write_1}\n\
{txt_write_2}\n\
{txt_write_3}\n\
{txt_write_4}\n\
{txt_write_5}\n\
\n'
            )


form = Tk()

form.geometry('300x200')

lbl_1 = Label(form, text='Фамилия')
lbl_2 = Label(form, text='Имя')
lbl_3 = Label(form, text='Отчествово')
lbl_4 = Label(form, text='Номер телефона')
lbl_5 = Label(form, text='Email')
lbl_6 = Label(form, )

lbl_1.grid(column=0, row=0)
lbl_2.grid(column=0, row=1)
lbl_3.grid(column=0, row=2)
lbl_4.grid(column=0, row=3)
lbl_5.grid(column=0, row=4)
lbl_6.grid(column=0, row=6)

txt_1 = Entry(form, width=20)
txt_2 = Entry(form, width=20)
txt_3 = Entry(form, width=20)
txt_4 = Entry(form, width=20)
txt_5 = Entry(form, width=20)

txt_1.grid(column=1, row=0)
txt_2.grid(column=1, row=1)
txt_3.grid(column=1, row=2)
txt_4.grid(column=1, row=3)
txt_5.grid(column=1, row=4)

btn = Button(form, text='Отправить', command=clicked)
btn.grid(column=0, row=5)

form.mainloop()
