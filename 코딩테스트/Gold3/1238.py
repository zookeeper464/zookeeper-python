from heapq import heappop,heappush
import sys
inf = sys.maxsize

def check(num,dp,roads):
  q = [[0,num]]
  while q:
    now_val,now_node = heappop(q)

    for val, next_node in roads[now_node]:
      if dp[next_node]> val+now_val:
        dp[next_node] = val+now_val
        heappush(q,[dp[next_node],next_node])
  
  return dp

n,m,x = map(int,input().split())
come_roads = [[] for _ in range(n+1)]
go_roads = [[] for _ in range(n+1)]
for _ in range(m):
  a,b,t = map(int,input().split())
  come_roads[a].append([t,b])
  go_roads[b].append([t,a])

come_dp = [inf] * (n+1)
go_dp = [inf] * (n+1)
come_dp[x],go_dp[x] = 0,0
come_dp[0],go_dp[0] = 0,0

come_dp = check(x,come_dp,come_roads)
go_dp = check(x,go_dp,go_roads)

print(max([come_dp[i]+go_dp[i] for i in range(n+1)]))
