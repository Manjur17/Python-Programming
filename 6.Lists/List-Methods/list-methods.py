l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)

l.append(7)
l.sort(reverse=True) #descending order
l.reverse()
print(l.index(1))
print(l.count(1))

m = l.copy() #creates new list(deep copy)
m[0] = 0 # changes in m only
l.insert(1, 899)

m = [900, 1000, 1100]
k = l + m
print(k)

l.extend(m) #This method adds an entire list 
# or any other collection datatype (set, tuple, dictionary) to the existing list.


print(l)
