n,m = map(int,input().split())
before = []
for _ in range(n):
  before.append(list(map(int,list(input()))))
after = []
for _ in range(n):
  after.append(list(map(int,list(input()))))

cnt = 0
for r in range(1,n-1):
  for c in range(1,m-1):
    if before[r-1][c-1] == after[r-1][c-1]:
      pass
    else:
      for i in range(-1,2):
        for j in range(-1,2):
          before[r+i][c+j] = (before[r+i][c+j]+1)%2
      cnt += 1

if before == after:
  print(cnt)
else:
  print(-1)
