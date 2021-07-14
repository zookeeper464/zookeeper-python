n = int(input())

i = 0
while True:
  if 2**i >= n:
    i -= 1
    break
  i += 1

if n == 1 or n ==2:
  print(n)
else:
  print(2*(n-(2**i)))
