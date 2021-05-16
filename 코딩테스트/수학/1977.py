m = int(input())
n = int(input())
a = int(m**0.5)+1
b = int(n**0.5)
s, num = 0, a**2
for i in range(a,b+1):
  s += i**2

if num<=n:
  print(s)
  print(num)
else:
  print(-1)
