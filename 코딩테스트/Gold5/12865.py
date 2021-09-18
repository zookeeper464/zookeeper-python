n,k = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
answer = 0

def dfs (wei,idx,temp):
  global answer
  s = 0
  for i in range(idx+1,n):
    if wei+lst[i][0]>k:
      s = 1
    else:
      dfs(wei+lst[i][0],i,temp+lst[i][1])
  if s: 
    answer = max(answer,temp)

dfs(0,-1,0)
print(answer)
