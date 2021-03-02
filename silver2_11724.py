def DFS (i,visited,e_list):
  visited[i]=True
  for j in e_list[i]:
    if not visited[j]:
      DFS(j, visited, e_list)

N,M=map(int,input().split())
e_list=[[]]
visited=[True]
count=0
for i in range(N):
  e_list.append([])
  visited.append(False)
for i in range(M):
  a,b=map(int,input().split())
  e_list[a].append(b)
  e_list[b].append(a)

for i in range(1,N+1):
  if not visited[i]:
    DFS(i,visited,e_list)
    count+=1
    
print(count)
