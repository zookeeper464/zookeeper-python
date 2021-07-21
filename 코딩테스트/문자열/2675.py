n = int(input())
answer = []

for _ in range(n):
  m, s = input().split()
  m = int(m)
  temp = ''
  for i in s:
    temp += i*m
  answer.append(temp)

for ans in answer:
  print(ans)
