import mouseNode
import mapNode
import sys

import mouseGlobalConnector
import mapGlobal
import tkinter
from time import sleep
def main():
    solution = False

    #Set up a socket connection to the global map
    global_map=mouseGlobalConnector.mouseGlobalConnector()
    (x_pos,y_pos)=global_map.getInitialPosition()

    #create mouse using command line arguments as starting location
    mouse = mouseNode.mouse(x_pos,y_pos, 2,global_map)

    #display mouse in core window/ create core object?
#   start_core()

    root = tkinter.Tk()
    t = tkinter.Text(root, height= 500, width = 500)
    t.pack()

    def forget():
        t.delete("1.0",tkinter.END)
        root.after(0,work)

    def update(xOrg,yOrg):
        options = mouse.get_local_options()
        for x in options:
            #print(*x)
            t.insert(tkinter.END,x)
            t.insert(tkinter.END,'\n')
        root.after(100,forget)




    #while solution != True:
    #if solution != False:
    def work():
        #get sensing data(three distances, left, front,right)
        xOrg = mouse.getXLoc()
        yOrg = mouse.getYLoc()
        sensing = mouse.request_data(mouse.getDir())
        rotation, movement = mouse.next_step(sensing)
        print("{},{}".format(xOrg,yOrg))
        print("Forward {} Left {} Right {}".format(sensing[0].types, sensing[1].types, sensing[2].types))
        print ("Move {} Rotation {}".format(movement,rotation))
        mouse.update_location(rotation,movement)
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
