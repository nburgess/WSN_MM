import json
from subprocess import call
import io
import simplejson as json
call("./ipaudit -f "udp 500000" -m eth0 -o /home/tmp.txt")



# Using the newer with construct to close the file automatically.
	f = open( "tmp.txt", "r" )
	a = []
	for line in f:
    a.append(line)


	with io.open('jsontraffic.txt','w',encoding = 'utf-8') as f:	f.write(json.dumps(a,ensure_ascii=False))

	url ='http://173.198.236.83:3030/uploadNetwork.php'
	data = urllib.urlencode({'lines':a})
	req = urllib2.Request(url,data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print (the_page)
