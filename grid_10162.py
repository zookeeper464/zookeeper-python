n = int(input())
lst = [300,60,10]
answer = list("000")
#필요한 입력값 설정
if n%10 != 0:
  print(-1)
  #만약 시간 설정이 불가능하면 -1 출력
else:
  for i in range(3):
    if n >= lst[i]:
      answer[i] = str(n//lst[i])
      n %= lst[i]
    #만약 시간이 해당 단위 시간보다 크다면 그 시간만큼 누르고 누른 결과를 입력한다.
  print(" ".join(answer))
