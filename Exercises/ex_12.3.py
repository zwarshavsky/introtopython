import urllib.request, urllib.parse, urllib.error,re

fh = input("Enter a valid URL: ")
if len(fh) < 1: fh = "http://www.google.com/robots.txt"
with urllib.request.urlopen(fh) as myurl:
    wt="".join(line.decode() for line in myurl)

#characters = 0

#for line in fhand:
#    print(line)
#    print(line)
#    characters = len(line) + characters
#    if characters <= 3000:
#        print(line.strip())

print(wt[0:3000] + "\n",len(wt))
