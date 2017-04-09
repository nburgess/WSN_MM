import threading
import mapNode
import sys
import mapGlobal
import mouseNode
from time import sleep
from socket import *
from subprocess import call

# This class is in charge of broadcasting the map to all other mice in the maze
class coreStartup(threading.Thread):

    COMMAND_DELAY=5

    #This function broadcasts a copy of the map every WAIT_TO_SEND seconds
    def run(self):
        if self.production==1:
            call("core-gui /home/core/code/coreConfig/default.xml", shell=True)
            sleep(COMMAND_DELAY)
            call("coresendmsg exec node=2 num=1001 cmd='/home/core/code/WSNTRENT/WSN_MM/MICROMOUSE/combo/mouse.py 1')
            sleep(COMMAND_DELAY)
            call("coresendmsg exec node=3 num=1001 cmd='/home/core/code/WSNTRENT/WSN_MM/MICROMOUSE/combo/mouse.py 1')
            sleep(COMMAND_DELAY)
            call("coresendmsg exec node=4 num=1001 cmd='/home/core/code/WSNTRENT/WSN_MM/MICROMOUSE/combo/mouse.py 1')
            sleep(COMMAND_DELAY)
            call("coresendmsg exec node=5 num=1001 cmd='/home/core/code/WSNTRENT/WSN_MM/MICROMOUSE/combo/mouse.py 1')
            




    def __init__(self,production):
        threading.Thread.__init__(self)
        self.production=production

    
    