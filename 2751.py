import heapq
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
  heapq.heappush(lst,int(input()))

for i in range(n):
  print(heapq.heappop(lst))
