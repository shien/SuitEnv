# encoding: utf8

import os

app_name = "safari"

def test_method():
    os.system('open -a' + app_name)

def select_mode(event):
    print('get event')
