#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
# =====================================================
Module Name:
    - tk_button
Version:
    - 01.0.0
Variation:
    - None
Details:
    - Button utilities.
Public Commands:
    - WIP
Author:
    - Fernando Martin Perucki.
Updates:
    - 2021/08/11 Perucki: Completed.
    - 2021/08/06 Perucki: Created.
To Revise / Bugs known:
    - None.
Tested Software Version:
    - Python 3.9
Tested Operating System:
    - Windows 10
# =====================================================
"""

import tkinter
import os

# [Global variables] --------------------------------------------------- START
__version__ = '01.0.0'
__category__ = "DevLib"
dir_path = os.path.dirname(os.path.realpath(__file__))
# Prints and notes
toolNameSpace = "fmpApps"
# GUI
currentToolName = "{}: tkinter GUI library - Button".format(toolNameSpace)
__lang__ = 'eng'
# ---------------------------------------------------------------------- END


def on_enter(e):
    e.widget.config(background='pink')


def on_leave(e):
    e.widget.config(background='SystemButtonFace')


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
    # <CLASS> tkinter.Button(master, <options=values>)
    # ------------------
    # Simple
    btn01 = tkinter.Button(wnd, text='Simple')
    btn01.pack()
    # ------------------
    # BG, Active BG, FG, Active FG, font
    # bg/background: Normal background color.
    # activebackground: Background color when the button is under the cursor.
    # fgforeground/: Normal foreground (text) color.
    # activeforeground: Foreground color when the button is under the cursor.
    # font: The font, specified with (fontName, size)
    btn02 = tkinter.Button(wnd, text='BG, Active BG, FG, Active FG, font',
                           background='limeGreen',
                           foreground='purple',
                           activebackground="khaki1",
                           activeforeground="OrangeRed2",
                           font=("MV Boli", 12))
    btn02.pack()
    # ------------------
    # Height, Width and Highlight
    # highlightcolor: The color of the focus highlight when the widget has focus.
    btn03 = tkinter.Button(wnd, text='Height, Width and Highlight',
                           height=2, width=25,
                           highlightcolor='yellow')
    btn03.pack()
    # ------------------
    # Button bound to mouse
    btn04 = tkinter.Button(wnd, text='Button bound to mouse')
    btn04.bind("<Enter>", on_enter)
    btn04.bind("<Leave>", on_leave)
    btn04.pack()
    # ------------------
    # Using an image
    imgPath = '{}/_ico/btnImg.png'.format(dir_path)
    image = tkinter.PhotoImage(file=imgPath)
    btn05 = tkinter.Button(wnd, image=image)
    btn05.pack()
    # ------------------
    # Using an image AND text
    # compound: Used to display both image and text together. The default value is none,
    # meaning display only the image if present; if there is no image, display the text
    # specified by the text or textvariable options. Other possible values for the
    # compound option are: text (text only), image (image only), center (text in the center
    # of image), top (image above text), left, bottom, and right.
    btn06 = tkinter.Button(wnd, image=image,
                           text='Image and text', compound=tkinter.TOP)
    btn06.pack()
    # ------------------
    # Use only image as a button
    # Be careful because the background color needs to match to the window's one to look good.
    imgFullPath = '{}/_ico/btnFullImg.png'.format(dir_path)
    imageFull = tkinter.PhotoImage(file=imgFullPath)
    btn07 = tkinter.Button(wnd, image=imageFull, borderwidth=0,
                           background='gray25',
                           activebackground='gray25')
    btn07.pack()
    # ------------------
    # Justified text
    # justify: How to show multiple text lines: LEFT to left-justify each line;
    # CENTER to center them; or RIGHT to right-justify.
    btn08 = tkinter.Button(wnd, text='Justified\ntext\nwith multiple\nlines',
                           justify=tkinter.RIGHT, width=26)
    btn08.pack()
    # ------------------
    # Additional padding on X and Y
    # padx: Additional padding left and right of the text.
    # pady: Additional padding above and below the text.
    btn09 = tkinter.Button(wnd, text='Additional padding on X and Y')
    btn09.pack(padx=10, pady=10)
    # ------------------
    # Relief
    # relief: The type of the border. Some of the values are SUNKEN, RAISED, GROOVE, and RIDGE.
    btn10 = tkinter.Button(wnd, text='Relief', relief=tkinter.RIDGE)
    btn10.pack()
    # ------------------
    # State
    # state: Set this option to DISABLED to gray out the button and make it unresponsive.
    # Has the value ACTIVE when the mouse is over it. Default is NORMAL.
    btn11 = tkinter.Button(wnd, text='State: Disabled', state=tkinter.DISABLED)
    btn11.pack()
    # ------------------
    # Underline
    # underline: Default is -1, meaning that no character of the text on the button will
    # be underlined. If non-negative, the corresponding text character will be underlined.
    # (This looks to be mainly used for shortcuts)
    btn12 = tkinter.Button(wnd, text='Underline the t on this.', underline=19)
    btn12.pack()
    # ------------------
    # Wrap Length
    # wraplength: If this value is set to a positive number,
    # the text lines will be wrapped to fit within this length.
    btn13 = tkinter.Button(wnd, text='Wrap Length',
                           wraplength=20)
    btn13.pack()
    # ------------------

    #  ######################################
    wnd.configure(height=400, width=600)
    wnd.mainloop()


if __name__ == '__main__':
    execute()
