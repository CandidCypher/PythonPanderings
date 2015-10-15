#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is a basic test of building a simple clock in PySide
"""

import time
from PySide import QtCore, QtGui

clockApp = QtGui.QApplication([])


def tick():
    current_time = time.strftime('%H:%M:%S')
    lcd.display(current_time)

lcd = QtGui.QLCDNumber()
lcd.setDigitCount(8)

timer = QtCore.QTimer()
timer.timeout.connect(tick)
timer.start(1000)

lcd.show()

clockApp.exec_()
