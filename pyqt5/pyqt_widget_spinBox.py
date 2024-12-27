#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from functools import partial

# Define the font family and size
font = QFont("Arial", 16)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=250, positionY=150,
                           sizeX=420, sizeY=300,
                           title='Spin Box')

        # Create two lineEdits
        self._add_spinBox()

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

    def _add_spinBox(self):
        u"""

        :return:
        """
        self._gui['spinBox'] = QSpinBox(self)
        self._gui['spinBox'].move(150, 100)
        self._gui['spinBox'].setFont(font)

        # Set minimum and maximum values
        # self._gui['spinBox'].setMinimum(25)
        # self._gui['spinBox'].setMaximum(110)
        self._gui['spinBox'].setRange(25, 110)

        # Add a prefix and suffix
        self._gui['spinBox'].setPrefix('# ')
        self._gui['spinBox'].setSuffix(' number')

        # Set a step size
        self._gui['spinBox'].setSingleStep(5)

        # Connect to a method when the object changes
        self._gui['spinBox'].valueChanged.connect(self.get_value)

    def get_value(self):
        _val = self._gui['spinBox'].value()
        print(_val)


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
