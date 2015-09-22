#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is a basic data streamer that allows users to poll the an Arduino connected
to a "server" of some form.
"""

import zmq
import time
import serial

Arduino = serial.Serial('/dev/ttyACM0', 9600)
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://10.0.1.24:5556")

while True:
    message = socket.recv()
    print("Recieved Request")
    time.sleep(1)
    IMU_read = Arduino.readline()
    format_input = str(IMU_read, 'ascii').split(",")
    AcX = format_input[0]
    socket.send_string(b"AcX: %i" % AcX)