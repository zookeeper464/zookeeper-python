from sys import stdin

def input():
  return stdin.readline().rstrip('\n')

def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
answer = []
for _ in range(t):
  m, n, x, y = [int(x) for x in input().split(" ")]
  while (x<=m*n):
    if (x-y)%n==0:
      answer.append(x)
      break
    x += m
  if (x>m*n):
    answer.append(-1)

print(*answer,sep='\n')
