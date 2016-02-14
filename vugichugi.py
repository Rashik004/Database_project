import json
import urllib

url=raw_input('Enter Location: ')
if len(url)<1:
    url='http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_191199.json'
fhand=urllib.urlopen(url)
data=fhand.read()
#print type(data)
#print data
c=0
temp=json.loads(data)
print type(temp['comments'][0])
sum=0
for item in temp['comments']:
    sum=sum+int(item['count'])
print 'Count:', len(temp['comments'])
print 'Sum:',sum



