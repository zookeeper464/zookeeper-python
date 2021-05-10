n = int(input())
answer = []
for i in range(n):
  lst = list(map(int,input().split()))
  m = lst[0]
  lst = lst[1:]
  ev = sum(lst)/m
  count = 0
  for j in lst:
    if ev > j:
      count += 1
  answer.append(count/m*100)

for i in answer:
  print("{:.3f}%".format(i))
