answer = []

for i in range(5):
  s = input()
  n = len(s)
  for j in range(n):
    if s[j] == "F" and j < n-2:
      if s[j+1]+s[j+2] =="BI":
        answer.append(i+1)
        break
  #FBI가 들어간 첩보명을 찾고 입력

if answer:
  for i in answer:
    print(i, end = " ")
else:
  print("HE GOT AWAY!")
  #첩보명이 없다면 추방
