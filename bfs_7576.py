from collections import deque
import sys
input = sys.stdin.readline

q = deque()
total = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = []
s = True
#필요한 변수 설정

m, n = map(int,input().split())
lst = []
for i in range(n):
  lst.append(list(map(int,input().split())))
  for j in range(m):
    if lst[i][j] == 1:
      q.append([i,j])
#필요한 변수 입력
      
while q:
  total += 1
  #몇 초가 지나야 익는지 확인
  
  for i in range(len(q)):
    #해당 초에 익는 토마토를 모두 확인
    
    temp = q.popleft()
    for j in range(4):
      x, y = temp[0]+dx[j], temp[1]+dy[j]
      if 0<=x<n and 0<=y<m and lst[x][y] == 0:
        lst[x][y] = 1
        q.append([x,y])
        #해당 초에서 익은 모든 토마토의 주변 토마토를 다음 초에 익는다고 변경

for i in range(n):
  for j in range(m):
    if lst[i][j] == 0:
      s = False
      break
#모든 토마토가 다 익었는지 확인하기 위한 방법
      
if s:
  print(total-1)
else:
  print(-1)
