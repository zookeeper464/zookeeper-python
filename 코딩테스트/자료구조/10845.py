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
      num = q.popleft()
      return num
    elif s[0] == "f":
      return q[0]
    else:
      return q[-1]
  
  else:
    num = s.split()[1]
    q.append(num)
    return "False"

for _ in range(n):
  s = input()
  temp = command(s)
  if temp != "False":
    answer.append(temp)

for ans in answer:
  print(ans)
