#!/usr/local/bin/python3 python

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

def generate_commit_command():
    clipBoardEntry.config(state='normal')
    clipBoardEntry.delete(0, 'end')
    clipBoardEntry.insert(0, "Test")
    clipBoardEntry.config(state='readonly')
    window.update

def noEditChange():
    if noEdit.get() == 1:
        commitMessageEntry.delete(0, 'end')
        commitMessageEntry.config(state='disabled')
    else:
        commitMessageEntry.config(state='normal')
#end FUNCTIONS

#region SETUP UI
tk.Label(window, text='Modifiers', anchor='w').grid(row=0, column=0)
tk.Label(window, text='Commit prefix', anchor='w').grid(row=1, column=0)
tk.Label(window, text='Commit Message', anchor='w').grid(row=2, column=0)

ttk.Checkbutton(window, text='Add All', variable=addAll, style='TCheckbutton').grid(row=0, column=1, sticky='ew')
ttk.Checkbutton(window, text='Amend', variable=amend, style='TCheckbutton').grid(row=0, column=2, sticky='ew')
ttk.Checkbutton(window, text='No Edit', variable=noEdit, style='TCheckbutton', command=noEditChange).grid(row=0, column=3, sticky='ew')

commitPrefixEntry = tk.Entry(window)
commitMessageEntry = tk.Entry(window)

commitPrefixEntry.grid(row=1, column=1, columnspan=3, sticky='ew')
commitMessageEntry.grid(row=2, column=1, columnspan=3, sticky='ew')

ttk.Button(window, text='Generate command and copy', style='TButton', command=generate_commit_command).grid(row=3, columnspan=4, sticky='ew')

clipBoardEntry = tk.Entry(window, state='readonly')
clipBoardEntry.grid(row=4, columnspan=4, sticky='ew')
#end SETUP UI

#region SETUP WINDOW
window.title('Commit Helper')
window.resizable(0,0)
setup_window_position()
#end SETUP WINDOW

tk.mainloop()