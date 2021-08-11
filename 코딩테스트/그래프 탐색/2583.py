from collections import deque

m,n,k = map(int,input().split())
lst = [[0 for _ in range(n)] for _ in range(m)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
answer = []
num = 0

for _ in range(k):
  aa,bb,cc,dd = map(int,input().split())
  for r in range(bb,dd):
    for c in range(aa,cc):
      lst[r][c] = 1


for r in range(m):
  for c in range(n):
    if lst[r][c] == 0:
      num += 1
      lst[r][c] = 1
      cnt = 1
      q = deque([[r,c]])

      while q:
        tr,tc = q.popleft()
        for i in range(4):
          nr,nc = tr+dr[i], tc+dc[i]
          if 0<=nr<m and 0<=nc<n and lst[nr][nc] == 0:
            q.append([nr,nc])
            lst[nr][nc] = 1
            cnt += 1

      answer.append(cnt)

answer.sort()
print(num)
for ans in answer:
  print(ans, end=' ')
