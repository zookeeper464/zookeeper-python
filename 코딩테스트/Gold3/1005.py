# def dfs(num,total_time):
#   global ans
#   total_time += built_time[num]

#   if before_built[num] == []:
#     ans = max(ans,total_time)
#     return

#   for number in before_built[num]:
#     dfs(number,total_time)

# t = int(input())
# answer = []

# for _ in range(t):
#   ans = 0
#   n,k = map(int,input().split())
#   built_time = [0]+list(map(int,input().split()))
#   before_built = [[] for _ in range(n+1)]
#   for _ in range(k):
#     x,y = map(int,input().split())
#     before_built[y].append(x)
  
#   last_built = int(input())
#   dfs(last_built,0)
#   answer.append(ans)

# print(*answer,sep='\n')
#################################### 시간초과 dp를 활용하지 않았다.
from collections import deque

t = int(input())
answer = []

for _ in range(t):
  n,k = map(int,input().split())
  times = [0] + list(map(int,input().split()))

  graph = [[] for _ in range(n + 1)]
  degree = [0]*(n+1)
  for _ in range(k):
    x,y = map(int,input().split())
    graph[x].append(y)
    degree[y] += 1

  win = int(input())

  q = deque()
  for i in range(1, n + 1):
    if  degree[i] == 0:
      q.append(i)
  
  dp = times[:]

  while q:
    now = q.popleft()
    if now == win:
      break

    dp.append(now)
    for i in graph[now]:
      dp[i] = max(dp[i], dp[now] + times[i])
      degree[i] -= 1
      
      if degree[i] == 0:
        q.append(i)
  
  answer.append(dp[win])

print(*answer,sep='\n')
