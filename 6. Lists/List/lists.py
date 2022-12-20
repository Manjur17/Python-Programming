marks = [3, 5, 6, "Harry", True, 6, 7, 2, 32, 345, 23]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index


# Check whether an item in present in the list?
if "6" in marks:
    print("Yes")
else:
    print("No")

# Same thing applies for strings as well!
if "Ha" in "Harry":
    print("Yes")
else:
    print("No")

# Range of Index
# listName[start : end : jumpIndex]
print(marks)
print(marks[:])
print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

#jumpIndex -> step 
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])


