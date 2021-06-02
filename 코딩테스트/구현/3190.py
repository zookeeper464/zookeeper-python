from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
lst = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
  a,b = map(int,input().split())
  lst[a-1][b-1] = -1
turn = []
l = int(input())
for _ in range(l):
  t, s = input().split()
  t = int(t)
  turn.append([t,s])

dx, dy = [1,0,-1,0], [0,1,0,-1]
t, look, i = 0,0,0
tail = deque([[0,0]])
head = [0,0]
while True:
  t += 1

  x,y = head[0],head[1]
  nx,ny = x+dx[look], y+dy[look]
  if 0<=nx<n and 0<=ny<n and [nx,ny] not in tail:
    head = [nx,ny]
    tail.append(head)
    if lst[ny][nx] != -1:
      tail.popleft()
  else:
    break

  if i<len(turn) and t == turn[i][0]:
    if turn[i][1] == "D":
      look = (look+1)%4
    else:
      look = (look+3)%4
    i += 1
  
  lst[ny][nx] = t
print(t)
