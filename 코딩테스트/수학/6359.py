t = int(input())
answer = []
for _ in range(t):
  n = int(input())
  i = 1
  cnt = 0
  while i**2<=n:
    i += 1
    cnt += 1
  answer.append(cnt)

for i in answer:
  print(i)
