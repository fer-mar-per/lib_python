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
                           sizeX=600, sizeY=500,
                           title='Table')

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
        # Table
        self._gui['table'] = QTableWidget()
        # Add rows and columns
        self._gui['table'].setRowCount(5)
        self._gui['table'].setColumnCount(3)
        # Change names for columns
        self._gui['table'].setHorizontalHeaderItem(0, QTableWidgetItem("Country"))
        self._gui['table'].setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self._gui['table'].setHorizontalHeaderItem(2, QTableWidgetItem("Surname"))
        # Add items to the table (row, column)
        self._gui['table'].setItem(0, 1, QTableWidgetItem("First Item Added"))
        self._gui['table'].setItem(1, 2, QTableWidgetItem("Second Item Added"))
        # Set items of table to not be editable
        self._gui['table'].setEditTriggers(QAbstractItemView.NoEditTriggers)
        # In the case of hiding the different headers
        # self._gui['table'].horizontalHeader().hide()
        # self._gui['table'].verticalHeader().hide()

        # "Get" Button
        self._gui['btn_get'] = QPushButton("Get")
        self._gui['btn_get'].clicked.connect(self.get_val)

        # Connect to double click action
        self._gui['table'].doubleClicked.connect(self.get_val)

        # Add widgets to the layout
        self._gui['main_lay'].addWidget(self._gui['table'])
        self._gui['main_lay'].addWidget(self._gui['btn_get'])

    def get_val(self):
        for item in self._gui['table'].selectedItems():
            print(item.text(), item.row(), item.column())


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
