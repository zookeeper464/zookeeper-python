# import heapq

# n,m = int(input()), int(input())
# lst = [[] for _ in range(n+1)]
# dp = [-1] * (n+1)

# for _ in range(m):
#   a,b,v = map(int,input().split())
#   lst[a].append([v,b])

# start,end = map(int,input().split())

# q = lst[start]
# heapq.heapify(q)
# while dp[end] == -1:
#   v,b = heapq.heappop(q)
#   if dp[b] == -1:
#     dp[b] = v
#     for vv,bb in lst[b]:
#       if dp[bb] == -1:
#         heapq.heappush(q,[vv+v,bb])

# print(dp[end])
############################################

import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
m = int(input())
s = [[] for _ in range(n+1)]
dp = [inf for _ in range(n+1)]

for i in range(m):
  a,b,w = map(int,input().split())
  s[a].append([b,w])
start,end = map(int,input().split())

def dijkstra(start):
  dp[start] = 0
  heap = []
  heapq.heappush(heap,[0,start])
  while heap:
    w, n = heapq.heappop(heap)
    if dp[n] < w:
      continue
    for n_n, wei in s[n]:
      n_w = w + wei
      if dp[n_n] > n_w:
        dp[n_n] = n_w
        heapq.heappush(heap, [n_w, n_n])

dijkstra(start)
print(dp[end])
