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

url = input('Enter:')
if len(url) < 1: url = "http://www.dr-chuck.com/page1.htm"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


tcount = 0
# Retrieve all of the anchor tags
tags = soup('p')
for tag in tags:
    #print(tag.get('href', None))
    tcount = tcount + 1
print(tcount)
