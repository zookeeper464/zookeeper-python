m = int(input())
ball = 1
for _ in range(m):
  a,b = map(int,input().split())
  if ball == a:
    ball = b
  elif ball == b:
    ball = a

print(ball)
