#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=50, positionY=50,
                           sizeX=600, sizeY=500,
                           title='Slider')

        # Create and set layout
        self._add_main_layout()

        # Add texts
        self._add_texts()

        # Add the slider
        self._add_slider()

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

    def _add_texts(self):
        self._gui['text01'] = QLabel("0")
        self._gui['text02'] = QLabel("Hello World")

        # Add a space on the top
        self._gui['main_lay'].addStretch()

        # Add the widgets to the layout
        self._gui['main_lay'].addWidget(self._gui['text01'])
        self._gui['main_lay'].addWidget(self._gui['text02'])

        # Adjust this widget to the center
        self._gui['text01'].setAlignment(Qt.AlignCenter)

    def _add_slider(self):
        self._gui['slider'] = QSlider(Qt.Horizontal)  # Use Qt.Vertical for vertical (duh)

        # Set min and max
        self._gui['slider'].setMinimum(0)
        self._gui['slider'].setMaximum(100)

        # Add "ticks" (lines that are a visible representation of the slider value)
        self._gui['slider'].setTickPosition(QSlider.TicksAbove)  # By default it will display a tick per unit
        self._gui['slider'].setTickInterval(10)

        # Connect the widgets change to a method
        self._gui['slider'].valueChanged.connect(self.get_slider_value)

        # Add the widget to the layout
        self._gui['main_lay'].addWidget(self._gui['slider'])

    def get_slider_value(self):
        # Get value
        _val = self._gui['slider'].value()

        # Set value for text
        self._gui['text01'].setText(str(_val))

        # Change font size based on value
        _font = QFont("Times", _val)
        self._gui['text02'].setFont(_font)


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
