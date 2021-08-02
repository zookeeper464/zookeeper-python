from collections import deque

n,m,v = map(int,input().split())
lst = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)

for i in range(1,n+1):
  lst[i] = sorted(lst[i])

q = deque([v])
visit = [False] * (n+1)
visit[v] = True
bfs_lst = [v]
while q:
  temp = q.popleft()
  for i in lst[temp]:
    if not visit[i]:
      visit[i] = True
      q.append(i)
      bfs_lst.append(i)

dfs_lst = [v]
visit = [False] * (n+1)
visit[v] = True
def dfs (v):
  global dfs_lst, visit
  for i in lst[v]:
    if not visit[i]:
      visit[i] = True
      dfs_lst.append(i)
      dfs(i)

dfs(v)

for ans in dfs_lst:
  print(ans,end=' ')
print()
for ans in bfs_lst:
  print(ans,end=' ')
