import tkinter
from tkinter.constants import*

import os

import config

app_name = "safari"

def test_method():
    #for app in app_list:
    os.system("open -a" + app)

def select_mode(event):
    print('get event')

class Viewer:   
    def config(self):
        tk = tkinter.Tk()

        frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
        frame.pack(fill=BOTH, expand=1)

        l = tkinter.Label(frame, text="Mode Select")
        l.pack(side=TOP, expand=1)

        e = tkinter.Entry(frame)
        e.pack()
        e.focus_set()
        e.bind('<Return>', select_mode)

        b = tkinter.Button(frame, text="Select", command=test_method)
        b.pack(side=BOTTOM)

        tk.mainloop()

view = Viewer()
view.config()
