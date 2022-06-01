from time import sleep
i = 10
while i <= 10:
  print(i)
  sleep(1)
  i = i - 1
  if i == 0:
    print("BUM BUM POOW!")
  if i < 0:
    break

''''
for count in range(10, -1, -1)
  print(count)
  sleep(0.5)
print("BUM! BUM! POOW!")
'''