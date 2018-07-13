import re
x = "shmacky had a whacky Memphis, what@buddha!!!"
y = re.findall("@(\S+)",x)
print(y)
