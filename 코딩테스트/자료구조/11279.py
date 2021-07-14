import heapq

n = int(input())
lst,answer = [],[]
for _ in range(n):
  m = int(input())
  if m == 0:
    if lst:
      answer.append(-heapq.heappop(lst))
    else:
      answer.append(0)
  else:
    heapq.heappush(lst,-m)
  
for ans in answer:
  print(ans)
