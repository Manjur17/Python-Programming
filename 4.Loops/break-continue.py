
for i in range(12):
  if(i == 10):
    print("Skip this iteration")
    continue
  print("5 X", i, "=", 5 * i)


# Emulate do-while loop
i = 0
while True:
  print(i)
  i = i + 1
  if (i % 100 == 0):
    break
