n=int(input())
lst=[]
for i in range(n):
  a,b=map(int,input().split())
  b=(b-1)%4+1
  a=a%10
  temp=(a**b-1)%10+1
  lst.append(temp)

for i in lst:
  print(i)

