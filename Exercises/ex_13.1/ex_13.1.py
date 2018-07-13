import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_57018.xml'


#address = input('Enter location: ')
#if len(address) < 1: break
#    url = serviceurl + urllib.parse.urlencode({'address': address})
print('Retrieving', url)
uh = urllib.request.urlopen(url).read()
#print(uh)
print('Retrieved', len(uh), 'characters')
data = uh.decode()
#print(data)
tree = ET.fromstring(data)
#print(tree)
countlist=list()
users = tree.findall("comments/comment")
#print(users)
#counts = tree.findall('.//count')
#print(counts)
# #print(counts)
# #print(len(users))
for count in users:
    c = count.find("count").text
    c = int(c)
    countlist.append(c)
print(sum(countlist))






    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    #print('lat', lat, 'lng', lng)
    #print(location)
