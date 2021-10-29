# number 2
from collections import deque

# 테스트 횟수 : c
c = int(input())
# 시간을 저장하는 리스트 : answer
answer = []

for _ in range(c):
  # 건물의 층 수 : n, 최대 탑승가능 수 : m, 주어진 시간 : t
  n,m,t = map(int,input().split())
  # 주어진 시간에 따라서 승객관리, 승강기 관리를 한다.
  # 각 층에 존재하는 승객 : stair_in_man, 승강기 속 승객 정보 : lst
  stair_in_man = [deque() for _ in range(n+1)]
  lst = [0] * (n+1)
  #승강기의 위치 : num, 승강기의 방향 : look(1이면 위, 0이면 아래)
  num,look = 1,1
  # 승강기에 타고 있는 최대 인원 : s, 정답을 호출하기 위한 변수 : ans
  s,ans = 0,0


  for time_ in range(1,t+1):
    in_stair, out_stair = map(int,input().split())
    # 사람이 이동하는 층이 없다면 넘어간다.
    if in_stair == out_stair:
      pass

    # 이동해야 한다면 그 층에 서있는 것으로 저장한다.
    stair_in_man[in_stair].append(out_stair)
    # 사람이 탔는지 여부를 확인하는 변수 : check
    check = True
    while check:
      # 올라가는지 내려가는지 판단해서 처리한다.
      if look:
        # 천천히 올라가면서 내리거나 타야하는 사람을 찾는다.
        for i in range(num,n+1):
          # 내리거나 타야하는 사람이 있다면 해당 작업을 실행한다.
          if stair_in_man[i] or lst[i]:
            # 내려야 하는 모든 사람이 내린다.
            lst[i] = 0
            check = False
            # 만약 타야 하는 사람이 있다면 제일 오래 기다린 사람 한명만 태운다.
            if stair_in_man[i]:
              floor = stair_in_man[i].popleft()
              lst[floor] += 1
            # 문이 열리고 닫혔으니 다음 시간 사람을 입력 받는다.
            break

      else:
        # 천천히 올라가면서 내리거나 타야하는 사람을 찾는다.
        for i in range(num,0,-1):
          # 내리거나 타야하는 사람이 있다면 해당 작업을 실행한다.
          if stair_in_man[i] or lst[i]:
            # 내려야 하는 모든 사람이 내린다.
            lst[i] = 0
            check = False
            # 만약 타야 하는 사람이 있다면 제일 오래 기다린 사람 한명만 태운다. 
            if stair_in_man[i]:
              floor = stair_in_man[i].popleft()
              lst[floor] += 1
            # 문이 열리고 닫혔으니 다음 시간 사람을 입력 받는다.
            break
      
      # 만약 승강기의 위치가 1층 또는 n층이라면 방향을 바꾼다.
      num = i
      if num == n:
        look = 0
      elif num == 1:
        look = 1

    # 승강기 내부의 인원이 변경되었다면 파악한뒤 조건을 만족하지 않으면 현재 시간을 ans에 저장하고 탈출한다.
    temp = sum(lst)
    if temp>m:
      ans = time_
      break
    # 아니라면 현재 승강기에 탑승한 인원과 기존의 승강기에 탑승한 인원을 비교하여 큰값을 저장한다.
    else:
      s = max(temp,s)
  
  # 인원초가인 경우 시간을 저장한다.
  if ans:
    answer.append(ans)
  # 아닌경우 (기존의 승강기에 탑승한 최대인원)*(-1)을 저장한다.
  else:
    answer.append(-s)

# 저장된 값을 출력한다.
print(*answer,sep='\n')
