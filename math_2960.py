n,k=map(int,input().split())
visited=[False]*(n+1)
answer=0
for i in range(2,n+1):
  if not visited[i]:
    for j in range(i*2,n+1,i):
      if not visited[j]:
        visited[j]=True
        answer+=1
        if answer==k:
          break
    else:
      continue
    break

print(j)
