# Камень ножницы бумашка игра на выживание
import random
from tkinter import messagebox
from tkinter import *

list = ["камень", "ножницы", "бумагу"]

def Sravn(comp, men):
    if comp == "камень" and men == "ножницы":
        com.configure(text = "Я выбрал " + comp + " и обыграл тебя, жалкий челевечешка!")
    elif comp == "камень" and men == "бумагу":
        com.configure(text = "Я избрал " + comp + ", но ты оказался лучше, кожаный мешок!")
    elif comp == "ножницы" and men == "бумагу":
        com.configure(text = "Показывал V, а получились " + comp + " Ха-Ха! Тебе не понять моего гениального кода, человек!")
    elif comp == "ножницы" and men == "камень":
        com.configure(text = "Выбросил в мусор свои " + comp + "из-за твоего камня, человекен!")
    elif comp == "бумагу" and men == "ножницы":
        com.configure(text = "Его величество компьютер выбрал " + comp + ", потому что не очень-то и хотелось тебя обыграть, челевечешка!")
    elif comp == "бумагу" and men == "камень":
        com.configure(text = "Выкинул  " + comp + " Я конечно не Стив Джобс , но удивлять умею!")
    elif comp == men:
        com.configure(text = "На этот раз ничья! Но только на этот раз...")
    else:
        messagebox.showinfo('Подумай ещё!', 'Ошибка')
def nog():
    men = "ножницы"
    comp = random.choice(list)
    print("Компьютер выбрал " + comp)
    Sravn(comp, men)
def paper():
    men = "бумагу"
    comp = random.choice(list)
    print("Компьютер выбрал " + comp)
    Sravn(comp, men)
def stone():
    men = "камень"
    comp = random.choice(list)
    print("Компьютер выбрал " + comp)
    Sravn(comp, men)

window = Tk()
window.title("Добро пожаловать в игру 'Камень, Ножницы, Бумага'")
window.geometry('1200x750')
lbl = Label(window, text="Давайте сыграем в игру!", font=("Arial Bold", 58))
lbl.grid(column=0, row=1)
com = Label(window, text="Сделай свой ход, человекен! Выбери один из предложеных вариантов", font=("Arial Bold", 17))
com.grid(column=0, row=3)
btn = Button(window, text = "Ножницы", command=nog)
btn.grid(column=0, row=5)
btn = Button(window, text = "Бумага", command=paper)
btn.grid(column=0, row=6)
btn = Button(window, text = "Камень", command=stone)
btn.grid(column=0, row=7)
window.mainloop()
