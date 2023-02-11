import customtkinter as ctk
from dokusan import generators, solvers
from dokusan.entities import Sudoku, BoxSize
from tkinter import messagebox
from tkinter import Menu
import numpy as np
import os
from functools import partial
from PIL import ImageTk, Image


def main(diff):
    global rank
    if diff == 1:
        rank = 50
    elif diff == 2:
        rank = 300
    elif diff == 3:
        rank = 500
    elif diff == 4:
        rank = 900
    root.destroy()


def entry_limit(*args):
    global last_txt, text_var_entry
    txt = text_var_entry.get()
    if len(txt) == 0:
        text_var_entry.set('')
    elif len(txt) < 2:
        text_var_entry.set(txt)
        last_txt = txt
    else:
        text_var_entry.set(last_txt)


def ask_exit(even=None):
    answer = messagebox.askyesno(title='Do you want to exit?', message='Do you really want to exit?\nAll changes will be lost')
    if answer:
        exit(0)


def click(txt):
    global entry, text_var_entry, last_txt
    x = (int(txt) % 9) * 43 + (int(txt) % 9) * 3 + (int(txt) % 9 * 0.3)+ 12
    y = (int(txt) // 9) * 43 + (int(txt) // 9) * 3 + (int(txt) // 9  * 0.3) + 12
    text_var_entry = ctk.StringVar()
    if entry in root.winfo_children():
        entry.destroy()
        entry = ctk.CTkEntry(root,
                             width=20,
                             height=20,
                             textvariable=text_var_entry,
                             font=font)
    else:
        entry = ctk.CTkEntry(root,
                             width=20,
                             height=20,
                             textvariable=text_var_entry,
                             font=font)
    entry.focus_set()
    last_txt = ''
    text_var_entry.trace('w', entry_limit)
    entry.bind('<Return>', partial(enter_num, txt))
    entry.place(x=x, y=y)


def enter_num(txt, event):
    global text_var_entry, entry
    if len(text_var_entry.get()) > 0:
        buttons[txt].configure(require_redraw=True, text=text_var_entry.get())
        board[int(txt) // 9, int(txt) % 9] = text_var_entry.get()
        entry.destroy()
        entry = '123'


def check_game():
    board_check = board.tolist()
    string_check_fun = ''
    for lst in board_check:
        lst = ''.join(lst)
        string_check_fun += lst
    if '0' in string_check_fun:
        messagebox.showerror(title='Empty cells',
                             message='Cannot check the solution.\nThere are empty cells on the board')
    elif solution != string_check_fun:
        messagebox.showerror(title='Bad solution',
                             message='This solution is not right.\nTry to change something...')
    else:
        again = messagebox.askyesno(title='You win!', message='Yes, that\'s the solution!\nDo you want to play again?')
        if again:
            root.destroy()
            os.system('sudoku_game.pyw')
        else:
            root.destroy()


def center_window(width=300, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


def change_mode():
    if ctk.get_appearance_mode() == 'Dark':
        ctk.set_appearance_mode('Light')
        line1 = canvas.create_line(173, 0, 173, 520, width=5, fill='black')
        line2 = canvas.create_line(347, 0, 347, 520, width=5, fill='black')
        line3 = canvas.create_line(0, 173, 520, 173, width=5, fill='black')
        line4 = canvas.create_line(0, 347, 520, 347, width=5, fill='black')
        canvas.configure(bg='white')
    else:
        ctk.set_appearance_mode('Dark')
        line1 = canvas.create_line(173, 0, 173, 520, width=5, fill='white')
        line2 = canvas.create_line(347, 0, 347, 520, width=5, fill='white')
        line3 = canvas.create_line(0, 173, 522, 173, width=5, fill='white')
        line4 = canvas.create_line(0, 347, 522, 347, width=5, fill='white')
        canvas.configure(bg='black')


ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

root = ctk.CTk()
center_window(400, 300)
icon = ImageTk.PhotoImage(Image.open('img/icon.png'))
root.iconphoto(True, icon)
root.title('Sudoku')
root.configure(takefocus=1)
root.protocol('WM_DELETE_WINDOW', ask_exit)
font = ctk.CTkFont(family='Century Gothic', size=25)

label_menu = ctk.CTkLabel(root,
                          text='Welcome to the sudoku game!\nChoose the difficulty:',
                          font=font)
button_very_easy = ctk.CTkButton(root, text='Very easy', command=partial(main, 1), font=font)
button_easy = ctk.CTkButton(root, text='Easy', command=partial(main, 2), font=font)
button_medium = ctk.CTkButton(root, text='Medium', command=partial(main, 3), font=font)
button_hard = ctk.CTkButton(root, text='Hard', command=partial(main, 4), font=font)
label_menu.pack(expand=True)
button_very_easy.pack(expand=True)
button_easy.pack(expand=True)
button_medium.pack(expand=True)
button_hard.pack(expand=True)
root.mainloop()


ctk.set_appearance_mode('System')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.resizable(False, False)
center_window(650, 450)
icon = ImageTk.PhotoImage(Image.open('img/icon.png'))
root.iconphoto(True, icon)
root.title('Sudoku')
root.configure(takefocus=1)
root.protocol('WM_DELETE_WINDOW', ask_exit)
font = ctk.CTkFont(family='Century Gothic', size=15)

menubar = Menu(root)
root.configure(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Change appearance mode',
                      command=change_mode,
                      underline=0)
file_menu.add_separator()
file_menu.add_command(label='Exit',
    command=ask_exit,
    accelerator='Ctrl-E',
    underline=0)
menubar.add_cascade(label='File',
    menu=file_menu,
    underline=0)

board = np.array(list(str(generators.random_sudoku(avg_rank=rank)))).reshape(9, 9)

board_check = board.tolist()
string_check = ''
for lst in board_check:
    lst = ''.join(lst)
    string_check += lst
solution = solvers.backtrack(Sudoku.from_string(string_check, box_size=BoxSize(3, 3)))
solution = str(solution)

canvas = ctk.CTkCanvas(root, width=520, height=520)
line1 = canvas.create_line(173, 0, 173, 520, width=5)
line2 = canvas.create_line(347, 0, 347, 520, width=5)
line3 = canvas.create_line(0, 173, 520, 173, width=5)
line4 = canvas.create_line(0, 347, 520, 347, width=5)
canvas.place(x=0, y=0)

buttons = {}
x = 0
for row in range(9):
    for col in range(9):
        buttons[str(x)] = ctk.CTkButton(root,
                                        text=board[row, col] if board[row, col] != '0' else '',
                                        command=partial(click, str(x)),
                                        width=40,
                                        height=40,
                                        border_width=1,
                                        font=font)
        buttons[str(x)].grid(row=row, column=col, padx=3, pady=3)
        x += 1

button_check = ctk.CTkButton(root, text='Check!', command=check_game, width=150, height=100, font=font)
button_exit = ctk.CTkButton(root, text='Exit', command=ask_exit, width=150, height=60, font=font)
button_check.place(x=460, y=50)
button_exit.place(x=460, y=200)

entry = '123'
root.bind_all('<Control-e>', ask_exit)

root.mainloop()