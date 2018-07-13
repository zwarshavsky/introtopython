# import sys
# sys.stdout = open('text.log', 'w')
# if True:
#     g = "shamckle"
#     print (g)
#     #f.write(g)
#     h = "shamckleDbitch"
#     print (h)
#     #f.write(h)
# else:
#     print("goodbye world")


class Tee:
    def write(self, *args, **kwargs):
        self.out1.write(*args, **kwargs)
        self.out2.write(*args, **kwargs)
    def __init__(self, out1, out2):
        self.out1 = out1
        self.out2 = out2
    def flush(self):
        pass

import sys
sys.stdout = Tee(open("text.log", "w"), sys.stdout)


if True:
    g = "shamckle"
    print (g)
    #f.write(g)
    h = "shamckleDbitch"
    print (h)
    #f.write(h)
else:
    print("goodbye world")
