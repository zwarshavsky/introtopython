num = 0
tot = 0.0

while True:
    sval = input("enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print("invalid number")
        continue
    fval = float(sval)
    num = num + 1
    tot = tot + fval
print(tot, num, tot/num)
