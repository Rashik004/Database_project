import re
l="abcde avd"
string = 'i think mabe 124 + <font color="black"><font face="Times New Roman">but I don\'t have a big experience it just how I see it in my eyes <font color="green"><font face="Arial">fun stuff'
t=re.sub('<.*?>', '', string)
print t
