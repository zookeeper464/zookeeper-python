lst = [list(map(int,input().split())) for _ in range(9)]
row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
box = [[False] * 10 for _ in range(9)]
zeros = []
for r in range(9):
  for c in range(9):
    if lst[r][c] == 0: zeros.append([r,c])
    else:
      row[r][lst[r][c]] = True
      col[c][lst[r][c]] = True
      box[3*(r//3)+c//3][lst[r][c]] = True

num = len(zeros)

def dfs (cnt):
  if cnt == num:
    for i in lst:
      print(*i, sep=' ')
    exit(0)
  
  r,c = zeros[cnt]
  for i in range(1,10):
    if not row[r][i] and not col[c][i] and not box[3*(r//3)+c//3][i]:
      lst[r][c] = i
      row[r][i] = col[c][i] = box[3*(r//3)+c//3][i] = True
      dfs(cnt+1)
      
      lst[r][c] = 0
      row[r][i] = col[c][i] = box[3*(r//3)+c//3][i] = False

dfs(0)

