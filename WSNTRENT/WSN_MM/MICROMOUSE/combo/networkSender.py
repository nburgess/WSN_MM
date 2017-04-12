import threading
import mapNode
import sys
import mapGlobal
import mouseNode
from time import sleep
from socket import *
import io
from subprocess import call
import mouseGlobalConnector

# This class is in charge of broadcasting the map to all other mice in the maze
class networkSender(threading.Thread):

    MYPORT = 50000 #port that we will send data to
    MAP_SIZE=1089 #33 x 33
    WAIT_TO_SEND=60 #time delay between each map send

    #This function broadcasts a copy of the map every WAIT_TO_SEND seconds
    def run(self):
        command=""
        url ='http://173.198.236.83:3030/uploadNetwork.php'

        print("Started Network Thread")

        while 1:
            #Look for network traffic
            print("Reading network data================")
            call("/home/ipaudit/bin/ipaudit -f 'udp 500000' -m eth0 -c 20 -o /home/core/code/networkTraffic"+self.node+".txt",shell=True)
            
            #upload network traffic to server
            f = open( "/home/core/code/networkTraffic.txt", "r" )
            for line in f:
                self.connector.sendIpLine(line)
            print("Sent network data================")


	    

    def __init__(self,node,connector):
        threading.Thread.__init__(self)
        self.node=str(node)
        self.connector=connector

    
    