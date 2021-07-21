answer = 1
for _ in range(3):
  answer *= int(input())
answer = str(answer)

lst = [0] * 10
for i in answer:
  lst[int(i)] += 1

for i in lst:
  print(i)
