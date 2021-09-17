n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
check = [[False for _ in range(m)] for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
max_result = -1
def dfs(r,c,now,cnt):
  global max_result 
  if cnt == 4:
    max_result = max(max_result,now)
    return
	
  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]
    if 0<=nr<n and 0<=nc<m and not check[nr][nc]:
      check[nr][nc] = True
      dfs(nr,nc,now+lst[nr][nc],cnt+1)
      check[nr][nc] = False

def except_dfs(r,c):
  center = lst[r][c]
  wings = 4
  min_result = 100000
  
  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]
    if wings ==2:
      return 0

    if not(0<=nr<n and 0<=nc<m):
      wings -=1
      continue
    
    center += lst[nr][nc]

    if lst[nr][nc] < min_result:
      min_result = lst[nr][nc]
  
  if wings == 4:
      center -= min_result
  
  return center

for r in range(n):
  for c in range(m):
    check[r][c] = True
    dfs(r,c,lst[r][c], 1)
    check[r][c] = False
    temp = except_dfs(r,c)
    max_result = max(temp, max_result)

print(max_result)
