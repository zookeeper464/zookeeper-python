temp = 1 
for i in range(3):
  temp *= int(input())

s = str(temp)
answer = [0 for i in range(10)]
for i in s:
  answer[int(i)] += 1

for i in answer:
  print(i)
