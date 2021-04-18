import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
lst = [[] for i in range(n+1)]
for i in range(m):
  a, b = map(int,input().split())
  if b not in lst[a]:
    lst[a].append(b)
    lst[b].append(a)
#주어진 사람에 대한 입력값과 친구관계에 대한 입력을 동시에 처리한다.

num = n*m
answer = 0
#변수 설정

for i in range(1, n+1):
  q = deque(lst[i])
  count = 0
  x = 1
  visited = [False for i in range(n+1)]
  for j in lst[i]:
    visited[j] = True
    count += x
  visited[i] = True
  #각 사람에 따른 변수 설정
  
  while q:
    x += 1
    for j in range(len(q)):
      temp = q.popleft()
      for k in lst[temp]:
        if not visited[k]:
          visited[k] = True
          q.append(k)
          count += x
    #각 사람마다 count를 계산하여 만나기 위한 횟수를 추가한다.

  if num > count:
    answer = i
    num = count

print(answer)
