lst = []
m = 0
for _ in range(5):
  lst.append(list(input()))
  m = max(m,len(lst[-1]))

for c in range(m):
  for r in range(5):
    if len(lst[r]) > c:
      print(lst[r][c],end='')
