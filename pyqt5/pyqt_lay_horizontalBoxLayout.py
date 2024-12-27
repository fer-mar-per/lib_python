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
                           title='Horizontal Box Layout')

        # Add the layout
        self._add_main_layout()

        # Add buttons
        self._add_buttons(addStretch=True)

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
        self._gui['lay_hbox'] = QHBoxLayout()
        self.setLayout(self._gui['lay_hbox'])

    def _add_buttons(self, addStretch):
        btn01 = QPushButton("Button 1", self)
        btn02 = QPushButton("Button 2", self)
        btn03 = QPushButton("Button 3", self)
        if addStretch:
            self._gui['lay_hbox'].addStretch()
        self._gui['lay_hbox'].addWidget(btn01)
        self._gui['lay_hbox'].addWidget(btn02)
        self._gui['lay_hbox'].addWidget(btn03)
        if addStretch:
            self._gui['lay_hbox'].addStretch()

        # Set the margins for the layout (left, top, right, bottom)
        self._gui['lay_hbox'].setContentsMargins(120, 20, 10, 30)


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
