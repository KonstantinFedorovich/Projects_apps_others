import tkinter as tk
from random import randint, choice
from tkinter import messagebox
i=0
def left_button_click():
    global i
    label.config(text="You`ve clicked")
    i=i+1
    label2 = tk.Label(window, text="Вы нажали на кнопку " + str(i) + " раз")
    label2.pack(pady=20)
window = tk.Tk()  # обращаемся к классу Tk из модуля tk
window.title("My App")
window.geometry("800x600")
label = tk.Label(window,text="Text of app")
label.pack(pady=10)
button=tk.Button(window,text="Click",command=left_button_click)
button.pack(pady=20)
window.mainloop()
