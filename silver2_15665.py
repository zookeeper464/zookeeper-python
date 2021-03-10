N,M=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
sol=[]

def solve(depth, N, M):
  if depth == M:
    print(' '.join(map(str, sol)))
    return
  overlap = 0
  for i in range(N):
    if overlap != lst[i]:
      sol.append(lst[i])
      overlap = lst[i]
      solve(depth+1, N, M)
      sol.pop()

solve(0, N, M)
