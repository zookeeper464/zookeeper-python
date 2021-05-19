a, b = 0,1
n = int(input())
for i in range(n%1500000):
  a, b = b, (a+b)%1000000
print(a)
