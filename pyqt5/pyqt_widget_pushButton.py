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
        self._wnd_settings(sizeX=350, sizeY=350,
                           title='Buttons')

        # Add a simple label and two buttons to the GUI
        self._add_label()
        self._add_buttons()

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
        u"""
        Adds a simple label.
        """
        self._gui['text1'] = QLabel("My text", self)
        self._gui['text1'].move(160, 50)

    def _add_buttons(self):
        u"""
        Adds two buttons.
        """
        # Create the buttons
        enterButton = QPushButton("Enter", self)
        exitButton = QPushButton("Exit", self)

        # We need to use the 'move' geometry manager to place out widgets properly
        enterButton.move(100, 80)
        exitButton.move(200, 80)

        # We give a functionality to the buttons
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)

    def enterFunc(self):
        # Change the text
        self._gui['text1'].setText('Enter applied')
        # We need to also update the size of the label
        self._gui['text1'].resize(150, 20)

    def exitFunc(self):
        # Change the text
        self._gui['text1'].setText('Exit applied')
        # We need to also update the size of the label
        self._gui['text1'].resize(150, 20)


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
