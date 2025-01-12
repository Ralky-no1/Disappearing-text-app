import tkinter
from tkinter import filedialog
import time

screen = tkinter.Tk()
screen.configure(width = 800, height = 800)
screen['bg'] = 'grey'

text_editor = tkinter.Text(width = 100, height = 40, font=("Arial", 14))
text_editor.grid(column = 0, row = 1, columnspan = 2)


def delete_text():
    text_editor.delete(1.0, tkinter.END)


def restart_timer(event=None):
    global time_not_typed
    screen.after_cancel(time_not_typed)
    time_not_typed = screen.after(10000, delete_text)


def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_editor.get("1.0", "end"))


menu_bar = tkinter.Menu(screen)

file_menu = tkinter.Menu()
file_menu.add_command(label='Save', command=save_file)
menu_bar.add_cascade(label="File", menu=file_menu)
screen.config(menu=menu_bar)


time_not_typed = screen.after(10000, delete_text)


text_editor.bind('<Key>', restart_timer)


screen.mainloop()