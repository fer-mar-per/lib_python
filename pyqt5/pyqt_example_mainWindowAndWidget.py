#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from functools import partial


class CentralWidgets(QWidget):
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
        # self.show()

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


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=50, positionY=50,
                           sizeX=600, sizeY=600,
                           title='QMainWindow & QWidget together')

        # Create and set layout
        self._add_main_layout()
        # Add the central widget
        self.main_widget = CentralWidgets()
        self.setCentralWidget(self.main_widget)

        # Add the widgets
        self._add_widgets()

        # Show the window maximized
        self.showMaximized()

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
        self._gui['main_lay'] = QVBoxLayout()
        self.setLayout(self._gui['main_lay'])

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

        # Toolbar
        self._gui['menu_toolbar'] = self.addToolBar("My Toolbar")
        self._gui['menu_toolbar'].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # Toolbar: Magic
        self._gui['menu_toolbar_magic'] = QAction(QIcon("_ico/btnFullImg.png"), "Magic", self)
        self._gui['menu_toolbar'].addAction(self._gui['menu_toolbar_magic'])
        # Toolbar: Lettuce
        self._gui['menu_toolbar_lettuce'] = QAction(QIcon("_ico/btnFullImg.png"), "Lettuce", self)
        self._gui['menu_toolbar'].addAction(self._gui['menu_toolbar_lettuce'])
        # Toolbar: Chop
        self._gui['menu_toolbar_chop'] = QAction(QIcon("_ico/btnFullImg.png"), "Chop", self)
        self._gui['menu_toolbar_chop'].triggered.connect(partial(self.btnFuncA, self._gui['menu_toolbar_chop']))
        self._gui['menu_toolbar'].addAction(self._gui['menu_toolbar_chop'])
        # Connecting the method to the toolbar
        self._gui['menu_toolbar'].actionTriggered.connect(self.btnFuncB)
        # Add a comboBox to the toolBar
        self._gui['menu_comboBox'] = QComboBox()
        self._gui['menu_comboBox'].addItems(["One", "Two", "Three"])
        self._gui['menu_toolbar'].addWidget(self._gui['menu_comboBox'])

    def closeWnd(self):
        mBox = QMessageBox.information(self, "WARNING",
                                       "Do you want want to exit the application?",
                                       QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
        if mBox == QMessageBox.Yes:
            sys.exit()

    def btnFuncA(self, btn):
        print(btn.text())

    def btnFuncB(self, btn):
        if btn.text() == "Magic":
            print("Magic")
        elif btn.text() == "Lettuce":
            print("Lettuce")


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
