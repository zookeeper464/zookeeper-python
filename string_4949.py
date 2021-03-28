import sys
input = sys.stdin.readline
answer = []
while True:
  s = input().rstrip()
  if s == '.':
    break
  lst = []
  temp = True
  for i in s:
    if i == '(' or i == '[':
      lst.append(i)
    elif i == ')':
      if not lst or lst[-1] == '[':
        temp = False
        break
      elif lst[-1] == '(':
        lst.pop()
    elif i == ']':
      if not lst or lst[-1] == '(':
        temp = False
        break
      elif lst[-1] == '[':
        lst.pop()

  if temp and not lst:
    answer.append('yes')
  else:
    answer.append('no')

for i in answer:
  print(i)
