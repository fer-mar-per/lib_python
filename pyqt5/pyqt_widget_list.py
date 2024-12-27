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
        self._wnd_settings(positionX=250, positionY=150,
                           sizeX=500, sizeY=500,
                           title='List')

        # Add a Line Edit
        self._add_lineEdit()

        # Add a List Widget
        self._add_list()

        # Add buttons
        self._add_buttons()

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

    def _add_lineEdit(self):
        self._gui["lineEdit"] = QLineEdit(self)
        self._gui["lineEdit"].move(100, 50)

    def _add_list(self):
        self._gui["list"] = QListWidget(self)
        self._gui["list"].move(100, 80)
        _lst = ["NameA", "NameB", "NameC"]
        self._gui["list"].addItems(_lst)
        self._gui["list"].itemClicked.connect(self.funcSel)

    def _add_buttons(self):
        self._gui["btn_add"] = QPushButton("Add", self)
        self._gui["btn_add"].move(360, 80)
        self._gui["btn_add"].clicked.connect(self.funcAdd)
        self._gui["btn_del"] = QPushButton("Delete", self)
        self._gui["btn_del"].move(360, 110)
        self._gui["btn_del"].clicked.connect(self.funcDel)
        self._gui["btn_get"] = QPushButton("Get", self)
        self._gui["btn_get"].move(360, 140)
        self._gui["btn_get"].clicked.connect(self.funcGet)
        self._gui["btn_delAll"] = QPushButton("Delete All", self)
        self._gui["btn_delAll"].move(360, 170)
        self._gui["btn_delAll"].clicked.connect(self.funcDelAll)

    def funcAdd(self):
        _val = self._gui["lineEdit"].text()
        if _val:
            self._gui["list"].addItem(_val)
            self._gui["lineEdit"].setText("")

    def funcDel(self):
        _idx = self._gui["list"].currentRow()
        self._gui["list"].takeItem(_idx)

    def funcGet(self):
        _it = self._gui["list"].currentItem()
        if _it:
            _val = _it.text()
            print(_val)

    def funcDelAll(self):
        self._gui["list"].clear()

    def funcSel(self):
        print(self._gui["list"].currentItem().text())


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
