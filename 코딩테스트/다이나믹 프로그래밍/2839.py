n = int(input())
count = 0
while True:
  if n%5 == 0:
    break
  if n<0:
    count = -1
  n -= 3
  count += 1

if count < 0:
  print(count)
else:
  print(count + n//5)
