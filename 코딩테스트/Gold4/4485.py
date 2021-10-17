from heapq import heappop, heappush
import sys

inf = sys.maxsize
answer = []
dr,dc = [1,-1,0,0],[0,0,1,-1]

while True:
  n = int(input())
  if n == 0:
    break
  
  lst = [list(map(int,input().split())) for _ in range(n)]
  dp = [[inf for _ in range(n)] for _ in range(n)]
  dp[0][0] = lst[0][0]
  q = [[lst[0][0],0,0]]
  while q:
    num,r,c = heappop(q)
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<n:
        if lst[nr][nc]+num<dp[nr][nc]:
          dp[nr][nc] = lst[nr][nc]+num
          heappush(q,[dp[nr][nc],nr,nc])
  
  answer.append(dp[-1][-1])

for i in range(len(answer)):
  print(f'Problem {i+1}: {answer[i]}')
