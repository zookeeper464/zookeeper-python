n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
answer = 100000000

def dfs (cnt,idx,visited,start,temp):
  global answer
  if temp >= answer:
    return

  if cnt == n and lst[idx][start]>0:
    answer = min(answer,temp+lst[idx][start])
    return
  
  for i in range(n):
    if lst[idx][i] > 0 and not visited[i]:
      visited[i] = True
      dfs(cnt+1,i,visited,start,temp+lst[idx][i])
      visited[i] = False

for i in range(n):
  visited = [False for _ in range(n)]
  visited[i] = True
  dfs(1,i,visited,i,0)
  visited[i] = False

print(answer)
