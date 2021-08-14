from collections import deque
import heapq

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]

shark = False
for i in range(n):
  for j in range(n):
    if lst[i][j] == 9:
      lst[i][j] = 0
      shark = [i,j]
      break
  if shark:
    break

answer = 0
size = 2
num = 0

def bfs (shark, size, num):
  global lst, answer
  q = deque([shark])
  cnt = 0
  eat = []
  visited = [[False]*n for _ in range(n)]

  while q:
    cnt += 1
    for _ in range(len(q)):
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<n and lst[nr][nc]<=size and not visited[nr][nc]:
          visited[nr][nc] = True
          q.append([nr,nc])
          if 0<lst[nr][nc] < size:
            heapq.heappush(eat,[nr,nc])
            
    if eat:
      answer += cnt
      r, c = heapq.heappop(eat)
      lst[r][c] = 0
      num += 1
      if num == size:
        num = 0
        size += 1
      return [r,c], size, num

  return shark, -1, num

while size>0:
  shark, size, num = bfs(shark,size,num)

print(answer)
