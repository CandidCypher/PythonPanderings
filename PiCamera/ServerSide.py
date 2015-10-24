#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is a script that runs on the Raspberry Pi Capturing frames to a stream
"""

import io
import picamera
import zmq

# ZMQ Settings
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://10.1.10.218:5555")
socket.setsockopt_unicode()

# Establishing Stream
cam_stream = io.BytesIO()

# Camera Configuration
camera = picamera.PiCamera()

while True:
    camera.capture(cam_stream, format='jpeg', use_video_port=True)
    cam_stream.seek(0)
    socket.send_unicode(cam_stream.getvalue())
