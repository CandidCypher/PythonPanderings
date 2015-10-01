#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is a test for creating a Burning Widget
"""

import sys
from PySide import QtGui, QtCore


class Communicate(QtCore.QObject):
    updateBW = QtCore.Signal(int)


class BurningWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.initUI()

    def initUI():
        self.setMinimumSize(1,30)
        self.value = 75
        self.num[75, 150, 225, 300, 375, 450, 525, 600, 675]

    def stValue(self, value):
        self.value = value

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()

    def drawingWidget(self, qp):
        font = QtGui.QFont('Serif', 7, QtGui.QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        step = int(round(w/10.0))
        till = int(((w/750.0)*self.value))
        full = int(((w/750.0)*700))

        if self.value >= 700:
            qp.setPen(QtGui.QColor(255, 255, 255))
            qp.setBrush(QtGui.QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QtGui.QColor(255, 175, 175))
