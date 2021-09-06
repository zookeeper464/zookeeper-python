n = int(input())
lst = input().split()
mx,mi = 0, 10**(n+1)
s_max,s_min = '',''

def dfs (idx,cnt,temp,visited):
  global mx,mi,s_max,s_min
  if cnt == n:
    t = int(temp)
    if mx < t:
      mx=t
      s_max = temp
    if mi > t:
      mi=t
      s_min = temp
    return
  
  for i in range(10):
    if not visited[i]:
      if lst[cnt] == '<' and idx<i:
        visited[i] = True
        dfs(i,cnt+1,temp+str(i),visited)
        visited[i] = False
      elif lst[cnt] == '>' and idx>i:
        visited[i] = True
        dfs(i,cnt+1,temp+str(i),visited)
        visited[i] = False

visited = [False for _ in range(10)]
for i in range(10):
  visited[i] = True
  dfs(i,0,f'{i}',visited)
  visited[i] = False

print(s_max)
print(s_min)
