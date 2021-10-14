from heapq import heappop,heappush,heapify

n = int(input())
hq = [int(input()) for _ in range(n)]
heapify(hq)
answer = 0

while len(hq)>1:
  a,b = heappop(hq),heappop(hq)
  heappush(hq,a+b)
  answer += a+b

print(answer)
