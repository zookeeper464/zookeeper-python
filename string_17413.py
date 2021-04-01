s = input()

temp = ""
answer = ""
i = 0
n = len(s)
# 입력이 필요한 부분 입력

while i < n:
  if s[i] =="<":
    while True:
      temp += s[i]
      if s[i] == ">":
        i += 1
        break
      i += 1
      if i == n:
        break
    answer += temp
    temp = ""
  # <>로 구성된 부분을 입력받고 순서를 그대로 입력
  
  elif s[i] == " ":
    answer += s[i]
    i += 1
  # 띄어쓰기가 나온다면 그대로 입력
  
  else:
    while True:
      temp += s[i]
      i += 1
      if i == n:
        break
      if s[i] == " " or s[i] == "<":
        break
    temp = temp[::-1]
    answer += temp
    temp = ""
    # <>부분이 아니라면 순서를 반대로 하여 입력

print(answer)
