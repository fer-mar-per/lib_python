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
                           title='LineEdits')

        # Add the textBoxes and button to print the values
        self._add_textBoxes()
        self._add_btn()

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

    def _add_textBoxes(self):
        u"""
        Adds the text boxes to the main window.
        """
        # Create the instances
        self._gui['nameTextBox'] = QLineEdit(self)
        self._gui['passTextBox'] = QLineEdit(self)

        # Add placeholder texts for them
        self._gui['nameTextBox'].setPlaceholderText("Your name here")
        self._gui['passTextBox'].setPlaceholderText("Your pass here")

        # Set the pass to be not visible
        self._gui['passTextBox'].setEchoMode(QLineEdit.Password)

        # Use the geometry manager to move the widgets
        self._gui['nameTextBox'].move(120, 50)
        self._gui['passTextBox'].move(120, 80)

    def _add_btn(self):
        u"""
        Adds the save button to the main window.
        """
        btn = QPushButton("Save", self)
        btn.move(180, 110)
        btn.clicked.connect(self.get_values)

    def get_values(self):
        name = self._gui['nameTextBox'].text()
        psw = self._gui['passTextBox'].text()
        self.setWindowTitle("Your name is: {} - And your psw is: {}".format(name, psw))


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
