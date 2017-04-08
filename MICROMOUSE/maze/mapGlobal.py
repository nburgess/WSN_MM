import mapNode
import sys

class mapGlobal:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.Map = [[mapNode.mapNode() for x in range(w)] for y in range(h)]

    def getNode(self,x,y):
        return self.Map[x][y]

    def setNode(self,x,y,val):
        self.Map[x][y] = val

    def initialize_map(self,input_file):
        with open(input_file, 'r') as f:
            return self.map_start(f)

    def map_start(self,open_file):
        i = 0
        j = 0
        counter = 0
        while True:
            c = open_file.read(1)
            if not c:
                print("End of file")
                break
            if c == '+' or c =='|' or c == '-':
                #sys.stdout.write(str(j))
                self.Map[i][j].types = 1
                sys.stdout.write(str(self.Map[i][j].types))
                j +=1
            elif c == '\n':
                print("")
                #print(self.Map[i][j].types)
                i +=1
                j = 0
            elif c == ' ':
                self.Map[i][j].types = 0
                sys.stdout.write(str(self.Map[i][j].types))
                j +=1
            else:
                print("There is an unrecognized character in map file!")
            #print c

    def blend_map(self,mouse_map):
        i = 0
        j = 0
        for i in range(0,33):
            for j in range(0,33):
                if self.getNode(i,j).options < mouse_map.getNode(i,j).options:
                    self.Map[i][j] = mouse_map.getNode(i,j)

    def print_map(self):
        i = 0
        j = 0
        for i in range(0,33):
            for j in range(0,33):
                sys.stdout.write(str(self.Map[i][j].options))
            print("")

    def check_for_request():
        send_data()
        return True

    #return data back to mouse
    def send_data():
        do
        stuff
