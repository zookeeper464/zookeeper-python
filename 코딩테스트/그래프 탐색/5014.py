from collections import deque

f,s,g,u,d = map(int,input().split())
lst = [-1] * (f+1)
cnt = 0
lst[s] = cnt
q = deque([s])

while q:
  cnt += 1
  for _ in range(len(q)):
    temp = q.popleft()
    up = temp+u
    down = temp-d
    if g in {up,down}:
      lst[g] = cnt
      q = False
      break
    if up<=f and lst[up] == -1:
      lst[up] = cnt
      q.append(up)
    if down>0 and lst[down] == -1:
      lst[down] = cnt
      q.append(down)
      
if lst[g] == -1:
  print('use the stairs')
else:
  print(lst[g])
