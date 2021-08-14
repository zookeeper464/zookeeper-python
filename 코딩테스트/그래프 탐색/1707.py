from collections import deque

def check (q, num):
  global ans
  m = 3 - num
  for _ in range(len(q)):
    temp = q.popleft()
    for i in lst[temp]:
      if visited[i] == 0:
        visited[i] = m
        q.append(i)
      elif visited[i] == num:
        ans = 'NO'
  return q

k = int(input())
answer = []
for _ in range(k):
  ans = 'YES'
  v,e = map(int,input().split())
  lst = [[] for _ in range(v+1)]

  for _ in range(e):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
  
  visited = [0] * (v+1)
  for i in range(1,v+1):
    if visited[i] == 0:
      visited[i] = 1
      q = deque([i])
      while q:
        q = check(q,1)
        q = check(q,2)
        if ans == 'NO':
          break
  answer.append(ans)

for ans in answer:
  print(ans)
