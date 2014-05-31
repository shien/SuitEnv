# encoding: utf8

import os
import tkinter

app_name = "safari"


class Action:
    def __init__(self, mode_data):
        self.buf = tkinter.StringVar()
        self.buf.set('')

        self.mode_data = mode_data

    def test_method(self):
        os.system('open -a' + app_name)

    def select_mode(self, event):
        if self.__have_input_mode() == "":
            return
        print('execute to set env')

    def __have_input_mode(self):
        if self.buf.get():
            mode = self.buf.get()
        else:
            return

        for dic in self.mode_data:
            if dic['mode'] == mode:
                mode = dic['mode']
                return mode

        return ""

    def get_buf(self):
        return self.buf
