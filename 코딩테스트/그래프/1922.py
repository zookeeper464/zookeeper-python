import heapq

n = int(input())
m = int(input())
lst = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
  a,b,c = map(int,input().split())
  lst[a].append([c,b])
  lst[b].append([c,a])

q = lst[1][:]
heapq.heapify(q)
answer = 0
cnt = 1
visited[1] = True
while q and cnt != n:
  val, idx = heapq.heappop(q)
  if not visited[idx]:
    answer += val
    visited[idx] = True
    cnt += 1
    for i in lst[idx]:
      heapq.heappush(q,i)
  
print(answer)
