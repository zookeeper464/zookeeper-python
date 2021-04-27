from collections import deque

t = int(input())
sol = []
#테스트 횟수 입력

for _ in range(t):
  n = int(input())
  lst = [list(map(int,input().split())) for __ in range(n+2)]
  #편의점과 도착점, 출발점 입력

  q = deque([lst[0]])
  #출발점 설정

  visited = [False for __ in range(n+2)]
  visited[0] = True
  s, answer = True, "sad"
  #필요한 변수 설정

  while q and s:
    #이동가능한 위치가 없거나 도착점에 도착한다면 탈출

    temp = q.popleft()
    for i in range(n+2):
      if not visited[i] and abs(lst[i][0]-temp[0])+abs(lst[i][1]-temp[1])<=1000:
        #이동하지 않고 거리가 1000이하인 지점이면 실행
        
        if i == n+1:
          s= False
          answer = "happy"
          break
          #만약 도착지점에 도달한다면 정답을 happy로 변경

        q.append(lst[i])
        visited[i] = True
        #도착지점이 아니라면 이동한 위치에서 다시 탐색

  sol.append(answer)

for i in sol:
  print(i)
