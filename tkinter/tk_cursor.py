#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""
# =====================================================
Module Name:
    - tk_cursor
Version:
    - 01.0.0
Variation:
    - None
Details:
    - Cursor utilities.
Public Commands:
    - WIP
Author:
    - Fernando Martin Perucki.
Updates:
    - 2021/07/30 Perucki: Cleaned up.
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
currentToolName = "{}: tkinter GUI library - Cursor".format(toolNameSpace)
__lang__ = 'eng'
# Dictionaries
cursors = {'common':  # List of cursors
               ['X_cursor',
                'arrow',
                'based_arrow_down',
                'based_arrow_up',
                'boat',
                'bogosity',
                'bottom_left_corner',
                'bottom_right_corner',
                'bottom_side',
                'bottom_tee',
                'box_spiral',
                'center_ptr',
                'circle',
                'clock',
                'coffee_mug',
                'cross',
                'cross_reverse',
                'crosshair',
                'diamond_cross',
                'dot',
                'dotbox',
                'double_arrow',
                'draft_large',
                'draft_small',
                'draped_box',
                'exchange',
                'fleur',
                'gobbler',
                'gumby',
                'hand1',
                'hand2',
                'heart',
                'icon',
                'iron_cross',
                'left_ptr',
                'left_side',
                'left_tee',
                'leftbutton',
                'll_angle',
                'lr_angle',
                'man',
                'middlebutton',
                'mouse',
                'pencil',
                'pirate',
                'plus',
                'question_arrow',
                'right_ptr',
                'right_side',
                'right_tee',
                'rightbutton',
                'rtl_logo',
                'sailboat',
                'sb_down_arrow',
                'sb_h_double_arrow',
                'sb_left_arrow',
                'sb_right_arrow',
                'sb_up_arrow',
                'sb_v_double_arrow',
                'shuttle',
                'sizing',
                'spider',
                'spraycan',
                'star',
                'target',
                'tcross',
                'top_left_arrow',
                'top_left_corner',
                'top_right_corner',
                'top_side',
                'top_tee',
                'trek',
                'ul_angle',
                'umbrella',
                'ur_angle',
                'watch',
                'xterm'],
           'win_native_mapped':  # On Windows systems, the following cursors are mapped to native cursors
               ['arrow',
                'center_ptr',
                'crosshair',
                'fleur',
                'ibeam',
                'icon',
                'sb_h_double_arrow',
                'sb_v_double_arrow',
                'watch',
                'xterm'],
           'win_added':  # On Windows, the following additional cursors are available
               ['no',
                'starting',
                'size',
                'size_ne_sw',
                'size_ns',
                'size_nw_se',
                'size_we',
                'uparrow',
                'wait'],
           'mac_native_mapped':  # On Mac OS X systems, the following cursors are mapped to native cursors
               ['arrow',
                'cross',
                'crosshair',
                'ibeam',
                'plus',
                'watch',
                'xterm'],
           'mac_added':  # On Mac OS X, the following additional cursors are available
               ['copyarrow',
                'aliasarrow',
                'contextualmenuarrow',
                'text',
                'cross-hair',
                'closedhand',
                'openhand',
                'pointinghand',
                'resizeleft',
                'resizeright',
                'resizeleftright',
                'resizeup',
                'resizedown',
                'resizeupdown',
                'none',
                'notallowed',
                'poof',
                'countinguphand',
                'countingdownhand',
                'countingupanddownhand',
                'spinning']
           }

# ---------------------------------------------------------------------- END


def execute(**kwargs):
    u"""
    WIP
    """
    # Input arguments -----------
    maxRows = kwargs.get('mr', kwargs.get('maxRows', 36))
    fontSize = kwargs.get('fs', kwargs.get('fontSize', 10))  # pixels
    cursorsList = kwargs.get('cl', kwargs.get('cursorsList', 'common'))
    # Local arguments -----------
    row = 0
    col = 0
    # Main process --------------
    wnd = tkinter.Tk()
    wnd.title(currentToolName)

    for cursor in cursors[cursorsList]:
        e = tkinter.Label(wnd, text=cursor,
                          font=(None, -fontSize), cursor=cursor)
        e.grid(row=row, column=col, sticky=tkinter.E + tkinter.W)
        row += 1
        if row > maxRows:
            row = 0
            col += 1
    wnd.mainloop()


if __name__ == '__main__':
    execute()
