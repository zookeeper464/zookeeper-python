N,M=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
visited=[False]*N
sol=[]

def solve(depth, N, M, j):
  if depth == M:
    print(' '.join(map(str, sol)))
    return
  overlap = 0
  for i in range(N):
    if not visited[i] and overlap != lst[i] and i>j:
      visited[i] = True
      sol.append(lst[i])
      overlap = lst[i]
      solve(depth+1, N, M, i)
      visited[i] = False
      sol.pop()

solve(0, N, M,-1)
