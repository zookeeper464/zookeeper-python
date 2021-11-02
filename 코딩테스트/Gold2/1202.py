import heapq

n,k = map(int,input().split())
answer = 0
lst = []

for _ in range(n):
  m,v = map(int,input().split())
  lst.append([m,v])

for _ in range(k):
  c = int(input())
  lst.append([c,-1])

lst.sort(key = lambda x:(x[0],-x[1]))

hq = []
for i in range(n+k):
  if lst[i][1] != -1:
    heapq.heappush(hq,-lst[i][1])
  else:
    if hq:
      answer -= heapq.heappop(hq)

print(answer)
