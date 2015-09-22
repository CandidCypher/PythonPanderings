#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is the client reader for the Arduino Data Streamer
"""

import zmq
import time

context = zmq.Context()

print("Connecting to remote Arduino....")
socket = context.socket(zmq.REQ)
socket.connect("tcp://10.0.1.24:5556")

for request in range(10):
    print("Sending request {}".format(request))
    socket.send(b"Data Please")
    print("Data has been requested")
    message = socket.recv()
    print("Collected Data {}".format(message))
