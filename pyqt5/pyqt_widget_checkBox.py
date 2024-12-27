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
                           title='CheckBox')

        # Add the necessary elements to the UI
        self._add_lineEdits()
        self._add_checkBox()
        self._add_button()

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

    def _add_lineEdits(self):
        # Add some LineEdit objects
        self._gui['name'] = QLineEdit(self)
        self._gui['name'].move(150, 50)
        self._gui['name'].setPlaceholderText("Enter your name")
        self._gui['surname'] = QLineEdit(self)
        self._gui['surname'].move(150, 80)
        self._gui['surname'].setPlaceholderText("Enter your surname")

    def _add_checkBox(self):
        # Create a checkbox
        self.remember = QCheckBox("Remember values", self)
        self.remember.move(150, 110)

    def _add_button(self):
        # Add a button for submit
        button = QPushButton("Submit", self)
        button.move(200, 140)
        button.clicked.connect(self.submit)

    def submit(self):
        _chkd = None
        if self.remember.isChecked():
            _chkd = 'Checked'

        else:
            _chkd = 'Unchecked'

        print("Name: {}".format(self._gui['name'].text()))
        print("Surname: {}".format(self._gui['surname'].text()))
        print("Remember: {}".format(_chkd))


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
