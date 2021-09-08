n = int(input())
lst = sorted([list(map(int,input().split())) for _ in range(n)])

for i in lst:
  print(*i)
