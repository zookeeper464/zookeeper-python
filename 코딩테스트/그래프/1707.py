from collections import deque

k = int(input())
answer = []

for _ in range(k):
  v,e = map(int,input().split())
  lst = [[] for _ in range(v+1)]
  visited1 = [False for _ in range(v+1)]
  visited2 = [False for _ in range(v+1)]
  answer1 = [1]
  answer2 = []
  for _ in range(e):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
  q1 = deque([1])
  q2 = deque()
  visited1[1] = True

  while True:
    for _ in range(len(q1)):
      x1 = q1.popleft()
      for i in lst[x1]:
        if not visited2[i]:
          q2.append(i)
          answer2.append(i)
          visited2[i] = True
    
    for _ in range(len(q2)):
      x2 = q2.popleft()
      for j in lst[x2]:
        if not visited1[j]:
          q1.append(j)
          answer1.append(j)
          visited1[j] = True
    
    if set(answer1)&set(answer2)!=set():
      break

    s = False
    if len(q1)+len(q2)==0:
      s = True
      for i in range(1,v+1):
        if visited1[i] or visited2[i]:
          pass
        else:
          s = False
          q1.append(i)
          visited1[i] = True
          break
    if s:
      break

  if not set(answer1)&set(answer2):
    answer.append("YES")
  else:
    answer.append("NO")

for i in answer:
  print(i)
