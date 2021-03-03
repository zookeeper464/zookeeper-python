import sys
sys.setrecursionlimit(10**6)

def BFS (lst,i,j):
  lst[i][j]=0
  dx=[-1,1,0]
  dy=[0,-1,1]
  for k in range(3):
    for l in range(3):
      if lst[i+dx[k]][j+dy[l]]==1:
        BFS(lst,i+dx[k],j+dy[l])   

answer=[]
while True:
  a,b=map(int,sys.stdin.readline().split())
  if [a,b]==[0,0]:
    break
  lst=[[0]*(a+2)]
  for i in range(b):
    ls=list(map(int,sys.stdin.readline().split()))
    lst.append([0]+ls+[0])
  lst.append([0]*(a+2))

  count=0
  for i in range(1,b+2):
    for j in range(1,a+2):
      if lst[i][j]==1:
        BFS(lst,i,j)
        count+=1
  answer.append(count)

for i in answer:
  print(i)
