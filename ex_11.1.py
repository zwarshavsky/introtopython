import re
#fname = input("regex_sum_42.txt")
#if len(fname) < 1 : fname = "regex_sum_42.txt"
fh = open("regex_sum_57014.txt")
numlist = list()
#fp = fh.read()
#for line in fh:
#line = line.rstrip()
for line in fh:
    #line = line.split(",")
    fn = re.findall("[0-9]+",line)
    if len(fn) < 1: continue
    for item in fn:
        item = int(item)
        numlist.append(item)
#res = [int(i) for i in numlist]
print(sum(numlist))
#for line in lines:
#    line = line.rstrip()
#    number = line.split(" ")
