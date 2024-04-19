#!/usr/bin/env python3

import socket
import struct

MCAST_GRP = '234.5.6.2'
MCAST_PORT = 6666

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((MCAST_GRP, MCAST_PORT))

mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
sock.setsockopt(socket.IPPROTO_IP, 12, 1)
while True:
  data, ancdata, msg_flags, addr = sock.recvmsg(65535,1024)
  print("packet from "+str(addr)+" containing "+str( len(data))+ " bytes with ttl of "+str(ancdata[0][2][0]))
  print(repr(data)[:128]+"..")

