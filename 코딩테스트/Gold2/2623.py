from collections import deque

n,m = map(int,input().split())
topl = [0]*(n+1)
v_list = [dict() for _ in range(n+1)]
for _ in range(m):
  lst = list(map(int,input().split()))
  num, lst = lst[0],lst[1:]
  for i in range(num-1):
    topl[lst[i+1]] += 1
    try:
      v_list[lst[i]][lst[i+1]] += 1
    except:
      v_list[lst[i]][lst[i+1]] = 1

q = deque()    
for i in range(1,n+1):
  if topl[i] == 0:
    q.append(i)

answer= []
while q:
  temp = q.popleft()
  answer.append(temp)
  for i in v_list[temp]:
    topl[i] -= v_list[temp][i]
    if topl[i] == 0:
      q.append(i)

if n == len(answer):
  print(*answer,sep='\n')
else:
  print(0)
