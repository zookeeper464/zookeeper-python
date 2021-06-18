from collections import deque

t = int(input())
dr,dc = [2,2,1,1,-1,-1,-2,-2],[1,-1,2,-2,2,-2,1,-1]
answer = []

for _ in range(t):
  n = int(input())
  lst = [[-1 for _ in range(n)] for _ in range(n)]
  sr,sc = map(int,input().split())
  er,ec = map(int,input().split())
  cnt = 0
  q = deque([[sr,sc]])
  lst[sr][sc] = 0
  if (sr,sc) == (er,ec):
    q = deque()
  while q:
    cnt += 1
    for _ in range(len(q)):
      tr,tc = q.popleft()
      if (tr,tc) == (er,ec):
        q = deque()
        cnt -= 1
        break
      for i in range(8):
        nr,nc = tr+dr[i],tc+dc[i]
        if 0<=nr<n and 0<=nc<n and lst[nr][nc] == -1:
          lst[nr][nc] = cnt
          q.append([nr,nc])
  answer.append(cnt)

for i in answer:
  print(i)
