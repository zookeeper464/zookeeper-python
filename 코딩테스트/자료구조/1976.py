from collections import deque

n,m = int(input()), int(input())
lst = [[] for _ in range(n+1)]
for i in range(n):
  tlst = list(map(int,input().split()))
  for j in range(n):
    if tlst[j] == 1:
      lst[i+1].append(j+1)

temp_list = list(map(int,input().split()))
q = deque([temp_list[0]])
check = set([temp_list[0]])

while q:
  temp = q.popleft()
  for i in lst[temp]:
    if not check & {i}:
      q.append(i)
      check.add(i)

if set(temp_list) - check:
  print('NO')
else:
  print('YES')
