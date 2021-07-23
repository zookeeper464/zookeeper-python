t = int(input())
answer = []
for _ in range(t):
  s = input().split()
  temp = []
  for i in s:
    temp.append(i[::-1])
  answer.append(' '.join(temp))

for ans in answer:
  print(ans)
