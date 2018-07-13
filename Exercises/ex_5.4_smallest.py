smallest_so_far = None
#print("Before", smallest_so_far)
for the_num in [1,2,3,4,5,6,7,8,9,10] :
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    #print(smallest_so_far, the_num)
print(smallest_so_far)
