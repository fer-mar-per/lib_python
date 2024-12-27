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
                           title='Vertical & Horizontal Box Layout')

        # Add the main layout
        _mainLay = self._add_main_layout()

        # Add the top layout
        _topLay = self._add_top_layout(parentLay=_mainLay, margins=[100, 10, 20, 20])

        # Add top lay widgets
        self._add_top_widgets(_topLay)

        # Add the bottom layout
        _btmLay = self._add_bottom_layout(parentLay=_mainLay, margins=[150, 10, 150, 10])

        # Add bottom lay widgets
        self._add_btm_widgets(_btmLay)

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
        _mainLay = QVBoxLayout()
        self.setLayout(_mainLay)
        return _mainLay

    @staticmethod
    def _add_top_layout(parentLay, margins):
        _topLay = QHBoxLayout()
        parentLay.addLayout(_topLay, 30)  # If you write parentLay.addLayout(_topLay, 40) it will occupy 40% of the space
        _topLay.setContentsMargins(*margins)  # [left, top, right, bottom]
        return _topLay

    @staticmethod
    def _add_bottom_layout(parentLay, margins):
        _btmLay = QHBoxLayout()
        parentLay.addLayout(_btmLay, 70)
        _btmLay.setContentsMargins(*margins)  # [left, top, right, bottom]
        return _btmLay

    @staticmethod
    def _add_top_widgets(topLay):
        _cbox = QCheckBox()
        _rbtn = QRadioButton()
        _cmb = QComboBox()

        topLay.addWidget(_cbox)
        topLay.addWidget(_rbtn)
        topLay.addWidget(_cmb)

    @staticmethod
    def _add_btm_widgets(btmLay):
        _btn1 = QPushButton()
        _btn2 = QPushButton()

        btmLay.addWidget(_btn1)
        btmLay.addWidget(_btn2)


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
