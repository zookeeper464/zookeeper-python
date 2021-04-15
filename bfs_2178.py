from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = []
for i in range(n):
  lst.append(list(map(int,list(input().rstrip()))))
#필요한 변수 입력

visited = [[False for i in range(m)] for j in range(n)]
visited[0][0] = True
q = deque([[0,0]])
count = 1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
s = True
#필요한 조건 설정

while s:
  count += 1
  #움직인 횟수 추가
  
  for i in range(len(q)):
    temp = q.popleft()
  #움직인 횟수만큼 움직여서 이동한 자리를 추출
  
    for i in range(4):
      x, y = temp[0]+dx[i], temp[1] +dy[i]
    #그 자리에서 움직인 자리 설정
    
      if (x,y) == (n-1,m-1):
        s = False
        break
      #도착지점에 도달하면 탈출
      
      if 0<=x<n and 0<=y<m and not visited[x][y] and lst[x][y] == 1:
        visited[x][y] = True
        q.append([x,y])
      #미로 내부에 있고 도착한 지점이 아니며 길이 있다면 움직인다.
      
    if not s:
      break
    #계산용 탈출문
    
print(count)
