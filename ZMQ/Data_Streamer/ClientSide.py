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
import zlib
import cPickle
import time


context = zmq.Context()

print("Connecting to remote Arduino....")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.1.106:5556")

while 1:
    socket.send(b"Data Please")
    start = time.time()
    print("Data has been requested")
    message = socket.recv()
    unpacked_pickle = zlib.decompress(message)
    data = cPickle.loads(unpacked_pickle)
    end = time.time()
    print(data)
    total_time = end - start
    print("Elapsed Time:", total_time)
