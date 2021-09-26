from collections import deque

def left (num):
  n = num//1000
  num = (10*num)%10000+n
  n = str(num)
  n = '0'*(4-len(a))+n
  return n

def right (num):
  n = num%10
  num = (num//10)+(n*1000)
  n = str(num)
  n = '0'*(4-len(a))+n
  return n

def minus (num):
  if num == 0:
    return '9999'
  num -= 1
  n = str(num)
  n = '0'*(4-len(a))+n
  return n

def multiple (num):
  num = (2*num)%10000
  n = str(num)
  n = '0'*(4-len(a))+n
  return n

def bfs (q):
  global b
  visited = [False for _ in range(10000)]
  visited[int(q[0][0])] = True
  while q:
    for _ in range(len(q)):
      s, string = q.popleft()
      l = left(int(s))
      r = right(int(s))
      mi = minus(int(s))
      mu = multiple(int(s))
      
      for idx,i in enumerate([l,r,mi,mu]):
        if not visited[int(i)]:
          visited[int(i)] = True
          q.append([i, string+'LRSD'[idx]])
          if int(i) == b:
            return string+'LRSD'[idx]
      
  return 'error'

t = int(input())
answer = []
for _ in range(t):
  a,b = input().split()
  a = '0'*(4-len(a))+a
  b = int(b)
  q = deque([[a,'']])
  answer.append(bfs(q))

for ans in answer:
  print(ans)
