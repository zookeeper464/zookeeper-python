N,M=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
sol=[]

def solve(depth, N, M, j):
  if depth == M:
    print(' '.join(map(str, sol)))
    return
  overlap = 0
  for i in range(N):
    if overlap != lst[i] and i>=j:
      sol.append(lst[i])
      overlap = lst[i]
      solve(depth+1, N, M, i)
      sol.pop()

solve(0, N, M,-1)
