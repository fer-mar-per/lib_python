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
                           title='Vertical Box Layout')

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
        self._gui['lay_vbox'] = QVBoxLayout()
        self._gui['lay_vboxA'] = QVBoxLayout()
        self.setLayout(self._gui['lay_vbox'])

    def _add_buttons(self, addStretch):
        btn01 = QPushButton("Save", self)
        btn02 = QPushButton("Exit", self)
        btn03 = QPushButton("DELETE", self)

        if addStretch:
            self._gui['lay_vbox'].addStretch()
        self._gui['lay_vbox'].addWidget(btn03)
        btn03.clicked.connect(self._delObjs)

        self._gui['lay_vboxA'].addWidget(btn01)
        self._gui['lay_vboxA'].addWidget(btn02)
        if addStretch:
            self._gui['lay_vbox'].addStretch()

        self._gui['lay_vbox'].addLayout(self._gui['lay_vboxA'])

        # Set the margins for the layout (left, top, right, bottom)
        self._gui['lay_vbox'].setContentsMargins(60, 20, 10, 30)

    def _delObjs(self):
        for i in reversed(range(self._gui['lay_vboxA'].count())):
            _wdg = self._gui['lay_vboxA'].takeAt(i).widget()
            if _wdg is not None:
                _wdg.deleteLater()


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
