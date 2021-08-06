answer = []

def check (lst):
  global mat, a,b

  dr,dc = [0,1,0,-1,1,1,-1,-1],[1,0,-1,0,1,-1,1,-1]
  while lst:
    r,c = lst.pop()
    for i in range(8):
      nr,nc = r+dr[i], c+dc[i]
      if 0<=nr<b and 0<=nc<a and mat[nr][nc] == 1:
        mat[nr][nc] = 0
        lst.append([nr,nc])

while True:
  a,b = map(int,input().split())
  if (a,b) == (0,0):
    break
  mat = [list(map(int,input().split())) for _ in range(b)]
  ans = 0
  for c in range(a):
    for r in range(b):
      if mat[r][c] == 1:
        mat[r][c] = 0
        lst = [[r,c]]
        check(lst)
        ans += 1
  answer.append(ans)

for ans in answer:
  print(ans)
