answer = []
for _ in range(3):
  n = sum(list(map(int,input().split())))
  if n == 0:
    answer.append("D")
  elif n == 1:
    answer.append("C")
  elif n==2:
    answer.append("B")
  elif n==3:
    answer.append("A")
  elif n==4:
    answer.append("E")

for i in answer:
  print(i)
