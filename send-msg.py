#!/usr/bin/env python3

import socket
import struct

MCAST_GRP = '234.5.6.2'
MCAST_PORT = 6666
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 3)
sock.sendto(b'Hello World!', (MCAST_GRP, MCAST_PORT))

