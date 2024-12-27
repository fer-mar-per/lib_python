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
        self._wnd_settings(positionX=50, positionY=50,
                           sizeX=400, sizeY=400,
                           title='Form Layout')

        # Add the layout
        self._add_main_layout()

        # Add buttons
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
        self._gui['lay_form'] = QFormLayout()
        self._gui['lay_form'].setVerticalSpacing(80)  # This will set the space between the rows.
        self.setLayout(self._gui['lay_form'])

    def _add_widgets(self):
        # This will set each row separately
        # self._gui['lay_form'].setRowWrapPolicy(QFormLayout.WrapAllRows)
        self._gui['name_txt'] = QLabel("Name: ")
        self._gui['name_inp'] = QLineEdit()
        self._gui['psw_txt'] = QLabel("Password: ")
        self._gui['psw_inp'] = QLineEdit()
        self._gui['cnty_txt'] = QLabel("Country: ")
        self._gui['cnty_cmbx'] = QComboBox()

        # Add a different layout for the buttons, so they can be placed on the right side
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))

        self._gui['lay_form'].addRow(self._gui['name_txt'],
                                     self._gui['name_inp'])  # You need to add the two widgets (max. two widgets)
        self._gui['lay_form'].addRow(self._gui['psw_txt'],
                                     self._gui['psw_inp'])  # You need to add the two widgets (max. two widgets)
        self._gui['lay_form'].addRow(self._gui['cnty_txt'],
                                     self._gui['cnty_cmbx'])  # You need to add the two widgets (max. two widgets)
        self._gui['lay_form'].addRow(hbox)


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
