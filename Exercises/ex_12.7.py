# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
count = input("Enter Count: ")
count = int(count)
position = input("Enter Position: ")
position = int(position)
position = position - 1
linklist = list()



while count >= 0:
    print(url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = count - 1
    del linklist
    linklist = list()
    tags = soup('a')
    for tag in tags:
        linklist.append(tag.get("href", None))
    url = linklist[position]






#        urllist = linklist

#    url = urllist[2]
    #print(url)

#print("SHANKBONE")






#while count >= 1:
#    print(newurl)
#    url = input('Enter - ')
#    if newurl != None: url = newurl
#    html = urllib.request.urlopen(url, context=ctx).read()
#    soup = BeautifulSoup(html, 'html.parser')
#    count = count - 1
#    tags = soup('a')
#    for tag in tags:
#        linklist.append(tag.get("href", None))
#        newurl = (linklist[0])
#print("SHANKBONE")
