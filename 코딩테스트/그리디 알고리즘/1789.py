s = int(input())

if s<100:
  n = 0
else:
  n = int(s**0.5)
  s -= n*(n+1)//2

while  n+1<=s:
  n += 1
  s -= n

print(n)
