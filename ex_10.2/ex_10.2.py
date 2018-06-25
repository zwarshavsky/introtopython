name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
hours = dict()
for line in fh:
    #line = line.rstrip()
    if line.startswith("From") and "From:" not in line:
        word = line.split()
        #print(word)
        time = word[5]
        time = time.split(":")
        time = time[0]
        hours[time] = hours.get(time,0) + 1
#hs = list()
for key,val in sorted(hours.items(), reverse= True):
    print(key,val)
