R,C = map(int,input().split())
mat = [list(input().rstrip()) for _ in range(R)]
answer = 0

def dfs (r,c):
  global s, answer
  if c == C-1:
    answer += 1
    s = True
    mat[r][c] = 'x'
    return

  for k in range(-1,2):
    if s:
      mat[r][c] = 'x'
      return

    if 0<=r+k<R and c<C-1 and mat[r+k][c+1] == '.':
      dfs(r+k,c+1)

  mat[r][c] = 'x'

  return


for i in range(R):
  if mat[i][0] == '.':
    s = False
    dfs(i,0)

print(answer)
