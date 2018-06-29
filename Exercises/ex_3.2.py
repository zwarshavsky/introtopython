hrs = input("Enter hours:")
rate = input("Enter rate:")
try:
    hr = float(hrs)
    rt = float(rate)
except:
    print("Error, enter numeric input")
    quit()
if hr <= 40 :
    h = hr * rt
    print(h)
else :
    ot = rt * 1.5
    h = (40) * (rt) + (hr-40) * (ot)
    print(h)
