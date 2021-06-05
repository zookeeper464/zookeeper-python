from collections import deque

t = int(input())
answer = []
for _ in range(t):
  s = input()
  n = int(input())
  temp = input()[1:-1].split(",")
  if temp != [""]:
    q = deque(list(map(int,temp)))
  else:
    q = deque()
  
  ck = 0
  for i in s:
    if i == "R":
      ck += 1
    elif ck%2==0 and q:
      q.popleft()
    elif ck%2==1 and q:
      q.pop()
    else:
      break
  if q:
    lst = list(q)
    if ck%2==1:
      lst = lst[::-1]
    answer.append(lst)  
  else:
    answer.append("error")

for i in answer:
  print(i)
