#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
# =====================================================
Module Name:
    - tk_font
Version:
    - 01.0.0
Variation:
    - None
Details:
    - Font utilities.
    - Because font choices are so platform-specific, be careful of
        hardcoding specifics (font families, sizes, etc.).
        This is something else you'll see in many older Tk programs
        that can make them look ugly.
Public Commands:
    - WIP
Author:
    - Fernando Martin Perucki.
Updates:
    - 2021/08/12 Perucki: Added fontchooser.
    - 2021/08/07 Perucki: Created.
To Revise / Bugs known:
    - None.
Tested Software Version:
    - Python 3.9
Tested Operating System:
    - Windows 10
# =====================================================
"""

import tkinter
import tkinter.font as tk_font
import os

# [Global variables] --------------------------------------------------- START
__version__ = '01.0.0'
__category__ = "DevLib"
dir_path = os.path.dirname(os.path.realpath(__file__))
# Prints and notes
toolNameSpace = "fmpApps"
# GUI
currentToolName = "{}: tkinter GUI library - Font".format(toolNameSpace)
__lang__ = 'eng'
# ---------------------------------------------------------------------- END


def execute(**kwargs):
    u"""
    WIP
    """
    # Input arguments -----------
    maxRows = kwargs.get('mr', kwargs.get('maxRows', 36))
    fontSize = kwargs.get('fs', kwargs.get('fontSize', 12))  # pixels
    cursorsList = kwargs.get('cl', kwargs.get('cursorsList', 'common'))
    # Local arguments -----------
    row = 0
    col = 0
    # Main process --------------
    wnd = tkinter.Tk()
    wnd.title(currentToolName)

    # The font.families() can not be executed if there is no root window
    fonts = list(tk_font.families())
    fonts.append('FONT_CHOOSER')
    for fnt in fonts:
        if fnt != 'FONT_CHOOSER':
            e = tkinter.Text(wnd, height=1, width=20,
                              font=(fnt, -fontSize))
            e.insert(1.0, fnt)
            e.grid(row=row, column=col, sticky=tkinter.E + tkinter.W)
            row += 1
            if row > maxRows:
                row = 0
                col += 1
        else:
            e_2 = tkinter.Label(wnd,   #height=1, width=20,
                                text="Text to change font",
                                font="helvetica {}".format(fontSize))
            # e_2.insert(1.0, "Text to change font")
            e_2.grid(row=row, column=col, sticky=tkinter.E + tkinter.W)

            def font_changed(font):
                e_2['font'] = font

            row += 1
            if row > maxRows:
                row = 0
                col += 1

            def fontChooserLaunch():
                wnd.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica 24', '-command',
                             wnd.register(font_changed))
                wnd.tk.call('tk', 'fontchooser', 'show')

            e = tkinter.Button(wnd, height=1, width=20,
                               text='Pick a font',
                               font="helvetica {}".format(fontSize),
                               command=fontChooserLaunch)
            e.grid(row=row, column=col, sticky=tkinter.E + tkinter.W)

    wnd.mainloop()


if __name__ == '__main__':
    execute()
