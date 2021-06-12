from collections import deque

q = deque()
total = 0
count = 0
s = True

n, k = map(int,input().split())
visited = [False for i in range(100001)]
visited[n] = True
q = deque()
q.append(n)

while q:
  for i in range(len(q)):
    temp = q.popleft()
    if temp == k:
      s = False
      break
    lst = [temp-1,temp+1, 2*temp]
    for j in lst:
      if 0<= j < min(max(n,k)+2,100001) and not visited[j]:
        visited[j] = True
        q.append(j)
  if not s:
    break
  count += 1

print(count)
