import threading
import mapNode
import sys
import mapGlobal
import mouseNode
from time import sleep
from socket import *
from subprocess import call
import coreStartup

# This class is in charge of broadcasting the map to all other mice in the maze
class coreStartupObj(threading.Thread):

    COMMAND_DELAY=5

    #This function broadcasts a copy of the map every WAIT_TO_SEND seconds
    def run(self):
        if self.production==1:
            if self.step==0:
                print("Starting core...")
                core2=coreStartup.coreStartupObj(self.production,self.step+1)
                core2.start()
                call("core-gui /home/core/code/coreConfig/default.xml", shell=True)
            else:
                
                sleep(self.COMMAND_DELAY)
                print("Testing")
                call("coresendmsg node number=2 xpos=0 ypos=0", shell=True)
                sleep(self.COMMAND_DELAY)
                print("Testing2")
                call("coresendmsg node number=2 xpos=0 ypos=0", shell=True)
                sleep(self.COMMAND_DELAY)
                print("Starting node 1...")
                call("coresendmsg exec node=2 num=1001 cmd='python /home/core/code/WSNTRENT/WSN_MM/MICROMOUSE/combo/mouse.py 1'")
                sleep(self.COMMAND_DELAY)
                print("Starting node 2...")
                call("coresendmsg exec node=3 num=1001 cmd='python /home/core/code/WSNTRENT/WSN_MM/MICROMOUSE/combo/mouse.py 1'")
                sleep(self.COMMAND_DELAY)
                print("Starting node 3...")
                call("coresendmsg exec node=4 num=1001 cmd='python /home/core/code/WSNTRENT/WSN_MM/MICROMOUSE/combo/mouse.py 1'")
                sleep(self.COMMAND_DELAY)
                print("Starting node 4...")
                call("coresendmsg exec node=5 num=1001 cmd='python /home/core/code/WSNTRENT/WSN_MM/MICROMOUSE/combo/mouse.py 1'")
            




    def __init__(self,production,step):
        threading.Thread.__init__(self)
        self.production=production
        self.step=step

    
    