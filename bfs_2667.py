from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
  lst.append(list(map(int,list(input().rstrip()))))
#필요한 변수 입력

q = deque()
total = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = []
#사용되는 변수 설정

for i in range(n):
  for j in range(n):
    #모든 장소 탐색
    
    if lst[i][j] == 1:
      count = 1
      total += 1
      q.append([i,j])
      lst[i][j] = 0
      # 아파트가 발견되면 아파트 단지를 찾는 과정 실행, 단지 갯수, 아파트갯수 증가
      
      while q:
        temp = q.popleft()
        for k in range(4):
          x, y = temp[0]+dx[k], temp[1]+dy[k]
          #아파트와 인접한 다른 아파트를 찾는 반복문
          
          if  0<=x<n and 0<=y<n and lst[x][y] == 1:
            lst[x][y] = 0
            count += 1
            q.append([x,y])
            #인접한 다른 아파트를 찾았다면 그 단지의 아파트 갯수에 추가
            
      answer.append(count)

answer.sort()
print(total)
for i in answer:
  print(i)
