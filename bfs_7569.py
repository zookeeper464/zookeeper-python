import sys
from collections import deque
input = sys.stdin.readline

n, m, h = map(int,input().split())
lst = []
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
count = -1
s = True

q = deque()
for i in range(h):
  temp = []
  for j in range(m):
    temp.append(list(map(int,input().split())))
    for idx, v in enumerate(temp[-1]):
      if v == 1:
        q.append([i,j,idx])
  lst.append(temp)
#입력 순서는 h,m,n순서로 index를 입력받는다.
#필요한 모든 변수 입력

while q:
  count += 1
  for i in range(len(q)):
    temp = q.popleft()
    #주어진 모든 q의 스택에 대해서 주변 상황 탐색
    
    for j in range(6):
      z,y,x = temp[0]+dz[j],temp[1]+dy[j],temp[2]+dx[j]
      if 0<=z<h and 0<=y<m and 0<=x<n and lst[z][y][x] == 0:
        lst[z][y][x] = 1
        q.append([z,y,x])
        #temp 주변에 0가 있다면 1로 변경해주고 q에 추가

for i in lst:
  if not s:
    break
  for j in i:
    if 0 in j:
      count = -1
      s = False
      break
#만약 0이 존재한다면 count를 -1로 변경      

print(count)
