# encoding: utf8

import os
import tkinter

class Action:
    def __init__(self, mode_data):
        self.buf = tkinter.StringVar()
        self.buf.set('')

        self.mode_data = mode_data

    # open apps list
    def __open_apps(self, applist):
        for appname in applist:
            os.system('open -a' + appname)

    # select mode from yaml file.
    def select_mode(self, event):
        modedic = self.__have_input_mode()
        if modedic == "":
            return

        apps = modedic['app']
        self.__open_apps(apps)

    def __have_input_mode(self):
        if self.buf.get():
            mode = self.buf.get()
        else:
            return

        for i, dic in enumerate(self.mode_data):
            if str(i) == mode:
                return dic

        for i, dic in enumerate(self.mode_data):
            if dic['mode'] == mode:
                return dic

        return ""

    def get_buf(self):
        return self.buf
