n = int(input())
lst = []
for _ in range(n):
  m = int(input())
  if m == 0 and lst:
    lst.pop()
  elif m != 0:
    lst.append(m)

print(sum(lst))
