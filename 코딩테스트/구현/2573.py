import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [1,0,-1,0],[0,1,0,-1]
s = True

def bfs (i,j):
  global visited, lst, lst1
  visited[i][j] = True
  cnt = sum([lst[i+dx[k]][j+dy[k]]==0 for k in range(4)])
  lst1[i][j] = max(lst[i][j] - cnt,0)
  for k in range(4):
    if lst[i+dx[k]][j+dy[k]] !=0 and not visited[i+dx[k]][j+dy[k]]:
      bfs(i+dx[k],j+dy[k])

answer = 0
while True:
  visited = [[False for _ in range(m)] for _ in range(n)]
  lst1 = [lst[z][:] for z in range(n)]
  temp =0
  for i in range(1,n-1):
    for j in range(1,m-1):
      if lst[i][j] != 0 and not visited[i][j]:
          if temp == 0:
            bfs(i,j)
            temp += 1
          else:
            s = False
            break
    lst = [lst1[z][:] for z in range(n)]
    if not s:
      break  
  if not s:
    break
  if temp == 0:
    break
  answer += 1
  
if s:
  print(0)
else:
  print(answer)
