from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
answer = []
for _ in range(t):
  a,b = input().rstrip("\n").split()
  b = int(b)
  lst = ["" for _ in range(10000)]
  q = deque([a])
  while q:
    s = q.popleft()
    if len(s) != 4:
      s = "0"*(4-len(s))+s
    temp = lst[int(s)]
    n = (2*int(s))%10000
    if not lst[n]:
      lst[n] = temp+"D"
      q.append(str(n))
    
    x0 = int(s[1]+s[2]+s[3]+s[0])%10000
    x1 = int(s[0]+s[2]+s[3]+s[1])%10000
    x2 = int(s[0]+s[1]+s[3]+s[2])%10000
    if not lst[x0]:
      lst[x0] = temp+"L"
      q.append(str(x0))
    if not lst[x1]:
      lst[x1] = temp+"L"
      q.append(str(x1))
    if not lst[x2]:
      lst[x2] = temp+"L"
      q.append(str(x2))

    if lst[b]:
      break
  
  answer.append(lst[b])

for ans in answer:
  print(ans)
