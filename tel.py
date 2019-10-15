import socket
import struct
import time

MCAST_GRP = '234.5.6.27'
MCAST_PORT = 6070

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((MCAST_GRP, MCAST_PORT))

mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
sock.setsockopt(socket.IPPROTO_IP, 12, 1)

prevdata = {}
while True:
  changed = False
  data, ancdata, msg_flags, addr = sock.recvmsg(65535,1024)
  source = str(addr[0])
  sport = str(addr[1])
  ttl = str(ancdata[0][2][0])
  timestamp = str(int(time.time()))
  if len(prevdata) > 0:
    if ttl != prevdata['ttl']:
      changed = True
    if sport != prevdata['sport']:
      changed = True
    if source != prevdata['source']:
      changed = True
  else:
    changed = True
  if changed:
    logfile = open("telefonie.log","a")
    logfile.write(timestamp+": "+source+" "+sport+" "+ttl+"\n")
    prevdata = { "ttl": ttl, "sport": sport, "source": source }
    logfile.close()
  print("packet from "+source+":"+sport+" with ttl of "+ttl)
  #  print(repr(data)[:128]+"..")
