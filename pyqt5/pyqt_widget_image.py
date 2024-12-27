#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(sizeX=350, sizeY=350,
                           title='Image')

        # Add the image and the buttons
        self._add_img()
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

    def _add_img(self):
        u"""
        Adds one image to the window.
        """
        _fullPath = r'C:/Users/marti/My Drive (martin@fmpsys.net)/'
        _fullPath += r'fmpSystem/desktopApps/win/py3_9/'
        _fullPath += r'fmpApps_dev/fmpApps/__devKit/devLib/pyqt_lib/'
        _localPath = '_ico/btnFullImg.png'
        _fullPath += _localPath

        # Create the Label that will display the image
        self._gui['image'] = QLabel(self)
        # Specify the path to the image (DOES LOCAL WORK?)
        self._gui['image'].setPixmap(QPixmap(_localPath))

        # Place the image using 'move'
        self._gui['image'].move(150, 50)

    def _add_buttons(self):
        u"""
        Adds one button to hide the image,
        and other button to display it.
        """
        # Add a button to remove the image
        removeButton = QPushButton("Remove", self)
        removeButton.move(150, 220)
        removeButton.clicked.connect(self.removeImg)

        # Add a button to add the image back
        showButton = QPushButton("Show", self)
        showButton.move(260, 220)
        showButton.clicked.connect(self.showImg)

    def removeImg(self):
        u"""
        Method to remove specified image.
        """
        self._gui['image'].close()

    def showImg(self):
        u"""
        Method to show back again the removed image.
        """
        self._gui['image'].show()


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
