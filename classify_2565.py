n=int(input())
lst=[]
lstb=[]
lstnum=[0]*n

for i in range(n):
  a,b=map(int,input().split())
  lst.append([a,b])

lst.sort()
for i in range(n):
  lstb.append(lst[i][1])

for i in range(n):
  for j in range(i):
    if lstb[i]>=lstb[j] and lstnum[i]<=lstnum[j]:
      lstnum[i]=lstnum[j]+1
  if lstnum[i]==0:
    lstnum[i]=1

print(n-max(lstnum))
