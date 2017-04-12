import json
from subprocess import call
import io
import simplejson as json
import urllib
import urllib2
import pprint
#call("/home/ipaudit/bin/ipaudit -f 'udp 500000' -m eth0 -c 20 -o /home/core/code/tmp.txt",shell=True)



# Using the newer with construct to close the file automatically.
f = open( "tmp.txt", "r" )
a = []
for line in f:
    print(line)
    a.append(str(line))

#with io.open('jsontraffic.txt','w',encoding = 'utf-8') as f:	f.write(json.dumps(a,ensure_ascii=False))

url ='http://173.198.236.83:3030/uploadNetwork.php'
data = urllib.urlencode({'line':a[0]})
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
the_page = response.read()
print (the_page)
#print(a[0])
