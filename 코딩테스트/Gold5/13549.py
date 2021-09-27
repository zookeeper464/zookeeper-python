from collections import deque

dist = [-1] * 100001

n,k = map(int, input().split())
q = deque([n])
dist[n] = 0

while q:
  now = q.popleft()
  temp = dist[now]
  if now*2<100001 and dist[now*2] == -1:
    q.appendleft(now*2)
    dist[now*2] = temp
  if now+1<100001 and dist[now+1] == -1:
    q.append(now+1)
    dist[now+1] = temp+1
  if now - 1 >= 0 and dist[now-1] == -1:
    q.append(now-1)
    dist[now-1] = temp+1

print(dist[k])
