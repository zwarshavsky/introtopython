import socket,re
fh = input("Enter a valid URL: ")
if len(fh) < 1: fh = "http://data.pr4e.org/intro-short.txt"
dn = re.findall("http://([a-z]+\S+)\/",fh)
try:
    domain = dn[0]
except:
    print("Invalid URL")
    exit()
domain = str(dn[0])
print(domain)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((domain, 80))
cmd = "GET " + fh + " HTTP/1.0\r\n\r\n"
mysock.send(cmd.encode())

characters = 0
curr_size = 0
data = ""


while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    #print(data[:20].decode(),end='')
    characters = len(data) + characters
    if characters <= 200:
        print(data.decode(),end='')
    #elif (len(data) == 3000):
    #    print(data.decode(),end='')
    #    continue

print("Length of string:",characters)
mysock.close()
