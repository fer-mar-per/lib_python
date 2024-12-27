#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

# Define the font family and size
font = QFont("Arial", 14)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=250, positionY=150,
                           sizeX=350, sizeY=350,
                           title='Timer')

        # Add a colored label
        self._add_label()

        # Add the timer (not visible)
        self._add_timer()

        # Add the start and stop buttons
        self._add_buttons_withFont()

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

    def _add_label(self):
        # Add a colored label
        self._gui['colLab'] = QLabel(self)
        self._gui['colLab'].resize(250, 250)
        self._gui['colLab'].setStyleSheet("background-color:green")
        self._gui['colLab'].move(40, 20)

    def _add_buttons_withFont(self):
        # Add a button to start the process
        buttonSrt = QPushButton("Start", self)
        buttonSrt.setFont(font)
        buttonSrt.move(80, 280)
        buttonSrt.clicked.connect(self.start)
        # Add a button to stop the process
        buttonStp = QPushButton("Stop", self)
        buttonStp.setFont(font)
        buttonStp.move(170, 280)
        buttonStp.clicked.connect(self.stop)

    def start(self):
        self._gui['timer'].start()

    def stop(self):
        self._gui['timer'].stop()

    def _add_timer(self):
        self._gui['timer'] = QTimer()
        self._gui['timer'].setInterval(1000)  # milliseconds
        self._gui['timer'].timeout.connect(self._changeColor)
        self._gui['value'] = 0

    def _changeColor(self):
        # Used in the case of two options only
        if self._gui['value'] == 0:
            self._gui['colLab'].setStyleSheet("background-color:yellow")
            self._gui['value'] = 1
        else:
            self._gui['colLab'].setStyleSheet("background-color:red")
            self._gui['value'] = 0


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    # wnd.start()  # This is used when you want to trigger the timer when the window is launched
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
