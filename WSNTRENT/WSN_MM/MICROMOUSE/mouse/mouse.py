import mouseNode
import mapNode
import sys

def main():
    solution = False

    #create mouse using command line arguments as starting location
    mouse = mouseNode.mouse(sys.argv[1],sys.argv[2])

    #display mouse in core window/ create core object?
#   start_core()

    while solution != true:

        #get data from global map, update local map
        request_data()

        #this data is then used to update location
        update_location()

        #?when we are sending the maze info back out there should also be a bool marking if there
        #?is a mouse in adjacent squares, this would be an automatic turn around

        #display mouses new location on core window
        send_data()

        #check if solution is within tile
        solution = mapGlobal.check_solution()



if __name__ == "__main__":
    main()
