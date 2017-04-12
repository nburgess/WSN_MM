import mapNode
import sys
import socket
import mapGlobal
import globalClientThread
import globalProgram
import mouseNodeServer
import coreStartup
import networkSender

#The global program is in charge of managing the globalMap object and
# listening for requests from the mice for movement informaiton
class globalProgram:


    #This function creaes a copy of the global map, creates four mice,
    # and then listen for communication requests from the mice
    def main():
        print("Starting global program")

        #check to make sure we have the right number of arguments
        if len(sys.argv)!=5:
            print("Invalid arguments!")
            print("usage: mouse.py PRODUCTION_MODE MAZE_TEXT_FILE MAZE_IMAGE_FILE DISTANCE_LEVEL")
            print("PRODUCTION: 0=development, 1=production")
            print("in development file paths are based off the local directory")
            print("in production file paths are based off /home/core/code/mazeFiles")
            print("DISTANCE_LEVEL: 0=150m, 1=400m, 2=1500m")
            return
        production=int(sys.argv[1])
        text_file=sys.argv[2]
        image_file=sys.argv[3]
        distance=int(sys.argv[4])

        #Create the global map we will use to check for movement paths
        our_map = mapGlobal.mapGlobal(33,33)
        if production==0:
            input_file=text_file
        else:
            input_file = "/home/core/code/mazeFiles/"+text_file
        our_map.initialize_map(input_file)

        #create four mice and set
        mouseCount=0
        mouse1=mouseNodeServer.mouse(1,1, 2,our_map,1)
        mouse2=mouseNodeServer.mouse(31,1, 1,our_map,2)
        mouse3=mouseNodeServer.mouse(1,31, 3,our_map,3)
        mouse4=mouseNodeServer.mouse(31,31, 0,our_map,4)

        #startup core
        core=coreStartup.coreStartupObj(production,0,image_file,distance)
        core.start()

        #start looking for network data
        network=networkSender.networkSender()
        network.start()

        #set up a socket and listen for mice movement requests
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 1337))
        server_socket.listen(5)
        while 1:
            mouseCount+=1
            if mouseCount==1:
                mouse=mouse1
            elif mouseCount==2:
                mouse=mouse2
            elif mouseCount==3:
                mouse=mouse3
            else:
                mouse=mouse4
            (client_socket, address) = server_socket.accept()
            clientThread=globalClientThread.globalClientThread(client_socket,mouse)
            print("Client oject created")
            clientThread.start()
            print("Client object started")




    if __name__ == "__main__":
        main()
