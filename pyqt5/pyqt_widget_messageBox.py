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
                           sizeX=420, sizeY=300,
                           title='Message Box')

        # Create two lineEdits
        self._add_lineEdits()

        # Create two radioButtons
        self._add_radioButtons()

        # Add submit button
        self._add_buttonA_withFont()
        self._add_buttonB_withFont()

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

    def _add_radioButtons(self):
        u"""
        Adds two radioButtons.
        """
        # Create the RadioButtons
        self._gui['male'] = QRadioButton("Male", self)
        self._gui['female'] = QRadioButton("Female", self)

        # Use a geometry manager to move them
        self._gui['male'].move(150, 110)
        self._gui['female'].move(200, 110)

        # Set the male to checked
        self._gui['male'].setChecked(True)

    def _add_buttonA_withFont(self):
        # Add a button for submit
        button = QPushButton("Question", self)
        button.setFont(font)
        button.move(200, 140)
        button.clicked.connect(partial(self._msgBox, messageType='question'))

    def _add_buttonB_withFont(self):
        # Add a button for submit
        button = QPushButton("Inform", self)
        button.setFont(font)
        button.move(200, 200)
        button.clicked.connect(partial(self._msgBox, messageType='information'))

    def get_values(self):
        _name = self._gui['name'].text()
        _surname = self._gui['surname'].text()
        _gender = None
        if self._gui['male'].isChecked():
            _gender = "Sir"
        elif self._gui['female'].isChecked():
            _gender = "Madam"

        return "{} {} {}".format(_gender, _name, _surname)

    def _msgBox(self, **kwargs):
        u"""
        Creates a message Box.
        """
        msgType = kwargs.get('mt', kwargs.get('messageType', 'question'))
        _title = None
        _msg = None
        _val = self.get_values()

        if msgType == 'question':
            _title = "Question Message Box"
            _msg = "Are you {}?".format(_val)

            _mBox = QMessageBox.question(self, _title, _msg,
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,  # The buttons
                                         QMessageBox.No  # The button you want focused
                                         )

            if _mBox == QMessageBox.Yes:
                # Close the application
                sys.exit()
            elif _mBox == QMessageBox.No:
                print("You said no. Good job.")

        elif msgType == 'information':
            _title = "Information Message Box"
            _msg = "You are {}.".format(_val)

            _mBox = QMessageBox.information(self, _title, _msg,
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,  # The buttons
                                         QMessageBox.No  # The button you want focused
                                         )


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
