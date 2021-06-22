from collections import deque

n = int(input())
start,end = map(int,input().split())
lst = [[] for _ in range(n+1)]
dist = [n for _ in range(n+1)]
m = int(input())
for _ in range(m):
  x,y = map(int,input().split())
  lst[x].append(y)
  lst[y].append(x)

def bfs (start):
  q = deque([start])
  dist[start] = 0

  while q:
    t = q.popleft()
    for i in lst[t]:
      if dist[i] > dist[t]+1:
        dist[i] = dist[t]+1
        q.append(i)
  return dist[end]

print(bfs(start))
