from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
stack, answer = deque(), []
#변수 입력

for i in range(n):
  temp = input()
  t = temp[0]
  #명령어 입력

  if t == "p":
    if temp[1] == "u":
      l = temp.split()
      stack.append(l[1])
    #입력이 push이면 뒤에 숫자를 stack에 넣는다.

    if temp[1] =="o":
      if stack:
        answer.append(stack.popleft())
      else:
        answer.append(-1)
    #입력이 pop이면 제일 앞의 수를 빼낸다. 수가 없다면 -1을 빼낸다.

  elif t == "s":
    answer.append(len(stack))
  #입력이 size이면 크기를 빼낸다.

  elif t == "e":
    if stack:
      answer.append(0)
    else:
      answer.append(1)
  #입력이 empty이면 스택의 빈 것의 유무를 판별한다.

  elif t == "f":
    if stack:
      tem = stack.popleft()
      answer.append(tem)
      stack.appendleft(tem)
    else:
      answer.append(-1)
  #입력이 front이면 제일 앞의 내용만 정답에 추가 없다면 -1 추가
  
  elif t == "b":
    if stack:
      tem = stack.pop()
      answer.append(tem)
      stack.append(tem)
    else:
      answer.append(-1)
  #입력이 back이면 제일 뒤의 내용만 정답에 추가 없다면 -1 추가


for i in answer:
  print(i)
