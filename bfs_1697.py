from collections import deque
import sys
input = sys.stdin.readline

q = deque()
total = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
count = 0
s = True
#필요한 변수 설정

n, k = map(int,input().split())
visited = [False for i in range(100001)]
visited[n] = True
q = deque()
q.append(n)
#필요한 변수 입력

while s and q:
  count += 1
  # 이동한 횟수 추가
  
  for i in range(len(q)):
    temp = q.popleft()
    #현재 위치 상황
    
    if temp == k:
      s = False
      break
      #현재 위치가 도착지점이면 탈출
      
    lst = [temp-1,temp+1, 2*temp]
    for j in lst:
      if 0<= j < min(max(n,k)+2,100001) and not visited[j]:
        visited[j] = True
        q.append(j)
        #이동 할 수 있는 모든 위치를 입력

print(count-1)
