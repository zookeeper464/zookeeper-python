n,m = map(int,input().split())
topl = [[0,i] for i in range(1,n+1)]
for _ in range(m):
  a, b = map(int,input().split())
  topl[b-1][0] = max(topl[a-1][0]+1,topl[b-1][0]+1)

topl.sort()
for i,x in topl:
  print(x, end=" ")
