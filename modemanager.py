import tkinter
from tkinter.constants import*

import yamlconfig
import action

class Viewer:   
    def __init__(self, mode_data):
        self.mode_data = mode_data

    def config(self):

        tk = tkinter.Tk()

        frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
        frame.pack(fill=BOTH, expand=1)

        l = tkinter.Label(frame, text="Mode Select")
        l.pack(side=TOP, expand=1)

        self.__show_mode(frame)

        act = action.Action(self.mode_data)
        buf = act.get_buf()

        e = tkinter.Entry(frame, textvariable = buf)
        e.pack()
        e.focus_set()
        e.bind('<Return>', act.select_mode)

        b = tkinter.Button(frame, text="Select", command=act.test_method)
        b.pack(side=BOTTOM)

        tk.mainloop()

    def __show_mode(self, frame):
        for data in self.mode_data:
            l = tkinter.Label(frame, text=data['mode'])
            l.pack()



if __name__ == "__main__":
    yc = yamlconfig.YamlConfig()
    yc.open_yaml()
    data = yc.get_data()

    view = Viewer(data)
    view.config()
