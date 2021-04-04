import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
answer = []
for i in range(n):
  m = int(input())
  if m == 0:
    if h:
      temp = heapq.heappop(h)
      answer.append(temp[0] * ((-1)**temp[1]))
    else:
      answer.append(0)
  elif m > 0:
    heapq.heappush(h,(m,2))
  else:
    heapq.heappush(h,(abs(m),1))


for i in answer:
  print(i)
