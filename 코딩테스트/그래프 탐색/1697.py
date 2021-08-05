from collections import deque
import sys
input = sys.stdin.readline

q = deque()
total = 0
count = 0
s = True

n, k = map(int,input().split())
visited = [False for i in range(100001)]
visited[n] = True
q = deque()
q.append(n)

while s and q:
  count += 1
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

print(count-1)
