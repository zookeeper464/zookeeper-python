import heapq

n = int(input())
lst = []
for _ in range(n):
  m = int(input())
  heapq.heappush(lst,m)

answer = 0
for _ in range(n-1):
  a = heapq.heappop(lst)
  b = heapq.heappop(lst)
  answer += a+b
  heapq.heappush(lst, a+b)

print(answer)
