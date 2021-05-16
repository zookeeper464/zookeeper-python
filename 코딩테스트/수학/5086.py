answer = []
while True:
  a, b = map(int,input().split())
  if (a,b) == (0,0):
    break
  if b%a == 0:
    answer.append("factor")
  elif a%b == 0:
    answer.append("multiple")
  else:
    answer.append("neither")

for i in answer:
  print(i)
