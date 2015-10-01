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
import numpy
import io
import serial
import zlib
import cPickle

stream = io.BytesIO()
camera = picamera.PiCamera()
Arduino = serial.Serial('/dev/ttyACM0', 9600)
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://192.168.1.106:5555")

while True:
    message = socket.recv()
    print("Recieved Request")
    IMU_read = Arduino.readlin()
    camera.capture(stream, format='jpeg')
    data = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
    packed_pickle = cPickle.dumps(data)
    bundle = zlib.compress(packed_pickle)
    socket.send(bundle)
