import mapNode
import sys
import socket
import mapGlobal
import globalClientThread
import globalProgram
import mouseNodeServer

#The global program is in charge of managing the globalMap object and
# listening for requests from the mice for movement informaiton
class globalProgram:


    #This function creaes a copy of the global map, creates four mice,
    # and then listen for communication requests from the mice
    def main():
        print("Starting global program")

        #Create the global map we will use to check for movement paths
        our_map = mapGlobal.mapGlobal(33,33)
        input_file = "file.txt"
        our_map.initialize_map(input_file)

        #create four mice and set
        mouseCount=0
        mouse1=mouseNodeServer.mouse(1,1, 2,our_map,1)
        mouse2=mouseNodeServer.mouse(31,1, 1,our_map,2)
        mouse3=mouseNodeServer.mouse(1,31, 3,our_map,3)
        mouse4=mouseNodeServer.mouse(31,31, 0,our_map,4)

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
