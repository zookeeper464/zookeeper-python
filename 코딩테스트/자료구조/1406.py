from collections import deque

s = input()
q1 = list(s)
q2 = deque()

def functions (s):
  global q1,q2
  lst = s.split()
  if len(lst) == 1:
    temp = lst[0]
    if temp == "L" and q1:
      x = q1.pop()
      q2.appendleft(x)
    if temp == "D" and q2:
      x = q2.popleft()
      q1.append(x)
    if temp == "B" and q1:
      q1.pop()
  else:
    q1.append(lst[1])

m = int(input())
for _ in range(m):
  s = input()
  functions(s)

answer = q1+list(q2)
print("".join(answer))
