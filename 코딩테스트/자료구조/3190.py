from collections import deque
import heapq

n,k = int(input()), int(input())
lst = [[0]*n for _ in range(n)]
for _ in range(k):
  r,c = map(int,input().split())
  lst[r-1][c-1] = -1

l = int(input())
dr,dc = [0,1,0,-1],[1,0,-1,0]
look = 0
time_list = []
for _ in range(l):
  t,s = input().split()
  t = int(t)
  heapq.heappush(time_list,(t,s))

q = deque([[0,0]])
now = 0
while True:
  now += 1
  nr,nc = q[-1][0]+dr[look],q[-1][1]+dc[look]
  if 0<=nr<n and 0<=nc<n:
    pass
  else:
    break
  q.append([nr,nc])
  if lst[nr][nc] == 1:
    break

  if time_list and time_list[0][0] == now:
    tt, ll = heapq.heappop(time_list)
    if ll == "L":
      look = (look+3)%4
    else:
      look = (look+1)%4

  if lst[nr][nc] != -1:
    tr,tc = q.popleft()
    lst[tr][tc] = 0

  lst[nr][nc] = 1

print(now)
