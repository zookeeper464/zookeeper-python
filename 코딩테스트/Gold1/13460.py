from collections import deque

def move(i, j, dr, dc):
  c = 0
  while lst[i + dr][j + dc] != "#" and lst[i][j] != "O":
    i += dr
    j += dc
    c += 1
  return i, j, c

def bfs(q):
  while q:
    ri, rj, bi, bj, d = q.popleft()
    if d > 10:
      break

    for i in range(4):
      nri, nrj, rc = move(ri, rj, dr[i], dc[i])
      nbi, nbj, bc = move(bi, bj, dr[i], dc[i])

      if lst[nbi][nbj] == "O":
        continue

      if lst[nri][nrj] == "O":
        return d

      if nri == nbi and nrj == nbj:
        if rc > bc:
          nri -= dr[i]
          nrj -= dc[i]
        else:
          nbi -= dr[i]
          nbj -= dc[i]

      if not visited[nri][nrj][nbi][nbj]:
        visited[nri][nrj][nbi][nbj] = True
        q.append([nri, nrj, nbi, nbj, d + 1])
          
  return -1

n,m = map(int, input().split())
dr,dc = [1,-1,0,0],[0,0,1,-1]
visited = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
lst = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
  for j in range(m):
    if lst[i][j] == "R":
      ri, rj = i, j
    if lst[i][j] == "B":
      bi, bj = i, j

q = deque([[ri, rj, bi, bj, 1]])
visited[ri][rj][bi][bj] = True
print(bfs(q))
