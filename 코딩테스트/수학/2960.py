n, k = map(int,input().split())
lst = [True for _ in range(n+1)]
lst[0],lst[1] = False, False
count = 0
s = False
for i in range(2,n):
  if lst:
    j = 1
    while i*j<=n:
      lst[i*j] = False
      j+= 1
      count += 1
      if count == k:
        s = True
        break
  if s:
    break

print(i*j)
