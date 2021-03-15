n,k=map(int,input().split())
result=[0]*(k+1)
result[0]=1
for i in range(n):
  a=int(input())
  for i in range(k+1-a):
    if result[i]!=0:
      result[a+i]+=result[i]


print(result[k])
