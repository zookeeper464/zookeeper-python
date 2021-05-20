answer = []

while True:
  a,b = map(int,input().split())
  if (a,b) == (0,0):
    break
  if a>b:
    answer.append("Yes")
  else:
    answer.append("No")

for i in answer:
  print(i)
