import xml.etree.ElementTree as ET
import urllib

url=raw_input('Enter Location: ')
fhand=urllib.urlopen(url)
text=str()
for line in fhand:
    text=text+line
#print text
stuff=ET.fromstring(text)
lst=stuff.findall('comments/comment/count')
print len(lst)
s=0
for it in lst:
    s=s+int(it.text)

print s

