from heapq import heappop, heappush
import sys
INF = sys.maxsize

n,e = map(int,input().split())
v_list = [[] for _ in range(n+1)]

for _ in range(e):
  a,b,c = map(int,input().split())
  heappush(v_list[a],[c,b])
  heappush(v_list[b],[c,a])

v1,v2 = map(int,input().split())
v1_dist = [INF]*(n+1)
v2_dist = [INF]*(n+1)
v1_dist[v1],v2_dist[v2] = 0,0

def check_dist (lst,node):
  q = []
  heappush(q,[lst[node],node])

  while q:
    val, now_node = heappop(q)

    if lst[now_node] < val:
      continue
    
    for new_val, new_node in v_list[now_node]:
      temp = val + new_val
      if temp < lst[new_node]:
        lst[new_node] = temp
        heappush(q, [temp, new_node])



check_dist(v1_dist,v1)
check_dist(v2_dist,v2)

answer = min(v1_dist[1]+v2_dist[n],v1_dist[n]+v2_dist[1])+v1_dist[v2]
if answer < INF:
  print(answer)
else:
  print(-1)
