n = int(input())
count = 0
while True:
  if n%5==0:
    count += n//5
    break
  count += 1
  n-=3
  if n<0:
    count = -1
    break

print(count)
  
