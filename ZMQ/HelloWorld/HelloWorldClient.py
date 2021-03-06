#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is the client side of HelloWorld that runs locally on your machine. This
sends out requests by sending a "Hello" message which is responded by the
server with "World"
"""

import zmq  # Isnt' that awesome?! You only need one thing.
import time


context = zmq.Context()

# Socket that talks to server
print("Connecting to Hello World Server.....")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.1.126:5556")
# We only run this loop 10 times
# Next version will do for ever (while )
for request in range(10):
    print("Sending request %s" % request)
    socket.send(b"Hello")
    print("Message has been sent")
    message = socket.recv()
    print("Recieved reply %s [ %s ]" % (request, message))
