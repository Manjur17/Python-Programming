
i = int(input("Enter the number: "))
print(i)

while (i <= 38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")



#  We can even use the else statement with the while loop. 
#  Essentially what the else statement does is that as soon as 
#  the while loop condition becomes False/ends, the interpreter comes out of the while loop and 
#  the else statement is executed.

count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else !!!")

# No do while loop in python
# We have to enumate it 
# do {
#  loop body;
# }while(condition);
