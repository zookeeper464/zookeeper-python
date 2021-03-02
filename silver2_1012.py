def checker(lst,a,b):
  lst[a][b]=False
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  for i in range(4):
    if lst[a+dx[i]][b+dy[i]]:
      checker(lst,a+dx[i],b+dy[i])


T=int(input())
answer=[]
for i in range(T):
  M,N,K=map(int,input().split())

  lst=[]
  for j in range(N+2):
    lst.append([False]*(M+2))

  li=[]
  for j in range(K):
    b,a=map(int,input().split())
    lst[a+1][b+1]= True
    li.append([a+1,b+1])
  
  count=0
  for j in li:
    if lst[j[0]][j[1]]:
      count+=1
      checker(lst,j[0],j[1])
  answer.append(count)
for i in answer:
  print(i)
