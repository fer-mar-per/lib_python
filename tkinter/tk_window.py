#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
# =====================================================
Module Name:
    - tk_window
Version:
    - 01.0.0
Variation:
    - None
Details:
    - Window utilities.
Public Commands:
    - WIP
Author:
    - Fernando Martin Perucki.
Updates:
    - 2021/07/28 Perucki: Separated module.
    - 2021/07/27 Perucki: Created.
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
currentToolName = "{}: tkinter GUI library - Window".format(toolNameSpace)
__lang__ = 'eng'
# ---------------------------------------------------------------------- END


def execute():
    u"""
    WIP 
    """
    iconPath = '{}/_ico/icoTest.ico'.format(dir_path)
    # gifPath = '{}/_ico/smiley.gif'.format(dir_path)
    # ######################################
    # <CLASS> Tk()
    #   Toplevel widget of Tk which represents mostly the main window of an application.
    wnd = tkinter.Tk()

    # ######################################
    # <CLASS> PhotoImage()
    #   Widget which can display colored images in GIF, PPM/PGM format.
    #   WARNING: This doesn't support PNG or JPG files.
    # img = tkinter.PhotoImage(file=gifPath)

    # ######################################
    # <METHODS> (others)
    #   tk.call method is the tkinter interface to tcl interpreter. We could run a tcl command by using this call
    #   method. It is handy when the Tkinter wrapper could not have access to some tcl/tk features.
    #   wm communicates with window manager.
    #   tkinter isn't pure python. Underlying it is a live Tcl interpreter with an extension called "tk"
    #   loaded into the interpreter. Most tkinter commands, methods and objects eventually wind up as invocations
    #   of tcl commands.
    #   The call method is the interface to this underlying tcl interpreter. It allows you to construct a tcl command
    #   and ask the interpreter to run it. It is a bridge between python and tcl.
    #   It is not typically used in application-level code, though it can be useful
    #   in the rare cases where the Tkinter wrapper around tcl/tk doesn't provide access to some feature
    #   supported by tcl/tk.
    #   _w is a Class Variable from the Tk() class --> _w = '.'
    # wnd.tk.call('wm', 'iconphoto', wnd._w, img)

    # ######################################
    # <METHODS> Inherited from Wm()
    #   Provides functions for the communication with the window manager.
    # -----------------
    # Tk().title(string=None)
    #   Set the title of this widget.
    wnd.title(currentToolName)

    # -----------------
    # Tk()['background'] = '#856ff8'
    #   Sets the background color using HEX.
    # wnd['background'] = '#856ff8'

    # -----------------
    # Tk().configure(bg/background=None)
    #   Sets the background color from the color chart. Refer to 'tkinter_colorChart' for details on the colors.
    wnd.configure(background="snow4")

    # -----------------
    # Tk().configure(height=None, width=None)
    #   Set window's size.
    wnd.configure(height=400, width=600)

    # -----------------
    # Tk().geometry(newGeometry=None)
    #   Set window's size. Set geometry to NEWGEOMETRY of the form =widthxheight+x+y.
    #   Return current value if None is given.
    # wnd.geometry("320x220")

    # -----------------
    # Tk().configure(cursor=None)
    #   Set the cursor to be displayed when the cursor is on top of the window. Refer to 'tkinter_cursor' for details
    #   on all the available cursors.
    wnd.configure(cursor='target')

    # -----------------
    # Tk().iconbitmap(bitmap=None, default=None)
    #   Set bitmap for the iconified widget to BITMAP. Return the bitmap if None is given.
    #   Under Windows, the DEFAULT parameter can be used to set the icon for the widget and any descendents
    #   that don't have an icon set explicitly. DEFAULT can be the relative path to a .ico file
    #   (example: root.iconbitmap(default='myIcon.ico') ).
    wnd.iconbitmap(iconPath)

    # -----------------
    # Tk().iconphoto(False, tkinter.PhotoImage(file=None))
    #   Another method to set the window icon, using the PhotoImage class. It accepts more image types.
    # WARNING!: This doesn't work when creating .exe with pyinstaller. Please use iconbitmap.
    # wnd.iconphoto(False, img)

    # -----------------
    # Tk().resizable(width=None, height=None)
    #   Instruct the window manager whether this width can be resized in WIDTH or HEIGHT.
    #   Both values are boolean values.
    wnd.resizable(width=True, height=True)

    # -----------------
    # Tk().maxsize(width=None, height=None)
    #   Set max WIDTH and HEIGHT for this widget. If the window is gridded the values are given in grid units.
    #   Return the current values if None is given.
    # wnd.maxsize(width=800, height=800)

    # -----------------
    # Tk().minsize(width=None, height=None)
    #   Set min WIDTH and HEIGHT for this widget. If the window is gridded the values are given in grid units.
    #   Return the current values if None is given.
    # wnd.minsize(width=100, height=100)

    # -----------------
    # Tk().attributes('-fullscreen', True)
    #   Set the window to maximized size (fullscreen).
    #   WARNING: This doesn't display the title bar.
    # wnd.attributes('-fullscreen', True)

    # -----------------
    # Tk().state('zoomed')
    #   Set the window to maximized size (fullscreen with title bar).
    wnd.state('zoomed')

    # -----------------
    # Tk().mainloop(n=0)
    #   Launch the window. Call the mainloop of Tk.
    wnd.mainloop()

    # -----------------
    return wnd


if __name__ == '__main__':
    execute()
