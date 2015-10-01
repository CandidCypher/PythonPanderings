#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is the client side of the basic image streamer.
"""

import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.1.106:5555")

while True:
    start = time.time()
    message = socket.recv()
    end = time.time()
    print(data)
    total_time = end - start
    print("Elapsed Time:", total_time)
