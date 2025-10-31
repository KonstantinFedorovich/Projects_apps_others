import tkinter as tk
from random import randint, choice
from tkinter import messagebox

def AddNote():
    value=EnterNote.get()
    if value!='':
        with open('Notes.txt','a+',encoding = "utf-8") as file:
            file.write(value + '\n')
        EnterNote.delete(0,'end')
    else:
        tk.messagebox.showinfo("Ошибка","Невозможно записать пустое значение")

def ViewNote():
    with open("Notes.txt","r",encoding= "utf-8") as file:
        lines = file.readlines()
        tk.messagebox.showinfo("Заметки:",lines)




window = tk.Tk()  # обращаемся к классу Tk из модуля tk
window.title("My App")
window.resizable(width = False, height = False)# отсуствие растягивания
window.geometry("800x600")
window["bg"]="orange"

note=tk.Label(window, text="Добавить заметку",font=("Arial",15),bg="orange")
note.place(x= 400,y = 25)
EnterNote=tk.Entry(fg="black",width=50)# поле ввода
EnterNote.place(x=300,y=65)

button=tk.Button(window, text= "Добавить заметку",command=AddNote,width=42,height=2,fg="black",bg="white")
button.place(x=300,y=110)

GiveNote=tk.Label(window, text="Вытащить заметку",font=("Arial Bold",15),fg="black",bg="orange")
GiveNote.place(x= 380,y = 180)

GiveNoteButton=tk.Button(window, text= "Вытащить заметку",command=ViewNote,width=42,height=2,fg="black",bg="white")
GiveNoteButton.place(x=300,y=250)



window.mainloop()
