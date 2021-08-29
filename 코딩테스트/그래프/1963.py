from collections import deque

p_list = [True for i in range(10001)]
for i in range(2, 101):
  if p_list[i]:
    j = i * 2
    while j < 10001:
      p_list[j] = False
      j += i

answer = []
t = int(input())

def bfs(a, b):
  q = deque()
  q.append([a, 0])
  visited = [0 for i in range(10000)]
  visited[a] = 1

  while q:
    num, cnt = q.popleft()
    if num == b:
      return cnt
    if num < 1000:
      continue

    for i in [1, 10, 100, 1000]:
      n = num - num % (i * 10) // i * i
      for j in range(10):
        if visited[n] == 0 and p_list[n]:
          visited[n] = 1
          q.append([n, cnt + 1])
        n += i

for i in range(t):
  a, b = map(int, input().split())
  ans = bfs(a, b)
  answer.append(ans)

for ans in answer:
  print(ans)
