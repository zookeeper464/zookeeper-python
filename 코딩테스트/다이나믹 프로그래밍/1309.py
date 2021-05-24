n=int(input())
a,b=1,2
for i in range(n-1):
  a,b=a+b,2*a+b

print((a+b)%9901)
