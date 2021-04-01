n = int(input())
s = input()
#입력해야 하는 값 입력

answer = 0
for i in s:
  if i == "A":
    answer += 1
  else:
    answer -= 1
#입력받은 표의 상대적인 값 입력

if answer > 0:
  print("A")
elif answer < 0:
  print("B")
else:
  print("Tie")
#answer의 값에 따른 결과 출력
