import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
answer = 0

def bfs():
  q = deque([(0, 0, 0)])
  visited[0][0][0] = 1

  while q:
    for _ in range(len(q)):
      r, c, wall = q.popleft()
      if r == n - 1 and c == m - 1:
        return visited[r][c][wall]

      for i in range(4):
        nr,nc = r+dr[i], c+dc[i]
        if 0 <= nr < n and 0 <= nc < m and visited[nr][nc][wall] == 0:
          if lst[nr][nc] == 0:
            q.append((nr, nc, wall))
            visited[nr][nc][wall] = visited[r][c][wall] + 1
                
          if wall == 0 and lst[nr][nc] == 1:
            q.append((nr, nc, 1))
            visited[nr][nc][1] = visited[r][c][wall] + 1

  return -1


print(bfs())
