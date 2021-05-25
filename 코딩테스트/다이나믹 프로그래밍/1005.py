from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    time = [0]
    temp = list(map(int, input().split()))
    for i in temp:
        time.append(i)
    graph = [[] for i in range(n + 1)]
    indegree = [0] * (n + 1)

    queue = deque()

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    win = int(input())

    for i in range(1, n + 1):
        if  indegree[i] == 0:
            queue.append(i)
    
    result = deepcopy(time)

    while queue:
        now = queue.popleft()
        if now == win:
            break
        result.append(now)
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    print(result[win])
    
    
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write

t = int(input())

def dfs (v):
  if not elst[v]:
    return vlst[v]
  if dp[v] == 0:
    return vlst[v]+max([dfs(i) for i in elst[v]])
  return dp[v]

answer = []
for _ in range(t):
  v, e = map(int,input().split())
  vlst = [0]+list(map(int,input().split()))
  elst = [[] for _ in range(v+1)]#준비가 필요한 건물
  dp = [0 for _ in range(v+1)]
  for i in range(e):
    a, b = map(int,input().split())
    elst[b].append(a)
  end = int(input())
  # test마다 필요한 변수 처리
  answer.append(dfs(end))

for i in answer:
  print(str(i)+"\n")
"""
