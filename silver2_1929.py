M,N=map(int,input().split())
from math import sqrt
for i in range(M,N+1):
  count=0
  for j in range(2,int(sqrt(i))+1):
    if i%j==0:
      count=1
      break
  if count==0 and i>1:
    print(i)
