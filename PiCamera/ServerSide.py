#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 CoroWare Robotics Solutions <www.coroware.com>
#
# Distributed under terms of the MIT license.

"""
This is a test of the PiRGBArray method to determine type.
"""

import zmq
import picamera
import picamera.array
from io

stream = io.BytesIO()
camera = picamera.PiCamera()
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.bind("tcp://192.168.1.106:5555")

while True:
    message = socket.recv()
    print("Recieved Request")
    camera.capture(stream, format='jpeg', use_video_port=True)
    socket.send_multipart(["PI_CAM", stream.getvalue()])
