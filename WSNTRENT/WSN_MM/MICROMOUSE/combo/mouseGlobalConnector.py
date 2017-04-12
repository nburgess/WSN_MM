import mapNode
import sys
import mapGlobal
import socket

# This file is in charge of communicating with the clients of the global map
# it accepts requests for movement and processes them
class mouseGlobalConnector:

    development_ip="127.0.0.1"
    production_ip="172.16.0.254"
    MAP_SIZE=1089 #33x33

    #This function will get the mouse's position from the global map
    #it is usually only used when the program starts but can be called
    #to get the position at any time
    def getInitialPosition(self):
       print("Fetching position")
       self.socket.send("start\n".encode())
       number_str=self.fetchLine()
       x_str=self.fetchLine()
       y_str=self.fetchLine()
       dir_str=self.fetchLine()
       print("("+x_str+","+y_str+")")
       number=int(number_str)
       x_pos=int(x_str)
       y_pos=int(y_str)
       dir=int(dir_str)
       return (number,x_pos,y_pos,dir)

    #This function returns whether or not there is a wall to the front
    #left and right of the mouse to help
    #
    # returns (f_val,r_val,l_val)
    #   f_val=1 if wall in front
    #   r_val=1 if wall to right
    #   l_val=1 if wall to left
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

    #This function move the mouse one block in the indicated dirrection
    #on the global map. If the function returns 0 there was a wall blocking
    # the mouses' movement
    #   0 up
    #   1 right
    #   2 down
    #   3 left
    #
    def requestMovement(self,dir):
        print("Requesting movement")
        self.socket.send("move\n".encode())
        self.socket.send((str(dir)+"\n").encode())
        success_str=self.fetchLine()
        success=int(success_str)
        return success


    def sendMap(self,typeList,optionList):
        buffer=''

        #Convert typeList to buffer
        for x in range(0,self.MAP_SIZE):
            buffer+=str(typeList[x])

        #Convert optionList to buffer
        for x in range(0,self.MAP_SIZE):
            buffer+=str(optionList[x])

        self.socket.send("map\n".encode())
        self.socket.send((buffer+"\n").encode())


    def sendIpLine(self,line):
        self.socket.send("ipaudit\n".encode())
        self.socket.send(line.encode())

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


    def __init__(self,production):
        print ("Setting up global connection")
        self.buffer=""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if production==1:
            self.socket.connect((self.production_ip, 1337))
        else:
            self.socket.connect((self.development_ip, 1337))
