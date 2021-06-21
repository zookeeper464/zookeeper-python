import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start_cost,start, end):
  dist = [INF for _ in range(n+1)]
  dist[start] = 0
  q = [(start_cost,start)]

  while q:
    p = heapq.heappop(q)
    cur_cost, cur_node = p[0], p[1]
    for next_cost, next_node in graph[cur_node]:
      if dist[next_node] > cur_cost + next_cost:
        dist[next_node] = cur_cost + next_cost
        heapq.heappush(q, (dist[next_node],next_node))
  return dist[end]

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  start,end,cost = map(int,input().rstrip().rsplit())
  graph[start].append((cost,end))
start, end = map(int,input().rstrip().rsplit())

print(dijkstra(0,start,end))
