answer = []
while True:
  a, b = map(int,input().split())
  if (a,b)==(0,0):
    break
  answer.append(a+b)
