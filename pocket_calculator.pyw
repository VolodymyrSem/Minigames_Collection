import tkinter as tk
import tkinter.font as font
from PIL import ImageTk, Image


def numbers(event):
    global last_num, enter_var
    pushed_button = event.widget
    num = pushed_button['text']
    if len(last_num) < 10:
        last_num += str(num)
        enter_var.set(last_num)


def action(event):
    global last_num, enter_var, overall
    pushed_button = event.widget
    action = pushed_button['text']
    if action == '=':
        overall = round(eval(overall + last_num), 2)
        overall = str(overall)
        while overall[-1] == '0' or overall[-1] == '.':
            overall = overall[0:-1]
        if len(overall) > 10:
            enter_var.set('ERROR')
        else:
            enter_var.set(overall)
        last_num = ''
        return
    elif action == 'C':
        enter_var.set('0')
        overall = ''
        last_num = ''
    elif action == '+/-':
        try:
            if last_num[0] != '-':
                last_num = '-' + last_num
                enter_var.set(last_num)
            else:
                last_num = last_num[1:]
                enter_var.set(last_num)
        except IndexError:
            if overall[0] != '-':
                overall = '-' + overall
                enter_var.set(overall)
            else:
                overall = overall[1:]
                enter_var.set(overall)
    else:
        if last_num[0] == '.':
            last_num = '0' + last_num
        if last_num == '':
            overall = overall[:-1] + action
        else:
            overall += str(last_num) + action
        last_num = ''


root = tk.Tk()
root.title('Pocket Calculator')
root.configure(bg='#9AFFA7')
icon = ImageTk.PhotoImage(Image.open('img/icon.png'))
root.iconphoto(True, icon)

font = font.Font(root, font='Consolas 35')

enter_var = tk.StringVar()
enter_var.set('0')
inp_line = tk.Entry(root, width=11, justify='right', font=font, textvariable=enter_var, bg='#9AFFA7')
inp_line.bind('<KeyPress>', 'break')
inp_line.grid(row=0, column=0, columnspan=5)

button_num_list = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.']
color_list = ['#00FF22', '#00FF33', '#00FF55',
               '#1EFF3C', '#1EFF4B', '#1EFF62',
               '#29FF46', '#29FF54', '#29FF6A',
               '#33FF4F', '#33FF85']
button_num_dict = {name: tk.Button(root, text=name, width=7, height=2, bg=color, activebackground=color)
                   for (name, color) in zip(button_num_list, color_list)}

for key in button_num_dict.keys():
    button_num_dict[key].bind('<Button-1>', numbers)

last_num = ''

button_act_list = ['=', '+/-', '*', '/', '+', '-', 'C']
color_list_act = ['#29FF78', '#33FF9A', '#29FF8D',
                  '#33FFA7', '#00FF89', '#1EFF87',
                  '#33FF6A']
button_act_dict = {name: tk.Button(root, text=name, width=7, height=2, bg=color, activebackground=color)
                   for (name, color) in zip(button_act_list, color_list_act)}

for key in button_act_dict.keys():
    button_act_dict[key].bind('<Button-1>', action)

overall = ''

button_num_dict['7'].grid(row=1, column=0)
button_num_dict['8'].grid(row=1, column=1)
button_num_dict['9'].grid(row=1, column=2)
button_num_dict['4'].grid(row=2, column=0)
button_num_dict['5'].grid(row=2, column=1)
button_num_dict['6'].grid(row=2, column=2)
button_num_dict['1'].grid(row=3, column=0)
button_num_dict['2'].grid(row=3, column=1)
button_num_dict['3'].grid(row=3, column=2)
button_num_dict['0'].grid(row=4, column=0)

button_act_dict['C'].grid(row=4, column=1)
button_num_dict['.'].grid(row=4, column=2)

button_act_dict['='].grid(row=3, column=3)
button_act_dict['+/-'].grid(row=4, column=3)

button_act_dict['+'].grid(row=1, column=4)
button_act_dict['-'].grid(row=2, column=4)
button_act_dict['*'].grid(row=3, column=4)
button_act_dict['/'].grid(row=4, column=4)

button_nothing1 = tk.Button(root, width=7, height=2, bg='#00FF6F', activebackground='#00FF6F')
button_nothing2 = tk.Button(root, width=7, height=2, bg='#1EFF78', activebackground='#1EFF78')
button_nothing1.grid(row=1, column=3)
button_nothing2.grid(row=2, column=3)

if __name__ == '__main__':
    root.mainloop()