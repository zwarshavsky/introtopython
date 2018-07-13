import socket,re
fh = input("Enter a valid URL: ")
if len(fh) < 1: fh = "http://www.google.com/robots.txt"
dn = re.findall("\.([a-z]+\S+)\/",fh)
try:
    domain = dn[0]
except:
    print("Invalid URL")
    exit()
domain = str(dn[0])

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((domain, 80))
cmd = "GET " + fh + " HTTP/1.0\r\n\r\n"
mysock.send(cmd.encode())

while True:
    data = mysock.recv(20)
    if (len(data) < 1):
        break
    print(data.decode(),end='')

mysock.close()
