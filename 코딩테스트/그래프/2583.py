from collections import deque

m, n, k = map(int, input().split())
dp = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
  a,b,c,d = map(int,input().split())
  for i in range(a,c):
    for j in range(b,d):
      dp[i][j] = 1

dr,dc = [0,1,0,-1],[1,0,-1,0]

answer = 0
answers = []
for y in range(n):
  for x in range(m):
    if dp[y][x] == 0:
      answer += 1
      cnt = 1
      dp[y][x] = 1
      q = deque([[y,x]])

      while q:
        for _ in range(len(q)):
          r,c = q.popleft()
          for i in range(4):
            nr,nc = r+dr[i],c+dc[i]
            if 0<=nr<n and 0<=nc<m and dp[nr][nc] == 0:
              dp[nr][nc] = 1 
              q.append([nr,nc])
              cnt += 1
              
      answers.append(cnt)

answers.sort()

print(answer)
for i in answers:
  print(i, end=" ")
