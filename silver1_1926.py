from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
#입력받을 값 입력

cnt, size = 0, 0
dx, dy = [1,0,-1,0], [0,1,0,-1]
#필요한 변수 설정

for i in range(n):
  for j in range(m):
    #모든 자리 탐색
    
    if lst[i][j] == 1:
      cnt += 1
      q = deque([[i,j]])
      temp, lst[i][j] = 0, 0
      #그림을 발견했을 때 새로운 변수 설정
      
      while q:
        #그림에 대한 탐색 시작
        
        temp += len(q)
        #그림의 크기 계산
        
        for t in range(len(q)):
          l = q.popleft()
          for k in range(4):
            x, y = l[0]+dx[k], l[1]+dy[k]
            if 0<=x<n and 0<=y<m and lst[x][y] == 1:
              q.append([x,y])
              lst[x][y] = 0
              #탐색한 그림에 대한 주변 탐색
          
      size = max(size,temp)
      #가장 큰 그림의 크기 계산

print(cnt)
print(size)
