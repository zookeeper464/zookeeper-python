lst = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for _ in range(n):
  x, y = map(int,input().split())
  for i in range(10):
    for j in range(10):
      if lst[x+i][y+j] == 0:
        lst[x+i][y+j] =1

answer = sum([sum(lst[i]) for i in range(100)])
print(answer)
