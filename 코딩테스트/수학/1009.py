n = int(input())
answer = []
for i in range(n):
  a, b = map(int,input().split())
  b %= 4
  answer.append((a**b)%10)

for i in answer:
  print(i)
