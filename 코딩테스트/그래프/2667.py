from collections import deque

n = int(input())
lst = [list(input()) for _ in range(n)]
dr,dc = [1,0,-1,0],[0,1,0,-1]
answer = 0

temp = []
for r in range(n):
  for c in range(n):
    if lst[r][c] == "1":
      q = deque([[r,c]])
      lst[r][c] = "0"
      cnt = 1
      while q:
        r, c = q.popleft()
        for i in range(4):
          nr, nc = r+dr[i],c+dc[i]
          if 0<=nr<n and 0<=nc<n and lst[nr][nc]=="1":
            q.append([nr,nc])
            lst[nr][nc] = "0"
            cnt += 1
      answer += 1
      temp.append(cnt)
print(answer)
for i in temp:
  print(i)
