from heapq import heappop,heappush

n,m = map(int,input().split())
v_list = [[] for _ in range(n+1)]
topl = [0]*(n+1)
hq = []
answer = []

for _ in range(m):
  a,b = map(int,input().split())
  topl[b] += 1
  v_list[a].append(b)

for i in range(1,n+1):
  if topl[i] == 0:
    heappush(hq,i)

while hq:
  temp = heappop(hq)
  answer.append(temp)
  for i in v_list[temp]:
    topl[i] -= 1
    if topl[i] == 0:
      heappush(hq,i)

print(*answer)
