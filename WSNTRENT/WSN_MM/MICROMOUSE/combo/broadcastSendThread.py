import threading
import mapNode
import sys
import mapGlobal
import mouseNode
from time import sleep
from socket import *

# This class is in charge of broadcasting the map to all other mice in the maze
class broadcastSendThread(threading.Thread):

    MYPORT = 50000 #port that we will send data to
    MAP_SIZE=1089 #33 x 33
    WAIT_TO_SEND=2 #time delay between each map send

    #This function broadcasts a copy of the map every WAIT_TO_SEND seconds
    def run(self):
        command=""

        print("STARTED!!!!!!!")


        while 1:
            #only send the map once every WAIT_TO_SEND seconds
            sleep(self.WAIT_TO_SEND)
            print("Sending map")
            sendMap=[]
            buffer=''

            nodeList=self.mouse.generate_sendlist()
            typeList=nodeList[0]
            optionList=nodeList[1]

            #Convert typeList to buffer
            for x in range(0,self.MAP_SIZE):
                buffer+=str(typeList[x])

            #Convert optionList to buffer
            for x in range(0,self.MAP_SIZE):
                buffer+=str(optionList[x])

            #broadcast map
            self.s.sendto(buffer.encode(), ('10.0.0.255', self.MYPORT))




    def __init__(self,mouse):
        threading.Thread.__init__(self)
        self.mouse=mouse

        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.s.bind(('', self.MYPORT))
        self.s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    
    