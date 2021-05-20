n = int(input())
answer = []

def check (a):
  global answer
  if a > 0:
    answer.append("advertise")
  elif a == 0:
    answer.append("does not matter")
  else:
    answer.append("do not advertise")

for i in range(n):
  r,e,c = map(int,input().split())
  check(e-c-r)

for i in answer:
  print(i)
