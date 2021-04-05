s = input()
answer = []
lst = [""]

for i in s:
  if i == "(":
    lst.append("")
    #연산자 자리 추가
  
  elif i ==")":
    answer.append(lst.pop())
    #연산이 끝난 연산자 추출
  
  elif i in list("+-*/"):
    if lst[-1] == "":
      lst[-1] = i
    #연산자가 없다면 연산자를 올려놓고 종료
    
    elif i == "+" or i == "-":
      while len(lst) > 0:
        answer.append(lst.pop())
      lst.append(i)
      #연산자가 +,-일때, 저장된 연산자를 모두 꺼내어 답에 추가하고 지금 연산자를 lst에 놓는다.
      
    else:
      if lst[-1] in ["*","/"]:
        answer.append(lst[-1])
        lst[-1] = i
      #연산자가 *,/일때, 이전에 연산자를 답에 추가하고 지금 연산자를 lst에 놓는다.
      
      else:
        lst.append(i)
      #연산자가 *,/로 연속할때, 연산자를 lst에 추가한다.
      
  else:
    answer.append(i)
  #문자인 경우 그냥 답에 추가한다.
  
print("".join(answer+lst[::-1]))
