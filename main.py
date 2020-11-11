#!/usr/bin/env python

import tkinter as tk
from tkinter import ttk
import re

window = tk.Tk()
addAll = tk.IntVar()
amend = tk.IntVar()
noEdit = tk.IntVar()

#region FUNCTIONS
def setup_window_position():
    w = window.winfo_reqwidth()
    h = window.winfo_reqheight()
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('+%d+%d' % (x, y))

def copy_to_clipboard_command():
    command = generate_command()
    clipBoardEntry.config(state='normal')
    clipBoardEntry.delete(0, 'end')
    clipBoardEntry.insert(0, command)
    clipBoardEntry.config(state='readonly')
    window.clipboard_clear()
    window.clipboard_append(command)
    window.update

def noEditChange():
    if noEdit.get() == 1:
        commitPrefixEntry.delete(0, 'end')
        commitPrefixEntry.config(state='disabled')
        commitMessageEntry.delete(0, 'end')
        commitMessageEntry.config(state='disabled')
    else:
        commitPrefixEntry.config(state='normal')
        commitMessageEntry.config(state='normal')

def generate_command():
    command = "git commit "
    command += add_arguments_string()
    command = message_string(command)
    return command

def add_arguments_string():
    command = ""
    if addAll.get() == 1:
        command += "-a "
    if amend.get() == 1:
        command += "--amend "
    if noEdit.get() == 1:
        command += "--no-edit "
    return command

def message_string(command):
    message = command
    if noEdit.get() == 0:
        if commitPrefixEntry.get() == "" or commitMessageEntry.get() == "":
            message = "Should fill Prefix and Message!"
        else:
            message += "-m \"[" + commitPrefixEntry.get().upper().replace('\n', '').replace('\r', '') + "] " + commitMessageEntry.get().replace('\n', '').replace('\r', '') + "\""
    return message
#end FUNCTIONS

#region SETUP UI
tk.Label(window, text='Arguments', anchor='w').grid(row=0, column=0)
tk.Label(window, text='Commit prefix', anchor='w').grid(row=1, column=0)
tk.Label(window, text='Commit Message', anchor='w').grid(row=2, column=0)

ttk.Checkbutton(window, text='Add All', variable=addAll, style='TCheckbutton').grid(row=0, column=1, sticky='ew')
ttk.Checkbutton(window, text='Amend', variable=amend, style='TCheckbutton').grid(row=0, column=2, sticky='ew')
ttk.Checkbutton(window, text='No Edit', variable=noEdit, style='TCheckbutton', command=noEditChange).grid(row=0, column=3, sticky='ew')

commitPrefixEntry = tk.Entry(window)
commitMessageEntry = tk.Entry(window)

commitPrefixEntry.grid(row=1, column=1, columnspan=3, sticky='ew')
commitMessageEntry.grid(row=2, column=1, columnspan=3, sticky='ew')

ttk.Button(window, text='Generate command and copy', style='TButton', command=copy_to_clipboard_command).grid(row=3, columnspan=4, sticky='ew')

clipBoardEntry = tk.Entry(window, state='readonly')
clipBoardEntry.grid(row=4, columnspan=4, sticky='ew')
#end SETUP UI

#region SETUP WINDOW
window.title('Commit Helper')
window.resizable(0,0)
setup_window_position()
#end SETUP WINDOW

tk.mainloop()
