from collections import deque

n = int(input())
m = int(input())
lst = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)
visited = [False for _ in range(n+1)]
visited[1] = True
answer = 0

q = deque([1])
while q:
  x = q.popleft()
  for i in lst[x]:
    if not visited[i]:
      visited[i] = True
      q.append(i)
      answer += 1
print(answer)
