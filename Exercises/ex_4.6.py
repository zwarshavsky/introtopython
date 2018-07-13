def computepay(h,r):
    hrs = float(h)
    rt = float(r)
    if hrs > 40:
        th = (hrs * rt) + (hrs - 40) * (rt * 0.5)
    else:
        th = hrs * rt
    return th

h = input("Enter Hours:")
r = input("Enter Rate:")
p = computepay(h,r)
print(p)
