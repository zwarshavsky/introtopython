hrs = input("Enter hours:")
rate = input("Enter rate:")
hr = float(hrs)
rt = float(rate)
#regular hour scenario#
if hr <= 40 :
    h = hr * rt
    print(h)
#overtime hour scenario#
else :
    ot = rt * 1.5
    h = (40) * (rt) + (hr-40) * (ot)
    print(h)
