import random as rn
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
from PIL import ImageTk, Image


def click(event):
    global who_moves, game_lst
    clicked_btn = event.widget
    place = int(str(clicked_btn)[8]) - 1 if len(str(clicked_btn)) == 9 else 0
    if game_lst[place//3][place%3] != '':
        return
    clicked_btn['text'] = 'X'
    clicked_btn['command'] = ''
    clicked_btn['state'] = 'disable'
    clicked_btn['bg'] = 'indianred2'
    clicked_btn['fg'] = 'white'
    game_lst[place//3][place%3] = 1
    game_lst_win.append(0)
    who_moves = False

    if win() == 1:
        root.destroy()
        return

    move = rn.randint(0, 8)
    switch = True
    while switch:
        if game_lst[move//3][move%3] != '':
            move = rn.randint(0, 8)
        else:
            clicked_btn = 'bt' + str(move)
            button_dict[clicked_btn]['text'] = 'o'
            button_dict[clicked_btn]['state'] = 'disable'
            button_dict[clicked_btn]['command'] = ''
            button_dict[clicked_btn]['bg'] = 'green yellow'
            button_dict[clicked_btn]['fg'] = 'white'
            game_lst[move // 3][move % 3] = 0
            game_lst_win.append(0)
            who_moves = True
            switch = False

    if win() == 1:
        root.destroy()
        return

def win():
    if who_moves:
        sign = 0
    else:
        sign = 1
    who = 'You' if who_moves == 0 else 'Computer'
    cross1 = cross2 = True
    for i in range(3):
        if game_lst[i][0] == game_lst[i][1] == game_lst[i][2] == sign:
            messagebox.showinfo(title='Win', message='{} win!'.format(who))
            return 1

        if game_lst[0][i] == game_lst[1][i] == game_lst[2][i] == sign:
            messagebox.showinfo(title='Win', message='{} win!'.format(who))
            return 1

        if game_lst[i][i] != sign:
            cross1 = False
        if game_lst[2 - i][2 - i] != sign:
            cross2 = False
    if cross1 or cross2:
        messagebox.showinfo(title='Win', message='{} win!'.format(who))
        return 1

    if len(game_lst_win) == 9:
        messagebox.showinfo(title='Draw', message="It's a draw!")
        return 1

root = tk.Tk()
root.title('Tic-Tac-Toe')
icon = ImageTk.PhotoImage(Image.open('img/icon.png'))
root.iconphoto(True, icon)

font = font.Font(root, size='50')

button_lst = [f'bt{x}' for x in range(9)]
button_dict = {name: tk.Button(root, text='', font=font, width=5, height=2, bg='#89F8FF') for name in button_lst}
x = 0
for el in button_dict.keys():
    button_dict[el].bind('<Button-1>', click)
    button_dict[el].grid(row=x//3, column=x%3)
    x += 1

game_lst = [['' for x in range(3)] for x in range(3)]
game_lst_win = []
who_moves = True
root.mainloop()
