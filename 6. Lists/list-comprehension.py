
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
