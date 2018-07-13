# Use the file name mbox-short.txt as the file name


fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    if fname == "fuck you":
        print("got you, asshole")
        exit()
    else:
        print("unkown filename:", fname)
        exit()

count = 0
f3 = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        f1 = line.find ("0")
        f2 = line[f1 : ]
        f2 = float(f2)
        f3 = f2 + f3
        count = count + 1
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
print("Average spam confidence:",(f3/count))
