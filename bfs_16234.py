import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int,input().split())
lst = []
for i in range(n):
  lst.append(list(map(int,input().split())))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
#기본 변수 입력

def check (q,tlst):
  while q:
    #탐색할 곳이 남아 있다면 반복문 실행

    for i in range(len(q)):
      temp = q.popleft()
      tlst.append(temp)
      visited[temp[0]][temp[1]] = True
      #탐색한 곳은 자료에 남긴다.
      
      for j in range(4):
        x, y = temp[0]+dx[j], temp[1]+dy[j]
        if 0<=x<n and 0<=y<n:
          #탐색할 곳이 리스트 안에 있다면 실시
          if  not visited[x][y] and l<=abs(lst[temp[0]][temp[1]]-lst[x][y])<=r:
            #탐색할 곳이 방문하지 않았고 조건을 만족한다면 탐색할 곳에 추가

            q.append([x,y])
            visited[x][y] = True
#탐색 시작이후 다른 곳을 탐색하기 위한 함수            

def ev (tlst, n):
  temp = 0
  for i in tlst:
    temp += lst[i[0]][i[1]]
  #탐색한 곳들의 수치를 더한다.
  
  temp = temp//n
  #평균을 구한 뒤 소숫점을 버린다.

  return temp 
#탐색 이후에 산출 값을 계산하기 위한 함수

count = 0
#이동한 횟수

while True:
  visited = [[False for i in range(n)] for i in range(n)]
  s, tlst = 0, []
  #처음 탐색할때마다 초기화 시켜주는 변수

  for i in range(n):
    for j in range(n):
      #모든 위치를 파악한다.

      if j<n-1 and not visited[i][j] and not visited[i][j+1] and l<=abs(lst[i][j]-lst[i][j+1])<=r:
        #리스트 내부에 있으며 비교 대상이 모두 탐색한 곳이 아니며 탐색할 두 구역이 조건을 만족한다면 실시한다.

        tlst.append([])
        q = deque([[i,j],[i,j+1]])
        visited[i][j] = True
        visited[i][j+1] = True
        #탐색할 리스트를 구성하고 탐색 구역을 활성화한다.
        
        check(q,tlst[-1])
        #탐색 함수를 실시한다.

        num = ev(tlst[-1],len(tlst[-1]))
        #평균값을 계산한다.

        for k in tlst[-1]:
          lst[k[0]][k[1]] = num
        #각 자리에 평균값을 입력한다.
          
      elif i<n-1 and not visited[i][j] and not visited[i+1][j] and l<=abs(lst[i][j]-lst[i+1][j])<=r:
        #리스트 내부에 있으며 비교 대상이 모두 탐색한 곳이 아니며 탐색할 두 구역이 조건을 만족한다면 실시한다.

        tlst.append([])
        q = deque([[i,j],[i+1,j]])
        visited[i][j] = True
        visited[i+1][j] = True
        #탐색할 리스트를 구성하고 탐색 구역을 활성화한다.

        check(q,tlst[-1])
        #탐색 함수를 실시한다.

        num = ev(tlst[-1],len(tlst[-1]))
        #각 자리에 평균값을 입력한다.

        for k in tlst[-1]:
          lst[k[0]][k[1]] = num
        #각 자리에 평균값을 입력한다.
      
      #위에 가로와 세로 탐색의 경우 함수를 이용하여 하나의 탐색으로 줄일 수 있다.

      else:
        s += 1
      #탐색을 시작하지 않은 횟수를 센다.

  if s == n**2:
    break
  #모든 자리를 탐색하지 않는다면 탈출

  else:
    count += 1
  #탐색을 한번이라도 실시하면 count를 센다.

print(count)
