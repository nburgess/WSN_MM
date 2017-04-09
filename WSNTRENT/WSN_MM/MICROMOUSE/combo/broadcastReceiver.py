# Recv UDP broadcast packets
 
 
MYPORT = 50000
 
import sys, time
from socket import *
import mouseNode

myip = "127.0.0.1"
print (str(myip))
 
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('', MYPORT))
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
 
while 1:
 
    data, addr = s.recvfrom(1024)
    if addr == myip:
        print('server received %r from myself' % (data))
    else:
        print('server received %r from %r' % (data, addr))