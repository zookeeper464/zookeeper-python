n = int(input())
lst = sorted([input().split() for _ in range(n)], key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in lst:
  print(i[0])
