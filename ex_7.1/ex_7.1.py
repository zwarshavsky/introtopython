fname = input("Enter a file name: ")
fh = open(fname)
fp = fh.read()
print(fp.rstrip().upper())
