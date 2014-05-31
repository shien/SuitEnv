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

        l = tkinter.Label(frame, text="[ Mac mode select ]")
        l.pack(side=TOP, expand=1)

        self.__show_mode(frame)

        act = action.Action(self.mode_data)
        buf = act.get_buf()

        e = tkinter.Entry(frame, textvariable = buf)
        e.pack()
        e.focus_set()
        e.bind('<Return>', act.select_mode)

        tk.mainloop()

    def __show_mode(self, frame):
        for i, data in enumerate(self.mode_data):
            text = str(i) + " : " +  data['mode']
            l = tkinter.Label(frame, text=text)
            l.pack()



if __name__ == "__main__":
    yc = yamlconfig.YamlConfig()
    yc.open_yaml()
    data = yc.get_data()

    view = Viewer(data)
    view.config()
