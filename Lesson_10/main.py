from tkinter import *
from tkinter import messagebox
import funcs

mainWindow = Tk()
width = 700
height = 400

screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()

x_offset = (screen_width - width) // 2
y_offeset = (screen_height - height) // 2

mainWindow.geometry(f"{width}x{height}+{x_offset}+{y_offeset}")


mainWindow.title("Викторина Бобика")
mainWindow.resizable(False, False)


QUEST = Label(text="", font=("Comic Sans MS", 16))
QUEST.place(anchor="center",relx=0.5, rely=0.15)

info = Label(text="", font=("Comic Sans MS", 12), fg="red")
info.place(anchor="center",relx=0.5, rely=0.25)


buttons = []

for i in range(1, 5):
    btn = Button(width=50, height=1, font=("Comic Sans MS", 14))
    btn.config(command=lambda b=btn: funcs.choise(b, QUEST, buttons, info))
    btn.place(anchor="center", relx=0.5, rely=0.25+0.15*i)
    buttons.append(btn)


funcs.generate_quest(QUEST, buttons)















mainWindow.mainloop()