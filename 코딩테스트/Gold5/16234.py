from collections import deque

N,L,R = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
dr,dc = [0,1,0,-1],[1,0,-1,0]
answer = 0

def check(q,visited):
  temp_lst = []
  temp = 0
  while q:
    r,c = q.popleft()
    temp_lst.append([r,c])
    temp += lst[r][c]
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and L<=abs(lst[r][c]-lst[nr][nc])<=R:
        q.append([nr,nc])
        visited[nr][nc] = True
  
  temp //= len(temp_lst)
  for i in temp_lst:
    y,x = i
    lst[y][x] = temp

while True:
  s=0
  visited = [[False for _ in range(N)] for _ in range(N)]
  for r in range(N):
    for c in range(N):
      if not visited[r][c]:
        for i in range(2):
          nr,nc = r+dr[i],c+dc[i]
          if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and L<=abs(lst[r][c]-lst[nr][nc])<=R:
            visited[nr][nc] = True
            q = deque([[nr,nc]])
            check(q,visited)
            s=1
  answer += s
  if s == 0:
    break

print(answer)
