n = int(input())
lst = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x : (x[1],x[0]))

for i in lst:
  print(*i)
