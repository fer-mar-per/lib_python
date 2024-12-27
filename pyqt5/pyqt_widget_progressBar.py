#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Create a variable for the progress bar counting
        self.count = 0

        # Set window's space, size and title
        self._wnd_settings(positionX=50, positionY=50,
                           sizeX=600, sizeY=150,
                           title='Progress Bar')

        # Add the layout
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
        self._gui['main_lay'] = QVBoxLayout()
        self._gui['hbox_lay'] = QHBoxLayout()
        self.setLayout(self._gui['main_lay'])

    def _add_widgets(self):
        # Add the progress bar
        self._gui['progBar'] = QProgressBar()
        # If you want to hide the text
        # self._gui['progBar'].setTextVisible(False)

        self._gui['main_lay'].addWidget(self._gui['progBar'])
        self._gui['main_lay'].addLayout(self._gui['hbox_lay'])

        # Add the buttons
        self._gui['btnStart'] = QPushButton("Start")
        self._gui['btnStop'] = QPushButton("Stop")
        self._gui['hbox_lay'].addWidget(self._gui['btnStart'])
        self._gui['hbox_lay'].addWidget(self._gui['btnStop'])
        self._gui['btnStart'].clicked.connect(self.timerStart)
        self._gui['btnStop'].clicked.connect(self.timerStop)

        # Create the timer
        self._gui['timer'] = QTimer()
        self._gui['timer'].setInterval(100)
        self._gui['timer'].timeout.connect(self.runProgressBar)

    def runProgressBar(self):
        if self.count != 100:
            self.count += 1
            self._gui['progBar'].setValue(self.count)
        else:
            self._gui['timer'].stop()

    def timerStart(self):
        self._gui['timer'].start()

    def timerStop(self):
        self._gui['timer'].stop()


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
