n = int(input())
#입력값 입력

i = 0
while True:
  if 2**i >= n:
    i -= 1
    break
  i += 1
#필요한 i값 계산

if n == 1 or n ==2:
  print(n)
else:
  print(2*(n-(2**i)))
#n과 i에 따른 계산 출력
