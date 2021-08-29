t = int(input())
answer = []
for _ in range(t):
  n,m = map(int,input().split())
  for _ in range(m):
    input()
  answer.append(n-1)

for ans in answer:
  print(ans)
