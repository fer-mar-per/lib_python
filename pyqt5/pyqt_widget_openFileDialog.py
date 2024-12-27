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
                           sizeX=500, sizeY=300,
                           title='Open File Dialog')

        # Create and set layout
        self._add_main_layout()

        # Add the widgets
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
        self._gui['main_vlay'] = QVBoxLayout()
        self._gui['main_hlay'] = QHBoxLayout()

        self.setLayout(self._gui['main_vlay'])

    def _add_widgets(self):
        # Add text editor
        self._gui['editor'] = QTextEdit()
        self._gui['main_vlay'].addWidget(self._gui['editor'])

        # Add open file button
        self._gui['main_vlay'].addLayout(self._gui['main_hlay'])
        self._gui['fileBtn'] = QPushButton("Open File")
        self._gui['main_hlay'].addStretch()  # Left side stretch for main_hlay
        self._gui['main_hlay'].addWidget(self._gui['fileBtn'])
        self._gui['main_hlay'].addStretch()  # Right side stretch for main_hlay
        self._gui['fileBtn'].clicked.connect(self.openFile)

    def openFile(self):
        _url = QFileDialog.getOpenFileName(self, "Open a file",
                                           "",  # If you want to open a specific directory
                                           "All Files(*);;*txt")
        if _url:
            self._gui['url'] = _url[0]
            print(self._gui['url'])
            _fl = open(self._gui['url'], 'r')
            _cnt = _fl.read()
            self._gui['editor'].setText(_cnt)


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
