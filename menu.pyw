import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import sys


def click(event):
    global pyexec
    file = event.widget['textvariable']
    os.system(str(file))


root = tk.Tk()
root.geometry('1020x570')
root.minsize(1020, 570)
root.maxsize(1020, 570)
icon = ImageTk.PhotoImage(Image.open('img/icon.png'))
root.iconphoto(True, icon)
root.title('Main Menu')
root.configure(takefocus=1)

bg = ImageTk.PhotoImage(Image.open('img/Desktop (1).png'))
background = tk.Label(root, image=bg)
background.place(x=0, y=0, relwidth=1, relheight=1)

pyexec = sys.executable

calc = tk.Button(root,
                 text='CLICK!',
                 textvariable='pocket_calculator.pyw',
                 bg='lightblue',
                 width=15,
                 height=2)
catch = tk.Button(root,
                  text='CLICK!',
                  textvariable='catch_me.pyw',
                  bg='lightblue',
                  width=15,
                  height=2)
tictactoe = tk.Button(root,
                      text='CLICK!',
                      textvariable='tic_tac_toe.pyw',
                      bg='lightblue',
                      width=15,
                      height=2)
clicker = tk.Button(root,
                    text='CLICK!',
                    textvariable='clicker_game.pyw',
                    bg='lightblue',
                    width=15,
                    height=2)


calc.bind('<Button-1>', click)
catch.bind('<Button-1>', click)
tictactoe.bind('<Button-1>', click)
clicker.bind('<Button-1>', click)

calc.place(x=755, y=420)
catch.place(x=822, y=230)
tictactoe.place(x=200, y=270)
clicker.place(x=82, y=421)

root.mainloop()