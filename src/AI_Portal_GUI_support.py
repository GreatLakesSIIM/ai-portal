#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 31, 2018 04:39:41 PM


import sys
import AI_Portal_GUI

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def set_Tk_var():
    global combobox
    combobox = StringVar()
    global combobox2
    combobox2 = StringVar()
    global combobox3
    combobox3 = StringVar()
    global spinbox
    spinbox = StringVar()
    global spinbox2
    spinbox2 = StringVar()
    global spinbox3
    spinbox3 = StringVar()
    global spinbox4
    spinbox4 = StringVar()
    global spinbox5
    spinbox5 = StringVar()
    global spinbox6
    spinbox6 = StringVar()
    global spinbox7
    spinbox7 = StringVar()
    global spinbox8
    spinbox8 = StringVar()
    global tch95
    tch95 = StringVar()
    global tch95_2
    tch95_2 = StringVar()
    global tch95_3
    tch95_3 = StringVar()
    global sex_select
    sex_select = StringVar()
    global sex_select2
    sex_select2 = StringVar()
    global sex_select3
    sex_select3 = StringVar()
    global sex_select4
    sex_select4 = StringVar()
    global smoke_select
    smoke_select = StringVar()
    global smoke_select2
    smoke_select2 = StringVar()
    global smoke_select3
    smoke_select3 = StringVar()
    global smoke_select4
    smoke_select4 = StringVar()
    global get_reports
    get_reports = StringVar()
    global get_only_reports
    get_only_reports = StringVar()
    global research_PID
    research_PID = StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    AI_Portal_GUI.vp_start_gui()

