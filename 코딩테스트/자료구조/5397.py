from collections import deque

t = int(input())
answer = []

for _ in range(t):
  s = input()
  lst = []
  q = deque()

  for i in s:
    if i == "<":
      if lst:
        q.appendleft(lst.pop())
    elif i == ">":
      if q:
        lst.append(q.popleft())
    elif i == '-':
      if lst:
        lst.pop()
    
    else:
      lst.append(i)
  answer.append(''.join(lst+list(q)))

for ans in answer:
  print(ans)

