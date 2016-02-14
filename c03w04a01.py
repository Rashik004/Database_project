# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import re
import urllib
from BeautifulSoup import *

i=5;

url = raw_input('Enter URL:')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

sum=0
# Retrieve all of the span tags
tags = soup('span')

for tag in tags:
   s=str(tag.contents)
   p=re.findall('[0-9]+',s)
   for i in range(len(p)):
       sum=sum+int(p[i])
print sum
   
   
