#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=50, positionY=50,
                           sizeX=600, sizeY=600,
                           title='Menu')

        # Create and set layout
        self._add_main_layout()

        # Add the widgets
        self._add_widgets()

        # Set window's icon
        self.setWindowIcon(QIcon("_ico/btnFullImg.png"))

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
        self.setWindowTitle('PyQt Main Window example: {}'.format(title))

    def _add_main_layout(self):
        u"""
        - In the case of a QMainWindow, you need a different approach for adding the top layout.
        """
        self._gui['main_wgt'] = QWidget()
        self._gui['main_lay'] = QVBoxLayout()
        self._gui['main_wgt'].setLayout(self._gui['main_lay'])
        self.setCentralWidget(self._gui['main_wgt'])

    def _add_widgets(self):
        # Menu Bar (WARNING: You need to inherit the window class from QMainWindow)
        self._gui['menu_bar'] = self.menuBar()

        # File Menu
        self._gui['menu_file'] = self._gui['menu_bar'].addMenu("File")
        # File Menu Item: New
        self._gui['menu_file_new'] = QAction("New", self)
        self._gui['menu_file_new'].setShortcut("Ctrl+n")
        self._gui['menu_file'].addAction(self._gui['menu_file_new'])
        # File Menu Item: Magic
        self._gui['menu_file_magic'] = QAction("Magic", self)
        self._gui['menu_file_magic'].setShortcut("Ctrl+m")
        self._gui['menu_file_magic'].setIcon(QIcon("_ico/btnFullImg.png"))
        self._gui['menu_file'].addAction(self._gui['menu_file_magic'])
        # File Menu Item: Exit
        self._gui['menu_file_exit'] = QAction("Exit", self)
        self._gui['menu_file_exit'].setShortcut("Ctrl+q")
        self._gui['menu_file_exit'].triggered.connect(self.closeWnd)
        self._gui['menu_file'].addAction(self._gui['menu_file_exit'])

        # Edit Menu
        self._gui['menu_edit'] = self._gui['menu_bar'].addMenu("Edit")

        # Code Menu
        self._gui['menu_code'] = self._gui['menu_bar'].addMenu("Code")

        # Help Menu
        self._gui['menu_help'] = self._gui['menu_bar'].addMenu("Help")

        self._gui['label01'] = QLabel("Hi there.")
        self._gui['main_lay'].addWidget(self._gui['label01'])

    def closeWnd(self):
        mBox = QMessageBox.information(self, "WARNING",
                                       "Do you want want to exit the application?",
                                       QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
        if mBox == QMessageBox.Yes:
            sys.exit()


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
