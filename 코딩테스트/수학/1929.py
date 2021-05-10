n,m= map(int,input().split())

plst = [True for i in range(m+1)]
plst[0],plst[1] = False, False
for i in range(2,m+1):
  if plst[i]:
    j = 2
    while i*j<m+1:
      plst[i*j] = False
      j += 1

for i in range(n,m+1):
  if plst[i]:
    print(i)
