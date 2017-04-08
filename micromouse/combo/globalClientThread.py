import threading
import mapNode
import sys
import mapGlobal
import mouseNodeServer

# This file is in charge of communicating with the clients of the global map
# it accepts requests for movement and processes them
class globalClientThread(threading.Thread):


    #Start the thread when a new client connects
    def run(self):
        command=""

        print("Client connected")
        while 1:
            command=self.fetchLine()
            print(command)
            if command=="start":
                self.socket.send((str(self.mouse.getXLoc())+"\n").encode())
                self.socket.send((str(self.mouse.getYLoc())+"\n").encode())
            elif command=="sense":
                dir_str=self.fetchLine()
                dir=int(dir_str)
                (f,r,l)=self.mouse.request_data(dir)
                self.socket.send((str(f)+"\n").encode())
                self.socket.send((str(r)+"\n").encode())
                self.socket.send((str(l)+"\n").encode())
            elif command=="move":
                dir_str=self.fetchLine()
                dir=int(dir_str)
                success=self.mouse.update_location(dir)
                self.socket.send((str(success)+"\n").encode())

            
        
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


    def __init__(self,socket,mouse):
        self.socket=socket
        self.mouse=mouse
        self.buffer=''
    