n = int(input())
m = int(input())
c = 0
mi = m+1

lst = [True for _ in range(m+1)]
lst[0], lst[1] = False, False
for i in range(2, m+1):
  if lst[i]:
    j = 2
    while i*j<=m:
      lst[i*j] = False
      j += 1
    if i>=n:
      c += i
      mi = min(i,mi)
if c:
  print(c)
if mi == m+1:
  print(-1)
else:
  print(mi)
