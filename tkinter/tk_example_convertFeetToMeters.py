#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
# =====================================================
Module Name:
    - tk_example
Version:
    - 01.0.0
Variation:
    - None
Details:
    - First code example of the book Modern Tkinter.
Public Commands:
    - WIP
Author:
    - Fernando Martin Perucki.
Updates:
    - 2021/08/26 Perucki: Solved .bind() using a function with arguments.
    - 2021/08/24 Perucki: Created.
To Revise / Bugs known:
    - None.
Tested Software Version:
    - Python 3.9
Tested Operating System:
    - Windows 10
# =====================================================
"""

import tkinter as tk
import tkinter.ttk as ttk
from functools import partial


class GUI:
    def __init__(self):
        self.gui = {}
        self.buildGUI()

    def buildGUI(self):
        self.gui['root'] = tk.Tk()
        self.gui['root'].title("Feet to Meters")

        # We put everything inside of a Frame because the main window isn't itself part of the "themed" widgets.
        # Its background color doesn't match the themed widgets we will put inside it.
        self.gui['mainFrame'] = ttk.Frame(self.gui['root'], padding="3 3 12 12")
        # After creating the frame, .grid() places it directly inside the application
        self.gui['mainFrame'].grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        # The following tell Tk that the frame should expand to fill any extra space if the window is resized:
        self.gui['root'].columnconfigure(0, weight=1)
        self.gui['root'].rowconfigure(0, weight=1)

        # Create a StringVar() and an Entry() for the text input
        self.gui['feet'] = tk.StringVar()
        self.gui['feet_entry'] = ttk.Entry(self.gui['mainFrame'],
                                           width=7,  # 7 characters
                                           textvariable=self.gui['feet'])
        self.gui['feet_entry'].grid(column=2, row=1, sticky=(tk.W, tk.E))

        # Create one Label() with the result in meters
        self.gui['meters'] = tk.StringVar()
        ttk.Label(self.gui['mainFrame'], textvariable=self.gui['meters']).grid(column=2, row=2,
                                                                               sticky=(tk.W, tk.E))

        # Add the button
        ttk.Button(self.gui['mainFrame'], text='Calculate',
                   command=partial(self.calculate,
                                   self.gui['feet'], self.gui['meters'])).grid(column=3, row=3, sticky=tk.W)

        # Add the remaining Label() widgets
        ttk.Label(self.gui['mainFrame'], text="feet").grid(column=3, row=1, sticky=tk.W)
        ttk.Label(self.gui['mainFrame'], text="is equivalent to").grid(column=1, row=2, sticky=tk.E)
        ttk.Label(self.gui['mainFrame'], text="meters").grid(column=3, row=2, sticky=tk.W)

        # Add a space (pad) between the widgets
        for child in self.gui['mainFrame'].winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Set the focus to the Entry() widget
        self.gui['feet_entry'].focus()

        # Bind the 'enter' ('return') key to the same function as the button
        self.gui['root'].bind("<Return>", partial(self.calculate,
                                                  self.gui['feet'],
                                                  self.gui['meters']))

        self.gui['root'].mainloop()

    @staticmethod
    def calculate(feetArg, meterArg, *args):
        try:
            val = float(feetArg.get())
            meterArg.set(int(0.3048 * val * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass


if __name__ == '__main__':
    GUI()
