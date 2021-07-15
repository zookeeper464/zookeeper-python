from collections import deque

n,m = map(int,input().split())
lst = list(map(int,input().split()))
answer = 0

q = deque(list(range(1,n+1)))
for i in range(m):
  cnt = 0
  while q[0] != lst[i]:
    el = q.popleft()
    q.append(el)
    cnt += 1

  l = len(q)
  if cnt > l//2:
    cnt = l-cnt
  q.popleft()
  answer += cnt

print(answer)
