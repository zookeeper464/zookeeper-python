from collections import deque

f,s,g,u,d = map(int,input().split())
t = max(f,g+d)
lst = [-1 for _ in range(f+1)]
q= deque([s])
lst[s] = 0
answer = "use the stairs"

while q:
  for i in range(len(q)):
    p = q.popleft()
    if p+u<=f and lst[p+u] == -1:
      lst[p+u] = lst[p]+1
      q.append(p+u)
    if p-d>0 and lst[p-d] == -1:
      lst[p-d] = lst[p]+1
      q.append(p-d)
  if lst[g] != -1:
    answer = lst[g]

print(answer)
