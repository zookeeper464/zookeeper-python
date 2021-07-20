answer = input()
s = input()
lst = list(s)
n = len(s)
stack = []
for i in answer:
  stack.append(i)
  if i == s[-1] and stack[-n:] == lst:
    del stack[-n:]

if stack:
  print("".join(stack))
else:
  print('FRULA')
