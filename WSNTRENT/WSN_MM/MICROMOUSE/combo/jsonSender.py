import threading
import mapNode
import sys
import mapGlobal
import mouseNode
from time import sleep
from socket import *
import io
import urllib
import mouseGlobalConnector

# This class is in charge of broadcasting the map to all other mice in the maze
class jsonSender(threading.Thread):

    MYPORT = 50000 #port that we will send data to
    MAP_SIZE=1089 #33 x 33
    WAIT_TO_SEND=20 #time delay between each map send

    #This function broadcasts a copy of the map every WAIT_TO_SEND seconds
    def run(self):
        command=""

        print("Started JSON Thread")

        while 1:
            #only send the map once every WAIT_TO_SEND seconds
            sleep(self.WAIT_TO_SEND)
            print("Sending map to server")
            sendMap=[]
            buffer=''

            nodeList=self.mouse.generate_sendlist()
            typeList=nodeList[0]
            optionList=nodeList[1]
            self.clientConnector.sendMap(typeList,optionList)
            
            #write JSON conversion 
            #sleep(self.WAIT_TO_SEND)
	    #with io.open('jsondata.txt', 'w', encoding='utf-8') as f:
             	#f.write(json.dumps(nodeList, ensure_ascii=False))

	   	#a = json.dumps(nodeList, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
		#f.write(unicode(a))

	    #url = 'http://173.198.236.83:3030/uploadMap.php'
	    #data = urllib.urlencode({'mouse': self.mouse.getNumber(), 'types': typeList, 'options': optionList})
	    #req = urllib2.Request(url, data)
	    #req = urllib2.urlopen(url=url, data=data)
	    #response = urllib2.urlopen(req)
	    #the_page = response.read()
	    #print the_page
	    
 
	    #with io.open('jsondata.txt', 'w', encoding='utf-8') as outfile:
	    	#str_ = json.dumps(nodeList, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
		#outfile.write(unicode(str_))

	    

    def __init__(self,mouse,clientConnector):
        threading.Thread.__init__(self)
        self.mouse=mouse
        self.clientConnector=clientConnector
    

        #self.s = socket(AF_INET, SOCK_DGRAM)
        #self.s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        #self.s.bind(('', self.MYPORT))
        #self.s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    
    