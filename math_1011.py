n=int(input())
lst=[]

for i in range(n):
  x,y=map(int,input().split())
  n=y-x
  j=0
  while True:
    n-=(j+1)//2
    if n<=0:
      break
    j+=1
  lst.append(j)

for i in lst:
  print(i)
