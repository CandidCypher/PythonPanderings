#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Dev>
#
# Distributed under terms of the MIT license.

"""
This application recives a video stream from a zmq streamer
"""

import zmq

# ZMQ Setup
sync_context = zmq.Context()
sync_socket = sync_context.socket(zmq.DEALER)
sync_socket.identity = b"u_watcher"
sync_socket.connect("tcp://10.0.0.13:6666")

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")


while True:
    print("Waiting for message")
    message = socket.recv_multipart()
    print("Message Captured")
    print(message[0])
    print("Recieved Message")
    print(message[1])
