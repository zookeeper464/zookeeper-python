N, M, v =map(int, input().split())
v_list=[[]]
visited=[False]
for i in range(N):
  v_list.append([])
  visited.append(False)
e_list=[]
for i in range(M):
  a,b=map(int,input().split())
  e_list.append([a,b])
  v_list[a].append(b)
  v_list[b].append(a)
for i in v_list:
  i.sort()


def dfs (v_list,v,visited):
  visited[v]=True
  print(v, end=" ")
  for i in v_list[v]:
    if not visited[i]:
      dfs(v_list,i, visited)

def bfs (v_list,v,visited):
  que=[v]
  visited[v]=True
  while True:
    for i in v_list[que[0]]:
      if not visited[i]:
        que.append(i)
        visited[i]=True

    print(que[0], end=" ")
    que=que[1:]
    if que==[]:
      break

dfs(v_list,v,visited)
print()
visited=[False]
for i in range(N):
  visited.append(False)   
bfs(v_list,v,visited)
