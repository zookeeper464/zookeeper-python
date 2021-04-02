s = input()
stack = 0
answer = 0
i = 0
#필요한 값 입력

while i < len(s)-1:
  if s[i]+s[i+1] == "()":
    answer += stack
    i += 2
  #레이저가 나오면 강철만큼 갯수 추가
  elif s[i] == "(":
    answer += 1
    stack += 1
    i += 1
  #강철 추가
  else:
    i += 1
  #강철 제거

print(answer)
