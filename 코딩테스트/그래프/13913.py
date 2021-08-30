from collections import deque

visited = [-1]* 100001
n,m = map(int,input().split())
q = deque([n])
visited[n] = -2

def bfs():
  global visited
  while q:
    for _ in range(len(q)):
      temp = q.popleft()
      for i in [temp+1,temp-1,temp*2]:
        if 0<=i<=100000 and visited[i] == -1:
          visited[i] = temp
          q.append(i)
          if i == m:
            return

bfs()
answer = []
temp = m
while True:
  answer.append(m)
  m = visited[m]
  if m == -2:
    break

print(len(answer)-1)
for _ in range(len(answer)):
  print(answer.pop(),end=' ')
