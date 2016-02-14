import re
import urllib
from BeautifulSoup import *
url = raw_input('Enter URL: ')
count=raw_input('Enter count: ')
position=raw_input('Enter Position: ')
#print url
#print type(url)
#exit()
p=list()
fhand = urllib.urlopen(url)

for j in range (int(count)):
    i=0
    print "Retrieving:",url
    for line in fhand:
            p=re.findall('<a.*>.*?</a>',line)
            if len(p)>0:
                i=i+1
                
            if i>=int(position):
                temp=str(p[0])
                #print temp
                t=re.findall('(http.*)?"', temp)
                url=str(t[1])#######
                #print url
                break
    #print j
    fhand = urllib.urlopen(url)
print "Last Url:", url
#print p
    #p=re.findall('<a.*>(.*)?</a>',p)
