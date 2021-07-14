from collections import deque

n = int(input())
q= deque()
answer = []

def command (s):
  if len(s.split()) == 1:
    if s[0] == "e":
      if q:
        return 0
      else:
        return 1
    
    elif s[0] == "s":
      return len(q)
    
    if not q:
      return -1

    if s[0] == "p":
      if s[4] =="f":
        num = q.popleft()
        return num
      else:
        num = q.pop()
        return num
    elif s[0] == "f":
      return q[0]
    else:
      return q[-1]
  
  else:
    if s[5] == 'b':
      num = s.split()[1]
      q.append(num)
      return "False"
    else:
      num = s.split()[1]
      q.appendleft(num)
      return "False"

for _ in range(n):
  s = input()
  temp = command(s)
  if temp != "False":
    answer.append(temp)

for ans in answer:
  print(ans)
