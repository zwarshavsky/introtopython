fname = input("Enter file name: ")
fh = open(fname)
numlist=list()
for line in fh:
    word = line.rstrip()
    word = line.split()
    for i in word:
        if i in numlist: continue
        if i not in numlist:
            numlist.append(i)
            numlist.sort()
print(numlist)

#word = numlist.split()
#word.sort()
