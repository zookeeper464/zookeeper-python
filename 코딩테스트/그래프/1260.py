from collections import deque

n,m,v = map(int,input().split())
lst = [[] for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)

for i in range(1,n+1):
  if len(lst[i])>1:
    lst[i].sort()

answer1 = []
def dfs (v):
  global answer1,visited
  answer1.append(v)
  if len(answer1) == n:
    return 0
  for i in lst[v]:
    if not visited[i]:
      visited[i] = True
      dfs(i)

visited = [False for _ in range(n+1)]
visited[v] = True
dfs(v)

visited = [False for _ in range(n+1)]
visited[v] = True
q = deque([v])
answer2 = [v]
while True:
  if len(answer2) == n or not q:
    break
  l = len(q)
  for i in range(l):
    temp = q.popleft()
    for i in lst[temp]:
      if not visited[i]:
        visited[i] = True
        q.append(i)
        answer2.append(i)

print(" ".join(list(map(str,answer1))))
print(" ".join(list(map(str,answer2))))
