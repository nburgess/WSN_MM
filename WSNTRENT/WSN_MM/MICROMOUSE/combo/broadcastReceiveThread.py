import threading
import mapNode
import sys
import mapGlobal
import mouseNode
from time import sleep
from socket import *

# This class is in charge of receiving the map from other mice on the field
class broadcastReceiveThread(threading.Thread):

    MYPORT = 50000 #port that we will receive data on
    MAP_SIZE=1089 #33x33

    #This function constantly looks for maps being sent to us
    def run(self):
        command=""

        print("Client connected")
        while 1:
            nodeList=None
            typeList=[]
            optionList=[]
            loaded=0
            buffer=''
            
            #get data from socket
            while (loaded<(self.MAP_SIZE*2)):
                newData,address = self.s.recvfrom(self.MAP_SIZE*2)
                loaded+=len(newData)
                buffer+=newData.decode()

            #load type list
            for x in range(0,self.MAP_SIZE):
                mapLine_str=buffer[x]
                mapLine=int(mapLine_str)
                typeList.append(mapLine)

            #load option list
            for x in range(0,self.MAP_SIZE):
                mapLine_str=buffer[x+self.MAP_SIZE]
                mapLine=int(mapLine_str)
                optionList.append(mapLine)

            nodeList=[typeList,optionList]
            print("Loaded full map!")
            self.mouse.combine_map(nodeList)

            
    #This function fetches the next line of communication
    # from the global map program
    def fetchLine(self):
        buffering = True
        while buffering:
            if "\n" in self.buffer:
                (line, self.buffer) = self.buffer.split("\n", 1)
                return line
            else:
                more,address = self.s.recvfrom(4096)
                more=more.decode()
            if not more:
                buffering = False
            else:
                self.buffer += more


    def __init__(self,mouse):
        threading.Thread.__init__(self)
        self.mouse=mouse
        self.buffer=''

        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.s.bind(('', self.MYPORT))
        self.s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    
    