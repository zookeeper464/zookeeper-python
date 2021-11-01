n = int(input())
a,b = 0,1
for _ in range(n%1500000):
  a,b = b,(a+b)%1000000

print(a)
