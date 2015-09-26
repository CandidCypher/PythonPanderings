#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is a camera streamer used for streaming video frames over a network
"""

import zmq
import cPickle
import zlib
import serial
import picamera
import picamera.array

# Network configuration Stuffs
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://your_IP_address_here:5555")

while True:
    message = socket.recv()
    print("Recived Request")
    camera = picamera.PiCamera()
    image_array = picamera.array.PiRGBArray(camera)
