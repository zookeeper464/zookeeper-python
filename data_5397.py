from collections import deque

n = int(input())
answer = []
for i in range(n):
  lst = list(input())
  front = []
  back = deque()
  #필요한 변수 입력

  for j in lst:
    if j =="<":
      if front:
        temp = front.pop()
        back.appendleft(temp)
    #앞에 문자가 있을때, 커서 위치 이동

    elif j == ">":
      if back:
        temp = back.popleft()
        front.append(temp)
    #뒤에 문자가 있을때, 커서 위치 이동

    elif j == "-":
      if front:
        front.pop()
    #앞에 문자가 있을때, 앞에 문자 1개 삭제

    else:
      front.append(j)
    #문자 추가

  answer.append("".join(front+list(back))) 

for i in answer:
  print(i) 
