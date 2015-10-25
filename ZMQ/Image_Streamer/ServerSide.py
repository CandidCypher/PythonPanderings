#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Dev>
#
# Distributed under terms of the MIT license.

"""
This is a basic building block for building a video streamer
"""

import cv2
import zmq
import io

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bindZZ
