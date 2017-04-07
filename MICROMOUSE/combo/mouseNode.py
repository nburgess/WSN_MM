import mapNode
import mapGlobal

class mouse:
    #anything here is shared by all instances
    w = 33
    h = 33

    def __init__(self, xstart, ystart, dstart):
        self.posStack = []
        self.xloc = xstart
        self.yloc = ystart
        self.dir = dstart
            #starting direction
            #0 up
            #1 right
            #2 down
            #3 left
        self.my_map = mapGlobal.mapGlobal(33,33)
        #Map[xstart][ystart].value = 1

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
    def request_data(self,x,y,dir,map):
        #get global map data
        nodePacket = [map.getNode(x-1,y-1),map.getNode(x-1,y),map.getNode(x-1,y+1),
                      map.getNode(x,y-1),map.getNode(x,y),map.getNode(x,y+1),
                      map.getNode(x+1,y-1),map.getNode(x+1,y),map.getNode(x+1,y+1)]
        #update local map
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                a = nodePacket[count]
                self.my_map.setNode(x+i,y+j,a)
                count += 1
        #get sensing data from updated local map
        if dir==0:
            f = self.my_map.getNode(x-1,y)
            l = self.my_map.getNode(x,y-1)
            r = self.my_map.getNode(x,y+1)
        elif dir==1:
            f = self.my_map.getNode(x,y+1)
            l = self.my_map.getNode(x-1,y)
            r = self.my_map.getNode(x+1,y)
        elif dir==2:
            f = self.my_map.getNode(x+1,y)
            l = self.my_map.getNode(x,y+1)
            r = self.my_map.getNode(x,y-1)
        elif dir==3:
            f = self.my_map.getNode(x,y-1)
            l = self.my_map.getNode(x+1,y)
            r = self.my_map.getNode(x-1,y)
        data = [f,l,r]
        return data
        #call core function here: should recieve visible data form global_map
        #this function should then update local map
        #core_function?

    def update_global(self,x,y,map):
        #get local map data
        nodePacket = [self.my_map.getNode(x-1,y-1),self.my_map.getNode(x-1,y),self.my_map.getNode(x-1,y+1),
                      self.my_map.getNode(x,y-1),self.my_map.getNode(x,y),self.my_map.getNode(x,y+1),
                      self.my_map.getNode(x+1,y-1),self.my_map.getNode(x+1,y),self.my_map.getNode(x+1,y+1)]
        #update global map
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                a = nodePacket[count]
                map.setNode(x+i,y+j,a)
                count += 1

    def get_local_options(self):
        return self.my_map.getOptions()

    #determine direction to move and take step
    def next_step(self,data):
        #check forward
        if data[0].types == 0 and data[0].options == 0:#!=2
            rotation = 0
            movement = 1
        #check left
        elif data[1].types == 0 and data[1].options ==0:
            rotation = -90
            movement = 1
        #check right
        elif data[2].types == 0 and data[2].options ==0:
            rotation = 90
            movement = 1
        else:
            rotation = 180
            movement = -1

        return rotation, movement

    def update_location(self,rotation, movement):
        oldDir = self.dir
        if rotation == -90:
            self.dir -= 1
            if self.dir == -1:
                self.dir = 3
        elif rotation == 90:
            self.dir += 1
            if self.dir == 4:
                self.dir = 0
        elif rotation == 0:
            pass
        else:
            print("Invalid rotation")

        #while movement != 0:
        if movement == 1:
            self.my_map.getNode(self.xloc,self.yloc).options = 1
            old = [self.xloc,self.yloc,oldDir]
            self.push(old)
            if self.dir == 0:
                self.xloc -=1
            elif self.dir == 1:
                self.yloc +=1
            elif self.dir == 2:
                self.xloc +=1
            elif self.dir == 3:
                self.yloc -=1
            #movement -= 1
        elif movement == -1:
            self.my_map.getNode(self.xloc,self.yloc).options = 2
            set = self.pop()
            self.xloc = set[0]
            self.yloc = set[1]
            self.dir = set[2]
            print("pop stack")
        else:
            print("stopped by wall")
                #reverse
        #check if goal is found

    #create a non-double list to be sent between mice
    def generate_sendlist(self):
        size = 1089
        nodeList = [mapNode.mapNode() for x in range(size)];
        count = 0
        #x(up/down)
        for i in range(0,33):
            #y(left,right)
            for j in range(0,33):
                nodeList[count]=self.my_map.getNode(i,j)
                count += 1
        return nodeList

    #takes incoming shared mouse map and combines it with my_map
    def combine_map(self,nodeList):
        count = 0
        #x(up/down)
        for i in range(0,33):
            #y(left,right)
            for j in range(0,33):
                node = nodeList[count]
                if self.my_map.getNode(i,j).types == 8:
                    self.my_map.setNode(i,j,node)
                if self.my_map.getNode(i,j).options < node.options:
                    self.my_map.setNode(i,j,node)
                count+=1


    #display mouse in core
    def send_data(self):
        do
        stuff

    #check for the center of the map, return True
    def check_goal(self,x,y):
        if x == 15 and y == 15:
            return True
        else:
            return False

    #stack
    def DisplayStack():
        print("Stack currently contains:")
        for Item in MyStack:
            print(Item)

    def push(self,value):
        self.posStack.append(value)

    def pop(self):
        if len(self.posStack) > 0:
            return self.posStack.pop()
        else:
            print("Stack is empty.")
