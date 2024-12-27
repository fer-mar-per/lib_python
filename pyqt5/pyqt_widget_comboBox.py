#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=250, positionY=150,
                           sizeX=350, sizeY=350,
                           title='ComboBox')

        # Create a comboBox
        self._add_comboBox()

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

    def _add_comboBox(self):
        u"""
        Adds a comboBox with some items.
        """
        # Create a ComboBox
        self._gui['combo'] = QComboBox(self)
        # Use a geometry manager to move it
        self._gui['combo'].move(150, 100)

        # Function to add only one item
        # (only strings)
        self._gui['combo'].addItem('Option A')

        # Function to add multiple items
        # (only strings)
        self._gui['combo'].addItems(['Option B', 'Option C'])

        # Add a button for saving
        button = QPushButton("Save", self)
        button.move(150, 130)
        button.clicked.connect(self.get_value)

    def get_value(self):
        value = self._gui['combo'].currentText()
        print(value)


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
