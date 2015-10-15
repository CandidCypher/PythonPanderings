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
from PIL import Image
from io import StringIO

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.1.123:5555")

while True:
    start = time.time()
    send_message = socket.send(b"Stream Please")
    message = socket.recv_multipart()
    f = StringIO(message[1])
    converted_image = Image.open(f).convert('RGB')
    f.close()
    end = time.time()
    total_time = end - start
    print("Elapsed Time:", total_time)
