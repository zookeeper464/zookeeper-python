answer = input()
s = input()
lst = list(s)
n = len(lst)
stack = []

for i in answer:
  stack.append(i)
  if i == s[-1] and stack[-n:] == lst:
    del stack[-n:]

print(*stack if stack else 'FRULA', sep='')
