import heapq

n,m = map(int,input().split())
lst = [0] * (n+1)
dp = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  dp[a].append(b)
  lst[b] += 1

temp_lst = []
for i in range(1,n+1):
  if lst[i] == 0:
    heapq.heappush(temp_lst,i)

while temp_lst:
  x = heapq.heappop(temp_lst)
  for i in dp[x]:
    lst[i] -= 1
    if lst[i] == 0:
      heapq.heappush(temp_lst,i)
  print(x, end=' ')
