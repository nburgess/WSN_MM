import mouseNode
import mapNode
import sys

import mapGlobal
import Tkinter
from time import sleep
def main():
    solution = False

    our_map = mapGlobal.mapGlobal(33,33)
    input_file = "file.txt"
    our_map.initialize_map(input_file)

    #create mouse using command line arguments as starting location
    mouse = mouseNode.mouse(int(sys.argv[1]),int(sys.argv[2]), 2)

    #display mouse in core window/ create core object?
#   start_core()

    root = tkinter.Tk()
    t = tkinter.Text(root, height= 500, width = 500)
    t.pack()
    lst = [['1','b'],['a','b'],['3','4'],['5','6']]
    def forget():
        t.delete("1.0",tkinter.END)
        root.after(0,work)

    def update(xOrg,yOrg):
        options = mouse.get_local_options()
        for x in options:
            #print(*x)
            t.insert(tkinter.END,x)
            t.insert(tkinter.END,'\n')
        our_map.getNode(xOrg,yOrg).types = 0
        root.after(100,forget)




    #while solution != True:
    #if solution != False:
    def work():
        #get sensing data(three distances, left, front,right)
        xOrg = mouse.getXLoc()
        yOrg = mouse.getYLoc()

        our_map.getNode(xOrg,yOrg).types = 5
        sensing = mouse.request_data(mouse.getXLoc(),mouse.getYLoc(),mouse.getDir(),our_map)
        rotation, movement = mouse.next_step(sensing)
        print("{},{}".format(xOrg,yOrg))
        print("Forward {} Left {} Right {}".format(sensing[0].types, sensing[1].types, sensing[2].types))
        print ("Move {} Rotation {}".format(movement,rotation))
        print(our_map.getNode(0,0).types)
        mouse.update_location(rotation,movement)
        mouse.update_global(xOrg,yOrg,our_map)
        solution = mouse.check_goal(mouse.getXLoc(),mouse.getYLoc())
        if solution == False:
            root.after(0,update(xOrg,yOrg))
    root.after(1000,work)
    root.mainloop()
        #if(rotation,movement) run_active = False
#        if rotation == -90:

#        elif rotation == 90:

#        elif rotation == 0:
#            pass
#        else:
#            print("Invalid rotation")

#        while movement:
#            if movement > 0:

#                movement -= 1
#            else:
#                print("stopped by wall")
#            else:
                #reverse
        #check if goal is found

        #get data from global map, update local map
#        mouse.request_data(mouse.getXLoc(),mouse.getYLoc(),mouse.getDir(),our_map)

        #this data is then used to update location
#        mouse.update_location()

        #?when we are sending the maze info back out there should also be a bool marking if there
        #?is a mouse in adjacent squares, this would be an automatic turn around

        #display mouses new location on core window
#        mouse.send_data()

        #check if solution is within tile
#        solution = our_map.check_solution()
    print("Center Found!")


if __name__ == "__main__":
    main()
