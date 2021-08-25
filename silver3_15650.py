n,m = map(int,input().split())

def dfs (num,depth,answer):
  if depth == m:
    print(answer)
  for j in range(num+1,n+1):
    dfs(j,depth+1,answer+f' {j}')

for i in range(1,n+1):
  dfs(i,1,str(i))
