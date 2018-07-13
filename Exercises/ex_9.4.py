name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = dict()
for line in fh:
    if line.startswith("From:"):
        name = line.split()
        del(name[0])
        #print(name)
        for word in name:
            # retrieve/create/update counter
            counts[word] = counts.get(word,0) + 1
            #print(word,counts[word])
            #print(counts)

#max_value = max(counts.values()
#max_keys = [(k,v)for k, v in counts.items() if v == max_value]
#print(max_value, max_keys)

bigcount = None
bigword = None
for sender,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = sender #capture/remember the bigword that was largest
        bigcount = count
print (bigword, bigcount)
