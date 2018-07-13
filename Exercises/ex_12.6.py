# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
num = 0
numlist = list()
tags = soup('span')
for tag in tags:
#    tag = int(tag)
#    # Look at the parts of a tag
#
#    print('TAG:', tag)
#    print('URL:', tag.get('href', None))
#    numbers = tag

    numlist.append(int(tag.contents[0]))

#    print('Contents:', tag.contents[0]))
#    print('Attrs:', tag.attrs)
print(sum(numlist))
#print(sum(tag.contents[0]))
