from heapq import heappop, heappush
import sys
INF = sys.maxsize

n,m = int(input()), int(input())
dp = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
  dp[i][i] = 0

for _ in range(m):
  a,b,c = map(int,input().split())
  dp[a][b] = min(dp[a][b],c)

def check(num):
  lst = []
  for idx,v in enumerate(dp[num]):
    heappush(lst,(v,idx))
  
  while lst:
    val,idx = heappop(lst)
    for i, v in enumerate(dp[idx]):
      if dp[num][i] > val+v:
        heappush(lst,(v+val,i))
        dp[num][i] = val+v
     
for i in range(1,n+1):
  check(i)
  for j in range(1,n+1):
    if dp[i][j] == INF:
      print(0, end=' ')
    else:
      print(dp[i][j], end=' ')
  print()
