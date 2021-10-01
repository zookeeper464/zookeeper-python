from heapq import heappop, heappush

def check (num):
  global st
  for i in lst[num]:
    if i[1] not in st:
      heappush(q,i)
  st.add(num)

v,e = map(int,input().split())
lst = [[] for _ in range(v+1)]
answer = 1000000
for _ in range(e):
  a,b,c = map(int,input().split())
  if answer > c:
    x,y = a,b
    answer = c
  
  lst[a].append((c,b))
  lst[b].append((c,a))

q, st = [], set([x,y])
check(x)
check(y)

while q:
  val, node = heappop(q)
  if node not in st:
    check(node)
    answer += val
  if len(st)==v:
    break

if len(st)==v:
  print(answer)
else:
  print(-1)
