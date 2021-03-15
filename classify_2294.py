n,m=map(int,input().split())
coin=[]
lst=[-1]*(m+1)
for i in range(n):
  a=int(input())
  coin.append(a)
  if a<=m:
    lst[a]=1

for i in range(1,m+1):
  for j in coin:
    if j<=i and lst[i-j]>0:
      if lst[i]>lst[i-j] or lst[i]==-1:
        lst[i]=lst[i-j]+1

print(lst[-1])
