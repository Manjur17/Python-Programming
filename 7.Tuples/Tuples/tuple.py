tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90  ERROR
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34]) ERROR -> index out of bound

if 3421 in tup:
    print("Yes 342 is present in this tuple")
else:
    print("No 342 is present in this tuple")

tup2 = tup[1:4] #returns new list
print(tup2)
