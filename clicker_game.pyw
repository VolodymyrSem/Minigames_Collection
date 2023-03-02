import tkinter as tk
from tkinter import Button
from tkinter import messagebox
from random import randint
import random as rn
from functools import partial
import time
from PIL import ImageTk, Image


def timer_fun():
    global timer_val, after_id
    timer_val += 1
    timer.config(text=timer_val)
    after_id = timer.after(1000, timer_fun)

def click(txt):
    global timer_var
    if not timer_var:
        timer_var = True
        timer.after(1000, timer_fun)
    if txt == min(rand_lst):
        rand_lst.remove(txt)
        obj_dct[txt].config(state='disabled')
        if rand_lst == []:
            timer_var = False
            timer.after_cancel(after_id)
            messagebox.showinfo(title='Congratulations!',
                                message='YOU WIN!\nThat time you\'ve spent {} seconds!'.format(timer_val))


wn = tk.Tk()
wn.title('Clicker Game')
wn.configure(bg='#3FFF9F')
icon = ImageTk.PhotoImage(Image.open('img/icon.png'))
wn.iconphoto(True, icon)

rand_lst = rn.sample(range(1, 999), 25)
obj_dct = {name: Button(wn,
                        text=name,
                        height=1,
                        width=10,
                        command=partial(click, name),
                        bg='#68FFB4',
                        activebackground='#00FF80',
                        font='Consolas 11') for name in rand_lst}
x = 0
y = 0
for el in obj_dct.keys():
    obj_dct[el].grid(row=x, column=y)
    x += 1
    if x > 4:
        x = 0
        y += 1

timer_val = 0
timer_var = False
timer = tk.Label(wn, text=0, bg='#3FFF9F', width=29, font='Consolas 21')
timer.grid(row=5, columnspan=5)

if __name__ == '__main__':
    wn.mainloop()
