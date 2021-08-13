from collections import deque

n,m = map(int, input().split())
dr,dc = [1,-1,0,0],[0,0,1,-1]
visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
s = []

def move(i, j, dr, dc):
  c = 0
  while s[i + dr][j + dc] != "#" and s[i][j] != "O":
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

      if s[nbi][nbj] != "O":
        if s[nri][nrj] == "O":
          return d

        if nri == nbi and nrj == nbj:
          if rc > bc:
            nri -= dr[i]
            nrj -= dc[i]
          else:
            nbi -= dr[i]
            nbj -= dc[i]

        if not visit[nri][nrj][nbi][nbj]:
          visit[nri][nrj][nbi][nbj] = True
          q.append([nri, nrj, nbi, nbj, d + 1])
          
  return -1

for i in range(n):
  a = list(input())
  s.append(a)
  for j in range(m):
    if a[j] == "R":
      ri, rj = i, j
    if a[j] == "B":
      bi, bj = i, j

q = deque()
q.append([ri, rj, bi, bj, 1])
visit[ri][rj][bi][bj] = True
print(bfs(q))
