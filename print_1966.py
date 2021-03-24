from collections import deque

k = int(input())

answer = []
for i in range(k):
  n,m = map(int,input().split())
  lst = list(map(int,input().split()))
  goal = [False] * n
  goal[m] = True
  gq = deque(goal)
  lq = deque(lst)
  rank = 0
  #계산에 필요한 변수들 설정

  while True:
    x = max(lq)
    temp1 = lq.popleft()
    temp2 = gq.popleft()
    if temp1 == x:
      rank += 1
      if temp2:
        break
      pass
    # 만약 가장 큰 값이라면 빼내고 만약 원하는 값이면 탈출
    else:
      lq.append(temp1)
      gq.append(temp2)
    #만약 가장 큰 값이 아니라면 다시 뒤에 넣는다.

  answer.append(rank)
  #탈출했다면 rank를 answer에 넣는다.

for i in answer:
  print(i)
