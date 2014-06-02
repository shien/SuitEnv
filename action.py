# encoding: utf8

import os
import tkinter

class Action:
    def __init__(self, mode_data):
        self.buf = tkinter.StringVar()
        self.buf.set('')

        self.mode_data = mode_data

        self.modedic = {} 

    def __close_apps(self, applist):
        for appname in applist:
            os.system("osascript -e 'tell application \"" + appname + "\" to quit'")


    # open apps list
    def __open_apps(self, applist):
        for appname in applist:
            os.system('open -a "' + appname + '"')

    # select mode from yaml file.
    def select_mode(self, event):
        modedic = self.__have_input_mode()
        if modedic == "":
            return

        if modedic == self.modedic:
            return

        if 'app' not in modedic:
            return 

        new_apps = modedic['app']

        if 'app' not in self.modedic:
            print("first exec")
            self.__open_apps(new_apps)
            self.modedic = modedic
            return

        old_apps = self.modedic['app']

        # make to close apps list
        set_close_app = set(old_apps) - set(new_apps)
        close_apps = list(set_close_app)
        print("close :")
        print(close_apps)
        self.__close_apps(close_apps)

        # make to open apps list
        set_open_apps = set(new_apps) - set(old_apps)
        open_apps = list(set_open_apps)
        print("open :")
        print(open_apps)
        self.__open_apps(open_apps)

        self.modedic = modedic

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
