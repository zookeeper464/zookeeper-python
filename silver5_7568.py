N=int(input())
lst=[]
for i in range(N):
  a,b=map(int,input().split())
  lst.append([a,b])

for i in range(N):
  rank=1
  for j in range(N):
    if lst[i][0]<lst[j][0] and lst[i][1]<lst[j][1]:
      rank+=1
  print(rank, end=" ")
