import time

timeStamp = time.strftime('%H:%M:%S')
print(timeStamp, "\n", "Type of timeStamp is ", type(timeStamp))

if (int(time.strftime('%H')) >= 5 and int(time.strftime('%H')) <= 12):
  print("Good morning")
elif (int(time.strftime('%H')) > 12 and int(time.strftime('%H')) <= 18):
  print("Good afternoon")
elif (int(time.strftime('%H')) > 18 and int(time.strftime('%H')) <= 21):
  print("Good evening")
