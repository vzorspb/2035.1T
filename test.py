#! /usr/local/bin/python3.8
import locale
import cgi
import shutil
import cgitb; cgitb.enable()

locale.setlocale(locale.LC_ALL, "")

(width,heigh)=shutil.get_terminal_size()
width-=2
print ("Content-Type: text/plain")
print ("")
print("\u250c"+"\u2500"*width+"\u2510")
x, y = (1234567890, 1234.56)
f="\u2502{0:^"+str(width)+"n}\u2502"

print (f.format(x))
print (f.format(y))

print("\u2514"+"\u2500"*width+"\u2518")

arguments = cgi.FieldStorage()
for i in arguments.keys():
    print (arguments[i].value)
