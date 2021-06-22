from collections import deque
import heapq

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
  for j in range(n):
    if lst[i][j] == 9:
      shark = [i,j]
      lst[i][j] = 0
      break
size,answer = 2,0
dr,dc = [-1,0,0,1],[0,-1,1,0]
num = 0

def bfs (shark,size,num):
  global lst, answer
  check = []
  visited = [[False for _ in range(n)] for _ in range(n)]
  q = deque([shark])
  cnt = 0
  while q:
    cnt += 1
    for _ in range(len(q)):
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<n and lst[nr][nc]<=size:
          if 0<lst[nr][nc]<size:
            heapq.heappush(check,[nr,nc])

          if not visited[nr][nc]:
            visited[nr][nc] = True
            q.append([nr,nc])
    if check:
      nr,nc = heapq.heappop(check)
      shark = [nr,nc]
      lst[nr][nc] = 0
      num += 1
      answer += cnt
      if num == size:
        size,num = size+1,0
      return (shark,size,num)

  return (shark,-1,num)

while size>0:
  shark,size,num = bfs(shark,size,num)

print(answer)
