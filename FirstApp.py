import tkinter as tk
from random import randint, choice
from tkinter import messagebox
window = tk.Tk()  # обращаемся к классу Tk из модуля tk
window.title("My App")
window.resizable(width = False, height = False)# отсуствие растягивания
window.geometry("800x600")
window["bg"]="orange"

note=tk.Label(window, text="Добавить заметку",font=("Arial",10),bg="white")
note.place(x= 400,y = 25)
EnterNote=tk.Entry(fg="black",width=50)# поле ввода
EnterNote.place(x=300,y=65)

window.mainloop()
