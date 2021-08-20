from collections import deque

def left (num):
  n = num//1000
  num = (10*num)%10000+n
  return num

def right (num):
  n = num%10
  num = (num//10)+(n*1000)
  return num

def minus (num):
  if num == 0:
    return 9999
  return num-1

def multiple (num):
  return (2*num)%10000

t = int(input())
answer = []

for _ in range(t):
  start, end = map(int,input().split())
  dp = ['' for _ in range(10000)]
  q = deque([start])
  
  if start == end:
    q = False
  
  while q:
    for _ in range(len(q)):
      num = q.popleft()
      temp = dp[num]
      l = []

      a = multiple(num)
      if not dp[a]:
        dp[a] = temp+"D"
        l.append(a)

      b = minus(num)
      if not dp[b]:
        dp[b] = temp+'S'
        l.append(b)

      c = left(num)
      if not dp[c]:
        dp[c] = temp+'L'
        l.append(c)

      d = right(num)
      if not dp[d]:
        dp[d] = temp+'R'
        l.append(d)
        
      if end in l:
        q = False
        break

      for i in l:
        q.append(i)

  answer.append(dp[end])

print('\n'.join(answer))
