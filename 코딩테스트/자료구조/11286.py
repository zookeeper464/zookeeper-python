import heapq

n = int(input())
answer = []
lst = []

for _ in range(n):
  m = int(input())
  if m == 0:
    if lst != []:
      answer.append(heapq.heappop(lst)[1])
    else:
      answer.append(0)
  else:
    heapq.heappush(lst,(abs(m),m))
  
for ans in answer:
  print(ans)
