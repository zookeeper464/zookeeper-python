s = set(range(1,31))
for _ in range(28):
  n = int(input())
  s = s - set([n])

lst = list(s)
lst.sort()
for i in lst:
  print(i)
