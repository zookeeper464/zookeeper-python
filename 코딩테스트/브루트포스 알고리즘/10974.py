n = int(input())
lst = []

def dfs (cnt,visited):
  if cnt == n:
    print(*lst)
    return 
  for i in range(1,n+1):
    if not visited[i]:
      visited[i] = True
      lst.append(i)
      dfs(cnt+1,visited)
      visited[i] = False
      lst.pop()

dfs(0,[False for _ in range(n+1)])
