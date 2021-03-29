from collections import deque

answer = []
n = int(input())
for i in range(n):
  s = input()
  m = input()
  
  l = input()[1:-1].split(",")
  try:
    lst = list(map(int,l))
  except:
    lst = []
  q = deque(lst)
#원하는 요구사항 입력값들을 모두 처리한다.

  def read (q, s):
    temp = 0
    lst = [0,0]
    for i in s:
      if i =="R":
        temp += 1
        temp %= 2
      elif i == "D" and temp == 1:
        lst[1] += 1
      elif i == "D" and temp == 0:
        lst[0] += 1
    #입력된 문자를 처리가능한 숫자로 변환

    for i in range(2):
      if i == 0:
        for j in range(lst[i]):
          if q:
            q.popleft()
          else:
            return ("error")
      else:
        q.reverse()
        for j in range(lst[i]):
          if q:
            q.popleft()
          else:
            return ("error")
    #입력된 수에 맞게 요구하는 함수 처리


    if temp == 0:
      q.reverse()
    #마지막으로 뒤집혀있는지 확인
    
    return ("[" + ",".join(list(map(str, q))) + "]")
    #문제 요구에 맞게 리스트 변환
  #글을 읽어 요구하는 함수 실행

  answer.append(read(q, s))

for i in answer:
  print(i)
