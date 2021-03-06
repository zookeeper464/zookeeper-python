n,m=map(int,input().split())
answer=0

def count(n,m):
  temp=0
  while n!=0:
    n=n//m
    temp+=n
  return temp
a=count(n,5)-count(m,5)-count(n-m,5)
b=count(n,2)-count(m,2)-count(n-m,2)
answer=min(a,b)
print(answer)
