from collections import deque

n = int(input())
q = deque([i+1 for i in range(n)])
#필요한 변수 입력

while q:
  print(q.popleft(), end = " ")
  #제일 위의 카드 출력
  if not q:
    break
  #출력이후 덱이 없다면 종료

  temp = q.popleft()
  q.append(temp)
  #덱이 존재하면 셔플
