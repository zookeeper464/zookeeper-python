import heapq

inf = 100000000
v,e = map(int, input().split())
k = int(input())
lst = [[] for _ in range(v)]
dp = [inf] * (v)
heap = []

def dijkstra(start):
  dp[start] = 0
  heapq.heappush(heap, [0, start])
  while heap:
    w, n = heapq.heappop(heap)
    for n_n, wei in lst[n]:
      n_w = wei + w
      if n_w < dp[n_n]:
        dp[n_n] = n_w
        heapq.heappush(heap, [n_w, n_n])

for i in range(e):
  u, v, w = map(int, sys.stdin.readline().split())
  lst[u-1].append([v-1, w])
dijkstra(k-1)

for i in dp:
  print(i if i != inf else "INF")
