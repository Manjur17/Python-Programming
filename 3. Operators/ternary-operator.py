# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)


# Python program to demonstrate nested ternary operator/nested if-else
a, b = 10, 20

print("Both a and b are equal" if a == b else "a is greater than b"
      if a > b else "b is greater than a")

# To use print function in ternary operator be like:-
a = 5
b = 7

print(a, "is greater") if (a > b) else print(b, "is Greater")
