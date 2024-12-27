#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from functools import partial

# Define the font family and size
font = QFont("Arial", 14)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=250, positionY=150,
                           sizeX=500, sizeY=500,
                           title='Text Editor')

        # Create the textEditor
        self._add_textEditor()

        # Add button
        self._add_buttonA_withFont()

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

    def _add_buttonA_withFont(self):
        # Add a button
        button = QPushButton("Send", self)
        button.setFont(font)
        button.move(330, 280)
        button.clicked.connect(self.get_value)

    def _add_textEditor(self):
        # Add a text editor (includes a slider so it doesn't need to be manually added)
        self._gui['txtEd'] = QTextEdit(self)
        # Avoid formatted text such as bold, italic, etc.
        self._gui['txtEd'].setAcceptRichText(False)
        self._gui['txtEd'].move(150, 80)

    def get_value(self):
        _val = self._gui['txtEd'].toPlainText()
        print(_val)


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
