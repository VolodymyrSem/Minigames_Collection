import tkinter as tk
from tkinter import messagebox
import random as rn
from PIL import ImageTk, Image


def away(event=None):
    global x
    global y
    x += rn.randint(70, 300)
    y += rn.randint(70, 300)
    if x > 440:
        x -= 440
    if y > 440:
        y -= 440
    button.place(x=x, y=y)

def win():
    messagebox.showinfo(title='YOU WIN', message='IS IT POSSIBLE?')

wn = tk.Tk()
wn.title('Catch me!')
wn.geometry('510x510')
wn.minsize(510, 510)
wn.maxsize(510, 510)
icon = ImageTk.PhotoImage(Image.open('img/icon.png'))
wn.iconphoto(True, icon)
bg = ImageTk.PhotoImage(Image.open('img/catchme_bg.png'))
background = tk.Label(wn, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(wn,
                   text='Catch me!',
                   takefocus='0',
                   borderwidth='3',
                   bg='lightgreen',
                   command=win,
                   width=8,
                   height=2)
button.bind('<Enter>', func=away)
x = 10
y = 10
button.place(x=x, y=y)

if __name__ == '__main__':
    tk.mainloop()