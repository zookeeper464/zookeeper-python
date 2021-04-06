n = int(input())
lst = list(map(int,input().split()))
stack = []
answer = []
#기본 변수 입력

for i in range(n-1,-1,-1):
  if not stack:
    answer.append(-1)
    stack.append(lst[i])
  #스택이 비어있다면 -1을 출력하고 숫자를 stack에 넣는다.
  else:
    while stack:
      temp = stack.pop()
      if temp > lst[i]:
        stack.append(temp)
        stack.append(lst[i])
        answer.append(temp)
        break
      #stack에서 호출한 숫자가 비교하려는 숫자에 비해 크다면 다시 넣고 비교한 숫자도 넣고 호출한 숫자를 정답에 넣는다.

    if not stack:
      answer.append(-1)
      stack.append(lst[i])
    #계속 추출하다가 stack에 있는 내용이 모두 나가면 -1을 추출하고 stack에는 숫자를 넣는다.
    
for i in range(n-1,-1,-1):
  print(answer[i], end = " ")
