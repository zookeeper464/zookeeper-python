from collections import deque

n,m = map(int,input().split())
v_list = [[] for _ in range(n+1)]
topl = [0] * (n+1)
q = deque()
answer = []

for _ in range(m):
  a,b = map(int,input().split())
  topl[b] += 1
  v_list[a].append(b)


for i in range(1,n+1):
  if topl[i] == 0:
    q.append(i)


while q:
  for _ in range(len(q)):
    i = q.popleft()
    answer.append(i)
    for j in v_list[i]:
      topl[j] -= 1
      if topl[j] == 0:
        q.append(j)

print(*answer)
