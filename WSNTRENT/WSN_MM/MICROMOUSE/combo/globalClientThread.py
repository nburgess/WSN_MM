import threading
import mapNode
import sys
import mapGlobal
import mouseNodeServer
from socket import *
import json
import io
import urllib
import urllib2

# This file is in charge of communicating with the clients of the global map
# it accepts requests for movement and processes them
class globalClientThread(threading.Thread):

    MAP_SIZE=1089 #33x33

    #This function constantly checks for messages from the client
    def run(self):
        command=""

        print("Client connected")
        while 1:
            command=self.fetchLine()
            print(command)
            if command=="start":
                print("Sending position")
                self.socket.send((str(self.mouse.getNumber())+"\n").encode())
                self.socket.send((str(self.mouse.getXLoc())+"\n").encode())
                self.socket.send((str(self.mouse.getYLoc())+"\n").encode())
                self.socket.send((str(self.mouse.getDir())+"\n").encode())
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
            elif command=="map":
                fat_line_str=self.fetchLine()
                (typeList,optionList)=self.bufferToArray(fat_line_str)
                #write JSON conversion 
                url = 'http://173.198.236.83:3030/uploadMap.php'
                data = urllib.urlencode({'mouse': self.mouse.getNumber(), 'types': typeList, 'options': optionList})
                req = urllib2.Request(url, data)
                #req = urllib2.urlopen(url=url, data=data)
                response = urllib2.urlopen(req)
            elif command=="ipaudit":
                ip_audit_line=self.fetchLine()
                url ='http://173.198.236.83:3030/uploadNetwork.php'
                data = urllib.urlencode({'line':ip_audit_line})
                req = urllib2.Request(url,data)
                response = urllib2.urlopen(req)

    def bufferToArray(self,buffer):
        typeList=[]
        optionList=[]

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

        return (typeList,optionList)
            

    #This function fetches the next line of communication
    # from the global map program
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
        threading.Thread.__init__(self)
        self.socket=socket
        self.mouse=mouse
        self.buffer=''
    
    