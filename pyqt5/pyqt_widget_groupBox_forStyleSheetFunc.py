#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


def groupBoxStyle():
    u"""
    Usually this function is in a separate file,
    and will be imported from that external module and executed.
    """
    return """
        QGroupBox {
            background-color: #fcc324;
            font: 15pt Times Bold;
            color: white;
            border: 2px solid gray;
            border-radius: 15px;
        }
    """


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=50, positionY=50,
                           sizeX=400, sizeY=400,
                           title='GroupBox (function styleSheet)')

        # Add the layout
        self._add_main_layout()

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

    def _add_main_layout(self):
        self._gui['lay_vbox'] = QVBoxLayout()
        self._gui['lay_vbox2'] = QVBoxLayout()

        self.setLayout(self._gui['lay_vbox'])

    def _add_buttons(self):
        # Create the Group Box widget
        self._gui['gpBox'] = QGroupBox("Group Name")
        # Add a Style Sheet for the Group Box
        self._gui['gpBox'].setStyleSheet(groupBoxStyle())
        # Create the widgets that will go in the layout inside the Group Box
        btn01 = QPushButton("Button 01", self)
        btn02 = QPushButton("Button 02", self)
        btn03 = QPushButton("Button 03", self)
        btn04 = QPushButton("Button 04", self)
        txt01 = QLabel("Text 01", self)
        txt01.setAlignment(QtCore.Qt.AlignCenter)
        # Add the widgets to the sub-layout that will be put inside the Group Box
        self._gui['lay_vbox2'].addWidget(btn01)
        self._gui['lay_vbox2'].addWidget(txt01)
        self._gui['lay_vbox2'].addWidget(btn02)
        self._gui['lay_vbox2'].addWidget(btn03)
        self._gui['lay_vbox2'].addWidget(btn04)
        # Set the sub-layout, which includes the widgets, for the Group Box
        self._gui['gpBox'].setLayout(self._gui['lay_vbox2'])

        self._gui['lay_vbox'].addStretch()
        self._gui['lay_vbox'].addWidget(self._gui['gpBox'])  # The Group Box is a Widget
        self._gui['lay_vbox'].addStretch()


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
