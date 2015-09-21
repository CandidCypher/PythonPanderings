#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is a test application for continuous reading of serial input
"""

import sys
from PySide import QtCore, QtGui
from ContinuousReadGY88 import GY88_python


class Gy88Display(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
