#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""

"""

import cv2
import numpy

capture = cv2.VideoCapture("http://@192.168.1.130:8000/")
while capture.isOpened():
    _, frame = capture.read()
    cv2.imshow("stream", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
