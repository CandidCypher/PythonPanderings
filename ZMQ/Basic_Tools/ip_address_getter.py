#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 cameron <cameron@Megatron-Virtual>
#
# Distributed under terms of the MIT license.

"""
This is a basic way of getting your machine's IP Address.
"""

import socket

ip_address = socket.gethostbyname(socket.getfqdn())
print(type(address), ip_address)
print(ip_address)
