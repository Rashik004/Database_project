import re
name = raw_input("Enter file:")
if len(name) < 1 : name = "real.txt"
final=list()
handle = open(name)
for line in handle:
    line=line.rstrip()
    temp= re.findall('[0-9]+', line)
    if len(temp)>0:
        final=final+temp

s=0
for i in final:
    s=s+int(i)

print s

