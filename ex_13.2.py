import urllib.request, urllib.parse, urllib.error
import json

url = input('enter url:')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_57019.json"

while True:
    if len(url) < 1: break
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved",len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js:
        print("==============CANT GET IT=============")
        print(data)
        continue

    print(json.dumps(js, indent=4))
    namelist = list()
    for name in js["comments"]:
#        name = int()
        #name = ["comments"]["count"]
        name = (name['count'])
        namelist.append(name)
    print(sum(namelist))
    exit()








#
# #info = json.loads(data)
# #print('User count:', len(info))
#
# #for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])
