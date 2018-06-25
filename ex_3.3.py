score = input("Enter Score: ")
sc = float(score)

if sc > 1.0 :
    print ("Score value is out of range")
    quit()
elif sc < 0 :
    print ("Score value is out of range")
    quit()
elif sc >= 0.9 :
    print("A")
elif sc >= 0.8 :
    print("B")
elif sc >= 0.7 :
    print("C")
elif sc >= 0.6 :
    print("D")
else :
    print("F")
