fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From:"):
        #name = line.rstrip()
        name = line.split()
        print(name[1])
        count = count + 1
        continue
    #if len(fname) < 1 : fname = "mbox-short.txt"
print("There were", count, "lines in the file with From as the first word")
