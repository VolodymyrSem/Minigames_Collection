import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as font
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

font = font.Font(family='Comic Sans', size=9)

calc = tk.Button(root,
                 text='TRY!',
                 textvariable='pocket_calculator.pyw',
                 bg='lightblue',
                 width=15,
                 height=2,
                 font=font)
catch = tk.Button(root,
                  text='PLAY!',
                  textvariable='catch_me.pyw',
                  bg='lightblue',
                  width=15,
                  height=2,
                  font=font)
tictactoe = tk.Button(root,
                      text='PLAY!',
                      textvariable='tic_tac_toe.pyw',
                      bg='lightblue',
                      width=15,
                      height=2,
                      font=font)
clicker = tk.Button(root,
                    text='PLAY!',
                    textvariable='clicker_game.pyw',
                    bg='lightblue',
                    width=15,
                    height=2,
                    font=font)
sudoku = tk.Button(root,
                   text='PLAY!',
                   textvariable='sudoku_game.pyw',
                   bg='lightblue',
                   width=15,
                   height=2,
                   font='ComicSans 13')


calc.bind('<Button-1>', click)
catch.bind('<Button-1>', click)
tictactoe.bind('<Button-1>', click)
clicker.bind('<Button-1>', click)
sudoku.bind('<Button-1>', click)

calc.place(x=755, y=420)
catch.place(x=822, y=230)
tictactoe.place(x=200, y=270)
clicker.place(x=82, y=421)
sudoku.place(x=438, y=340)

root.mainloop()