a, b=map(int,input().split())
c=min(a,b)
for i in range(1,c+1):
  if a%i==0 and b%i==0:
    d=i

print(d)
print((a*b)//d)
