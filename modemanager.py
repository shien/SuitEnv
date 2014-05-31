import tkinter
from tkinter.constants import*

import os

import yamlconfig

app_name = "safari"

def test_method():
    #for app in app_list:
    os.system("open -a" + app_name)

def select_mode(event):
    print('get event')

class Viewer:   
    def __init__(self, mode_data):
        self.mode_data = mode_data

    def config(self):

        tk = tkinter.Tk()

        frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
        frame.pack(fill=BOTH, expand=1)

        l = tkinter.Label(frame, text="Mode Select")
        l.pack(side=TOP, expand=1)

        for data in self.mode_data:
            l = tkinter.Label(frame, text=data['mode'])
            l.pack()

        e = tkinter.Entry(frame)
        e.pack()
        e.focus_set()
        e.bind('<Return>', select_mode)

        b = tkinter.Button(frame, text="Select", command=test_method)
        b.pack(side=BOTTOM)

        tk.mainloop()


if __name__ == "__main__":
    yc = yamlconfig.YamlConfig()
    yc.open_yaml()
    data = yc.get_data()

    view = Viewer(data)
    view.config()
