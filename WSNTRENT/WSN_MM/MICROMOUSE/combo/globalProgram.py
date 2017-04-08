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
        mouse1=mouseNodeServer.mouse(1,1, 2,our_map)
        mouse2=mouseNodeServer.mouse(32,1, 2,our_map)
        mouse3=mouseNodeServer.mouse(1,32, 2,our_map)
        mouse4=mouseNodeServer.mouse(32,32, 2,our_map)

        #set up a socket and listen for mice movement requests
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("127.0.0.1", 1337))
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
            clientThread.run()




    if __name__ == "__main__":
        main()
