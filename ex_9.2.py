name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = dict()
#print(dir(fh))
for line in fh:
    if line.startswith("From") and "From:" not in line:
        name = line.split()
        day = name[2]
        counts[day] = counts.get(day,0) + 1
print(counts)
