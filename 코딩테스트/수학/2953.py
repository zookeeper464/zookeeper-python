idx, n = 0, 0
for i in range(5):
  m = sum(list(map(int,input().split())))
  if m>n:
    idx = i+1
    n = m

print(idx, n)
