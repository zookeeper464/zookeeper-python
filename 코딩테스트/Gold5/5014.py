from collections import deque

f,s,g,u,d = map(int,input().split())
lst = [-1]*(f+1)
lst[s] = 0
q = deque([s])

while q:
  for _ in range(len(q)):
    temp = q.popleft()
    num = lst[temp]
    for i in (u,-d):
      t = temp+i
      if 0<t<=f and lst[t] == -1:
        lst[t] = num+1
        q.append(t)
        if t == g:
          break
    if t == g:
      q = deque()
      break

if lst[g] == -1:
  print('use the stairs')
else:
  print(lst[g])
