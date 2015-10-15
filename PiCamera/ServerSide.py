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
import io
from PIL import Image

stream = io.BytesIO()
camera = picamera.PiCamera()
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.bind("tcp://192.168.1.123:5555")

while True:
    message = socket.recv()
    print("Recieved Request")
    camera.capture(stream, format='jpeg', use_video_port=True)
    stream.seek(0)
    image = Image.open(stream)
    f = io.StringIO()
    Image.fromarray(image).save(f, 'JPEG')
    socket.send_multipart(["PI_CAM", f.getvalue()])
    f.close()
