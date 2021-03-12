from math import gcd

k=int(input())
lst=[]
for i in range(k):
  M,N,X,Y=map(int,input().split())
  c=gcd(M,N)
  if abs(X-Y)%c!=0:
    lst.append(-1)
  else:
    a=c-X%c
    m,n,x,y=M//c,N//c,(X+a)//c,(Y+a)//c
    for i in range(1,m):
      if (n*i)%m==1:
        break
    for j in range(1,n):
      if (m*j)%n==1:
        break
    answer=((n*i*x+m*j*y)%(m*n))*c-a
    lst.append(answer)

for i in lst:
  print(i)
