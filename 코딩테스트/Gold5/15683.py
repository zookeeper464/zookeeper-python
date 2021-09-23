from copy import deepcopy
from collections import deque

n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [0,1,0,-1],[1,0,-1,0]

def move(r,c,look,board):
  nr,nc = r+dr[look],c+dc[look]
  if 0<=nr<n and 0<=nc<m and board[nr][nc]!=6:
    board[nr][nc] = -1
    move(nr,nc,look,board)
  return

cctv = [-1, [[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[3,0]], [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],[[0,1,2,3]]]

a = []
for r in range(n):
  for c in range(m):
    if 0 < board[r][c] and board[r][c] < 6:
      a.append((r,c,board[r][c]))

ans = 100
def dfs(a,here,board):
  global ans
  if here == len(a):
    cnt = 0
    for r in range(n):
      for c in range(m):
        if board[r][c] == 0:
          cnt += 1
    ans = min(ans, cnt)
    return

  r,c,val = a[here]
  for arrs in cctv[val]:
    new_board = deepcopy(board)
    for direction in arrs:
      move(r,c,direction,new_board)
    dfs(a,here+1,new_board)

dfs(a, 0, board)
print(ans)
