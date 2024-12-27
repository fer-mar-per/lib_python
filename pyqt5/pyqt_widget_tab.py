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
                           sizeX=400, sizeY=200,
                           title='Tab')

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
        self._gui['main_lay'] = QVBoxLayout()
        self.setLayout(self._gui['main_lay'])

    def _add_widgets(self):
        # Tab Constructor
        self._gui['tabs'] = QTabWidget()
        # Each Tab
        self._gui['tab01'] = QWidget()
        self._gui['tab02'] = QWidget()
        self._gui['tab03'] = QWidget()
        # Add the tabs
        self._gui['tabs'].addTab(self._gui['tab01'], "First Tab")
        self._gui['tabs'].addTab(self._gui['tab02'], "Second Tab")
        self._gui['tabs'].addTab(self._gui['tab03'], "Third Tab")

        # Create first tab's widgets
        self._gui['tab01_lay'] = QVBoxLayout()
        self._gui['tab01_wd01'] = QLabel("Hi there.")
        self._gui['tab01_wd02'] = QPushButton("General Mustard.")
        self._gui['tab01_lay'].addWidget(self._gui['tab01_wd01'])
        self._gui['tab01_lay'].addWidget(self._gui['tab01_wd02'])
        self._gui['tab01'].setLayout(self._gui['tab01_lay'])

        # Add widgets to the layout
        self._gui['main_lay'].addWidget(self._gui['tabs'])


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
