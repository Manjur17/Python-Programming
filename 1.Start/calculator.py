
z = input("Enter Your Choice\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Floor division\n6.Exponential\n")
a = input("enter the first number: ")
b = input("enter the second number: ")
a = int(a)
b = int(b)
if z == '1':
    addition = a + b
    print("Addititon is:", addition)
elif z == '2':
    subtraction = a - b
    print("Subtraction is:", subtraction)
elif z == '3':
    multiplication = a * b
    print("Multiplication is:", multiplication)
elif z == '4':
    division = a/b
    print("Division is:", division)
elif z == '5':
    division = a//b
    print("Division is:", division)
elif z == '6':
    exponential = a**b
    print("Division is:", exponential)
else:
    print("Enter a valid input")
