text = "X-DSPAM-Confidence:    0.8475";
f1 = text.find("0")
#print (f1)
f2 = text.find("5",f1)
#print (f2)
f3 = text[f1+1 : f2+1]
f3 = float(f3)
print(f3)
