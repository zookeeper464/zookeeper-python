from collections import deque
from heapq import heappop, heappush

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [-1,0,0,1],[0,-1,1,0]
shark = ''
for r in range(n):
  for c in range(n):
    if lst[r][c] == 9:
      lst[r][c] = 0
      shark = [r,c]
      break
answer = 0
size = 2
num = 0

q = deque([shark])
def move (q,size,num):
  global answer
  visited = [[False for _ in range(n)] for _ in range(n)]
  visited[q[0][0]][q[0][1]] = True
  cnt = 0
  hq = []

  while q:
    cnt += 1
    for _ in range(len(q)):
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<n and not visited[nr][nc] and lst[nr][nc]<=size:
          q.append([nr,nc])
          visited[nr][nc] = True

          if 0 < lst[nr][nc] < size:
            heappush(hq,[nr,nc])
    
    if hq:
      nr,nc = heappop(hq)
      lst[nr][nc] = 0
      num += 1
      answer += cnt

      if size == num:
        size += 1
        num = 0

      return deque([[nr,nc]]), size, num
  
  return None, size, num

while q:
  q,size,num = move(q,size,num)

print(answer)
