import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
lst = []
mi, ma = 100, 0
for i in range(n):
  l = list(map(int,input().split()))
  lst.append(l)
  mi, ma = min(l+[mi]), max(l+[ma])
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 1
#필요한 변수 모두 입력

def bfs (m, lst, lst2):
  count = 0
  for i in range(n):
    for j in range(n):
    #모든 자리 탐색
    
      if lst[i][j] > m and not lst2[i][j]:
        count += 1
        q = deque([[i,j]])
        lst2[i][j] = True
        #젖지 않은 자리가 나오면 탐색 시작
        
        while q:
          temp = q.popleft()
          for k in range(4):
            x, y = temp[0]+dx[k], temp[1]+dy[k]
            if 0<=x<n and 0<=y<n and lst[x][y]>m and not lst2[x][y]:
              lst2[x][y] = True
              q.append([x,y])
        #주변에 젖지 않은 모든 자리 탐색
        
  return count

for i in range(mi, ma+1):
  visited = [[False for i in range(n)] for i in range(n)]
  answer = max(answer,bfs(i,lst,visited))
  #매 순간 visited 리셋
  
print(answer)
