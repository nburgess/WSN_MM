import mapNode

class mouse:
    #anything here is shared by all instances
    w = 33
    h = 33

    def __init__(self, xstart, ystart):
        self.xloc = xstart
        self.yloc = ystart
        self.Map = [[mapNode.mapNode() for x in range(33)] for y in range(33)]
        #Map[xstart][ystart].value = 1

    #get data about current cell from global map
    #update local map
    def request_data(self):
        #call core function here: should recieve visible data form global_map
        #this function should then update local map
    #   core_function?
        do


    #determine direction to move and take step
    def update_location(self):
        #self.xloc update
        #self.yloc update
        do

    #display mouse in core
    def send_data(self):
        do
        stuff

    #check for the center of the map, return True
    def check_solution(self):
        return True
