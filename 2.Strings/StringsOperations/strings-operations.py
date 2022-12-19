
fruit = "Mango"
mangoLen = len(fruit) #length of string
print(mangoLen)

# print(fruit[0:4]) # including 0 but not 4
# print(fruit[1:4]) # including 1 but not 4
# print(fruit[:5]) # starts from 0
# print(fruit[0:-3]) 
# print(fruit[:len(fruit)-3]) 

print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])

pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index