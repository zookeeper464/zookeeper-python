n,v = map(int,input().split())
lst = [[] for _ in range(n+1)]
for _ in range(v):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)

visited = [False for _ in range(n+1)]

cnt = 0
for i in range(1,n+1):
  if not visited[i]:
    visited[i] = True
    q = [i]
    cnt += 1
    while q:
      temp = q.pop()
      for j in lst[temp]:
        if not visited[j]:
          visited[j] = True
          q.append(j)

print(cnt)
