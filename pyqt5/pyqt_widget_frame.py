#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=50, positionY=50,
                           sizeX=400, sizeY=200,
                           title='Tab')

        # Create and set layout
        self._add_main_layout()

        # Add the widgets
        self._add_widgets()

        # Show the window
        self.show()

    def _wnd_settings(self, **kwargs):
        u"""
        Sets the following window's settings:
            - self.setGeometry()
            - self.setWindowTitle()
        """
        posX = kwargs.get('py', kwargs.get('positionY', 50))
        posY = kwargs.get('px', kwargs.get('positionX', 50))
        sizeX = kwargs.get('sx', kwargs.get('sizeX', 300))
        sizeY = kwargs.get('sy', kwargs.get('sizeY', 450))
        title = kwargs.get('t', kwargs.get('title', 'Window'))
        # ----------------

        # Place in space and set size
        self.setGeometry(posX, posY, sizeX, sizeY)

        # Set title
        self.setWindowTitle('PyQt Widget example: {}'.format(title))

    def _add_main_layout(self):
        self._gui['main_lay'] = QVBoxLayout()
        self.setLayout(self._gui['main_lay'])

    def _add_widgets(self):
        # -------------------
        # Top Frame
        self._gui['topFrame'] = QFrame()
        self._gui['topFrame'].setFrameStyle(QFrame.Panel | QFrame.Raised)
        self._gui['topFrame'].setLineWidth(2)
        self._gui['topFrame_lbl'] = QLabel("Top Frame")
        self._gui['topFrame_lbl'].setAlignment(Qt.AlignLeft)
        self._gui['topFrame_lbl'].setAlignment(Qt.AlignVCenter)
        self._gui['topFrame_lay'] = QHBoxLayout()
        self._gui['topFrame_lay'].addWidget(self._gui['topFrame_lbl'])
        self._gui['topFrame'].setLayout(self._gui['topFrame_lay'])

        # -------------------
        # Middle Frame
        self._gui['midFrame'] = QFrame()
        self._gui['midFrame'].setFrameStyle(QFrame.Box | QFrame.Sunken)
        self._gui['midFrame'].setLineWidth(5)
        self._gui['midFrame_lbl'] = QLabel("Middle Frame")
        self._gui['midFrame_lbl'].setAlignment(Qt.AlignCenter)
        self._gui['midFrame_lay'] = QHBoxLayout()
        self._gui['midFrame_lay'].addWidget(self._gui['midFrame_lbl'])
        self._gui['midFrame'].setLayout(self._gui['midFrame_lay'])

        # -------------------
        # Bottom Frame
        self._gui['bottomFrame'] = QFrame()
        self._gui['bottomFrame'].setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
        self._gui['bottomFrame'].setLineWidth(3)
        self._gui['btmFrame_lbl'] = QLabel("Bottom Frame")
        self._gui['btmFrame_lbl'].setAlignment(Qt.AlignRight)
        self._gui['bottomFrame_lay'] = QHBoxLayout()
        self._gui['bottomFrame_lay'].addWidget(self._gui['btmFrame_lbl'])
        self._gui['bottomFrame'].setLayout(self._gui['bottomFrame_lay'])

        # Add widgets to the layout
        self._gui['main_lay'].addWidget(self._gui['topFrame'])
        self._gui['main_lay'].addWidget(self._gui['midFrame'])
        self._gui['main_lay'].addWidget(self._gui['bottomFrame'])


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
