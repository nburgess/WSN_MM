import mapNode
import mapGlobal
from subprocess import call

class mouse:
    #anything here is shared by all instances
    w = 33
    h = 33
    NODE_OFFSET=0 #The offset that should be added to the mouse number (eg. offset of one means the first mouse in core is node2)
    MOVE_OFFSET=20

    def __init__(self, xstart, ystart, dstart,map,number):
        self.posStack = []
        self.xloc = xstart
        self.yloc = ystart
        self.dir = dstart
            #starting direction
            #0 up
            #1 right
            #2 down
            #3 left
        self.my_map = map
        self.number=int(number)
        #Map[xstart][ystart].value = 1
     
    def getNumber(self):
        return self.number
    def getXLoc(self):
        return self.xloc
    def getYLoc(self):
        return self.yloc
    def setLocation(self,x,y):
        self.xloc = x
        self.yloc = y

    def getDir(self):
        return self.dir
    def setDir(self,dir2):
        self.dir = dir2

    #get data about current cell from global map
    #update local map
    def request_data(self,dir):
        x=self.xloc
        y=self.yloc
        print(str(x)+","+str(y)+"-"+str(dir))

        #get sensing data from updated local map
        if dir==0:
            f = self.my_map.getNode(x-1,y).types
            l = self.my_map.getNode(x,y-1).types
            r = self.my_map.getNode(x,y+1).types
        elif dir==1:
            f = self.my_map.getNode(x,y+1).types
            l = self.my_map.getNode(x-1,y).types
            r = self.my_map.getNode(x+1,y).types
        elif dir==2:
            f = self.my_map.getNode(x+1,y).types
            l = self.my_map.getNode(x,y+1).types
            r = self.my_map.getNode(x,y-1).types
        elif dir==3:
            f = self.my_map.getNode(x,y-1).types
            l = self.my_map.getNode(x+1,y).types
            r = self.my_map.getNode(x-1,y).types
        return (f,r,l)
        #call core function here: should recieve visible data form global_map
        #this function should then update local map
        #core_function?



    def update_location(self,dir):

        newX=self.xloc
        newY=self.yloc

        if dir == 0:
            newX -=1
        elif dir == 1:
            newY +=1
        elif dir == 2:
            newX +=1
        elif dir == 3:
            newY -=1

        print("("+str(self.xloc)+","+str(self.yloc)+")-("+str(newX)+","+str(newY)+")-"+str(self.my_map.getNode(newX,newY).types)+"-"+str(self.my_map.getNode(self.xloc,self.yloc).types))
        if self.my_map.getNode(newX,newY).types==1:
            return 0
        else:
            self.xloc=newX
            self.yloc=newY
            newX2=newX*self.MOVE_OFFSET-12
            newY2=newY*self.MOVE_OFFSET-12
            nodeNum=self.number+self.NODE_OFFSET
            call("coresendmsg node number="+str(nodeNum)+" xpos="+str(newY2)+" ypos="+str(newX2), shell=True)
            return 1
      
