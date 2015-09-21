#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is your first cross network helloworld system. This module runs on the
raspberry pi side and simply pushes out world when it is connected to. This
will complete the message sent from the client side of Hello(client) +
World(Server)
"""

import zmq
import time


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.bind("tcp://192.168.1.126:5556")  # Change this to your Raspi's Address
time.sleep(1)
while True:
    # This section will sit and wait for a request from client
    message = socket.recv()
    print("Recieved request: %s" % message)
    # Insert some delay so you can actually see the message going back and forth
    time.slep(1)

    # Sending of the response
    socket.send(b"World")
