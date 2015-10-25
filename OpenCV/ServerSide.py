#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Dev>
#
# Distributed under terms of the MIT license.

"""
This is a basic camera streamer that uses OpenCV and ZMQ to stream camera
frames over sockets.
"""

import zmq

# ZMQ Settings
sync_context = zmq.Context()
sync_socket = sync_context.socket(zmq.DEALER)
sync_socket.identity = b"u_robot"
sync_socket.connect("tcp://10.0.0.13:6666")

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://10.0.0.13:5555")


while True:
    socket.send_multipart([b'Part Zero', b'part one', b'parttwo'])
    print("Sending Frame")
