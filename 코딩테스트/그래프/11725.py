from collections import deque

n = int(input())
lst = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
for _ in range(n-1):
  a,b = map(int,input().split())
  lst[a].append(b)
  lst[b].append(a)
q = deque([1])
while q:
  root = q.popleft()
  for i in lst[root]:
    if answer[i] == 0:
      answer[i] = root
      q.append(i)

for i in range(2,n+1):
  print(answer[i])
