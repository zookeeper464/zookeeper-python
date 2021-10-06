from collections import deque

t = int(input())
answer = []

# 연결 그래프 탐색
def check(q):
  global ans

  while q:
    for num in (1,2):
      for _ in range(len(q)):
        node = q.popleft()

        for temp_node in list(dp[node]):
          if visited[temp_node] == 0:
            visited[temp_node] = 3 - num
            q.append(temp_node)
          elif visited[temp_node] == num:
            ans = 'NO'
            return

  return

for _ in range(t):
  v,e = map(int,input().split())
  dp = [set() for _ in range(v+1)]
  visited = [0] * (v+1)
  for _ in range(e):
    a,b = map(int,input().split())
    dp[a].add(b)
    dp[b].add(a)

  ans = 'YES'
  # 비연결 그래프 탐색
  for i in range(1,v+1):
    if visited[i] == 0:
      visited[i] = 1
      q = deque([i])
      check(q)
      if ans == 'NO':
        break
  
  answer.append(ans)

print(*answer, sep='\n')
