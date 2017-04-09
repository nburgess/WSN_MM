import mouseNode
import mapNode
import sys

import mouseGlobalConnector
import mapGlobal
import broadcastReceiveThread
import broadcastSendThread

from time import sleep
def main():
    solution = False

    #check to make sure we have the right number of arguments
    if len(sys.argv)!=2:
        print("Invalid arguments!")
        print("usage: mouse.py PRODUCTION_MODE (1=production,0=development")
        return
    production=int(sys.argv[1])

    if production==0:
        import tkinter

    #Set up a socket connection to the global map
    global_map=mouseGlobalConnector.mouseGlobalConnector(production)
    (x_pos,y_pos,dir)=global_map.getInitialPosition()

    #create mouse using command line arguments as starting location
    mouse = mouseNode.mouse(x_pos,y_pos, dir,global_map)

    #set up the broadcast connection for the map
    print("create broadcasters")
    bSender=broadcastSendThread.broadcastSendThread(mouse)
    bReceiver=broadcastReceiveThread.broadcastReceiveThread(mouse)
    print("start broadcasters")
    bSender.start()
    bReceiver.start()

    #display mouse in core window/ create core object?
#   start_core()

    if production==0:
        root = tkinter.Tk()
        t = tkinter.Text(root, height= 500, width = 500)
        t.pack()

    def forget():
        if production==0:
            t.delete("1.0",tkinter.END)
            root.after(0,work)

    def update(xOrg,yOrg):
        if production==0:
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
        sleep(5)
        xOrg = mouse.getXLoc()
        yOrg = mouse.getYLoc()
        sensing = mouse.request_data(mouse.getDir())
        rotation, movement = mouse.next_step(sensing)
        print("{},{}".format(xOrg,yOrg))
        print("Forward {} Left {} Right {}".format(sensing[0].types, sensing[1].types, sensing[2].types))
        print ("Move {} Rotation {}".format(movement,rotation))
        mouse.update_location(rotation,movement)
        solution = mouse.check_goal(mouse.getXLoc(),mouse.getYLoc())
        if solution == False and production==0:
            root.after(0,update(xOrg,yOrg))
    if production==0:
        root.after(1000,work)
        root.mainloop()
    else:
        while 1:
            work()
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
