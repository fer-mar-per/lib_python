#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Set window's space, size and title
        self._wnd_settings(title="Labels", sizeY=350)

        # Add the labels
        self._add_labels()

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

    def _add_labels(self):
        u"""
        Creates a label widget and places it in 'self'.
        """
        # When it is created, the size of the label is also defined at creation time
        text1 = QLabel("Hello General Genovesse", self)
        text2 = QLabel("Hello World", self)

        # We need to use a geometry manager to place our labels properly
        # One geometry manager is 'move'
        text1.move(100, 50)
        text2.move(50, 100)

        # Set the alignment of text1 (AlignRight, AlignLeft, AlignCenter)
        text1.setAlignment(QtCore.Qt.AlignRight)

        # Set a style sheet for the text2
        text2.setStyleSheet('font-size: 24pt; font-family: Arial Bold; background-color: red')


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
