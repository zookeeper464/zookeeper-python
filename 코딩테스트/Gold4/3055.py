from collections import deque

n,m = map(int,input().split())
lst = [list(input().rstrip()) for _ in range(n)]
water = deque()
dr,dc = [1,-1,0,0],[0,0,1,-1]

for r in range(n):
  for c in range(m):
    if lst[r][c] == 'S':
      beaver = deque([[r,c]])
    elif lst[r][c] == '*':
      water.append([r,c])
    elif lst[r][c] == 'D':
      D=[r,c]

def water_move (q):
  for _ in range(len(q)):
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<m and lst[nr][nc] in '.S':
        lst[nr][nc] = '*'
        q.append([nr,nc])


def beaver_move (q):
  for _ in range(len(q)):
    r,c = q.popleft()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<m:
        if lst[nr][nc] == '.':
          lst[nr][nc] = 'S'
          q.append([nr,nc])
        elif lst[nr][nc] == 'D':
          lst[nr][nc] = 'S'
          return
seconds = 0
while beaver:
  water_move(water)
  beaver_move(beaver)
  seconds += 1
  if lst[D[0]][D[1]] == 'S':
    break

if lst[D[0]][D[1]] == 'S':
  print(seconds)
else:
  print('KAKTUS')
