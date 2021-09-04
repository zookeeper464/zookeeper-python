n = int(input())
lst = list(map(int,input().split()))
answer = 0

def dfs (cnt, idx,visited,temp):
  global answer
  if cnt == n:
    answer = max(temp,answer)
    return
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      dfs(cnt+1,i,visited,temp+abs(lst[i]-lst[idx]))
      visited[i] = False
  pass

for i in range(n):
  visited = [False for _ in range(n)]
  visited[i] = True
  dfs(1,i,visited,0)

print(answer)
