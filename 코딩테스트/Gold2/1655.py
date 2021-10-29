from heapq import heappop,heappush
import sys
inf = sys.maxsize

n = int(input())
large,small = [inf],[inf]
answer = []

for _ in range(n):
  num = int(input())
  if len(small)<=len(large):
    heappush(small,-num)
    if small[0]+large[0]<0:
      s = heappop(small)
      l = heappop(large)
      heappush(small,-l)
      heappush(large,-s)
  else:
    heappush(large,num)
    if small[0]+large[0]<0:
      s = heappop(small)
      l = heappop(large)
      heappush(small,-l)
      heappush(large,-s)

  answer.append(-small[0])
  
print(*answer,sep='\n')
