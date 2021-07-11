lst = []
n = int(input())
for _ in range(n):
  m = int(input())
  if m == 0:
    lst.pop()
  else:
    lst.append(m)

print(sum(lst))
