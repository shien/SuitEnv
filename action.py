# encoding: utf8

import os
import tkinter

class Action:
    def __init__(self, mode_data):
        self.buf = tkinter.StringVar()
        self.buf.set('')

        self.mode_data = mode_data

    def __test_method(self):
        os.system('open -a' + app_name)

    def select_mode(self, event):
        if self.__have_input_mode() == "":
            return

    def __have_input_mode(self):
        if self.buf.get():
            mode = self.buf.get()
        else:
            return

        for i, dic in enumerate(self.mode_data):
            if str(i) == mode:
                mode = dic['mode']
                return mode

        for i, dic in enumerate(self.mode_data):
            if dic['mode'] == mode:
                mode = dic['mode']
                return mode

        return ""

    def get_buf(self):
        return self.buf
