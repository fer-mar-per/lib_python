#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
# =====================================================
Module Name:
    - tk_prompt
Version:
    - 01.0.0
Variation:
    - None
Details:
    - Prompt examples/utilities.
Public Commands:
    - WIP
Author:
    - Fernando Martin Perucki.
Updates:
    - 2021/08/13 Perucki: Added messageBox first example.
    - 2021/08/10 Perucki: Created.
To Revise / Bugs known:
    - None.
Tested Software Version:
    - Python 3.9
Tested Operating System:
    - Windows 10
# =====================================================
"""

import tkinter
import tkinter.filedialog
import tkinter.messagebox
import os
from functools import partial

# [Global variables] --------------------------------------------------- START
__version__ = '01.0.0'
__category__ = "DevLib"
dir_path = os.path.dirname(os.path.realpath(__file__))
# Prints and notes
toolNameSpace = "fmpApps"
# GUI
currentToolName = "{}: tkinter GUI library - Prompt".format(toolNameSpace)
__lang__ = 'eng'
wnd_dict = {}
# ---------------------------------------------------------------------- END


class SubWndA:
    def __init__(self, **kwargs):
        u"""
        WIP
        """
        self.master = kwargs.get('m', kwargs.get('master', None))
        self.wndA = None

    def open_subWnd(self):
        u"""
        WIP
        """
        if self.wndA:
            print("Window already exists. Process omitted.")
            self.wndA.focus_force()
        else:
            self.wndA = tkinter.Tk()
            self.wndA.title(currentToolName)
            self.wndA.configure(background="gray25")
            self.wndA.resizable(width=True, height=True)
            self.wndA.configure(height=400, width=600)
            self.wndA.mainloop()
            return self.wndA

    def close_subWnd(self):
        u"""
        WIP
        """
        # ------------------
        if self.wndA is not None:
            try:
                does_exist = self.wndA.winfo_exists()
                if does_exist:
                    self.wndA.destroy()
                    self.wndA = None
            except tkinter.TclError:
                print("Window doesn't exist (Destroyed already). Process omitted.")
        else:
            print("Window doesn't exist (None). Process omitted.")


class FakeConsole:
    def __init__(self, **kwargs):
        u"""
        WIP
        """
        self.master = kwargs.get('m', kwargs.get('master', None))

    def asTextField(self):
        u"""
        WIP
        """
        if self.master:
            result = tkinter.Text(self.master)
            return result

    def write(self, *args):
        u"""
        WIP
        """
        pass


def execute():
    u"""
    WIP 
    """
    # ------------------
    wnd = tkinter.Tk()
    wnd.title(currentToolName)
    wnd.configure(background="gray25")

    wnd.resizable(width=True, height=True)
    #  ######################################
    # ------------------
    # Exit application
    btn01 = tkinter.Button(wnd, text='Exit this application', command=wnd.destroy)
    btn01.pack()
    # ------------------
    # Open sub-window A
    subWndA = SubWndA()
    btn02 = tkinter.Button(wnd, text='Open sub window A', command=subWndA.open_subWnd)
    btn02.pack()
    # Close sub-window A
    btn03 = tkinter.Button(wnd, text='Close sub window A', command=subWndA.close_subWnd)
    btn03.pack()
    #  ######################################
    # <MODULE> filedialog
    # ------------------
    # Ask Directory
    btn04 = tkinter.Button(wnd, text='Ask Directory', command=tkinter.filedialog.askdirectory)
    btn04.pack()
    # ------------------
    # Open File
    btn05 = tkinter.Button(wnd, text='Open File', command=tkinter.filedialog.askopenfilename)
    btn05.pack()
    # ------------------
    # Save File
    btn06 = tkinter.Button(wnd, text='Save File', command=tkinter.filedialog.asksaveasfilename)
    btn06.pack()
    #  ######################################
    # <MODULE> messageBox
    # A module used to display message boxes in your applications. This module provides
    # a number of functions that you can use to display an appropriate message.
    # Some of these functions are
    #       showinfo(), showwarning(), showerror(), askquestion(), askokcancel(), askyesno(), and askretryignore().
    # Syntax to create this widget:
    #   tkMessageBox.FunctionName(title, message [, options])
    # where:
    #   FunctionName − This is the name of the appropriate message box function.
    #   title − This is the text to be displayed in the title bar of a message box.
    #   message − This is the text to be displayed as a message.
    #   options − options are alternative choices that you may use to tailor a standard message box.
    #           Some of the options that you can use are default and parent. The default option is
    #           used to specify the default button, such as ABORT, RETRY, or IGNORE in the message box.
    #           The parent option is used to specify the window on top of which the message box is to be displayed.
    # ------------------
    # messageBox: showinfo
    btn07 = tkinter.Button(wnd, text='messageBox: showinfo', command=partial(tkinter.messagebox.showinfo,
                                                                             'Show Info Title', 'Show Info Content'))
    btn07.pack()

    #  ######################################
    wnd.configure(height=400, width=600)
    wnd.mainloop()


if __name__ == '__main__':
    execute()
