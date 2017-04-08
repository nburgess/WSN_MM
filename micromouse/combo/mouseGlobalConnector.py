import mapNode
import sys
import mapGlobal
import socket

# This file is in charge of communicating with the clients of the global map
# it accepts requests for movement and processes them
class mouseGlobalConnector:

    def getInitialPosition(self):
       print("Fetching position")
       self.socket.send("start\n".encode())
       x_str=self.fetchLine()
       y_str=self.fetchLine()
       print("("+x_str+","+y_str+")")
       x_pos=int(x_str)
       y_pos=int(y_str)
       return (x_pos,y_pos)

    def lookAhead(self,dir):
        print("Looking ahead")
        self.socket.send("sense\n".encode())
        self.socket.send((str(dir)+"\n").encode())
        f_str=self.fetchLine()
        r_str=self.fetchLine()
        l_str=self.fetchLine()
        print("("+f_str+","+r_str+","+l_str+")")
        f_val=int(f_str)
        r_val=int(r_str)
        l_val=int(l_str)
        return (f_val,r_val,l_val)

    def requestMovement(self,dir):
        print("Requesting movement")
        self.socket.send("move\n".encode())
        self.socket.send((str(dir)+"\n").encode())
        success_str=self.fetchLine()
        success=int(success_str)
        return success

    def fetchLine(self):
        buffering = True
        while buffering:
            if "\n" in self.buffer:
                (line, self.buffer) = self.buffer.split("\n", 1)
                return line
            else:
                more = self.socket.recv(4096).decode()
            if not more:
                buffering = False
            else:
                self.buffer += more

    def __init__(self):
        print ("Setting up global connection")
        self.buffer=""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("127.0.0.1", 1337))

    