n,m = map(int,input().split())
#입력하고자 하는 값 입력

if n > 2:
  if m <= 4:
    print(m)
  elif m < 7:
    print(4)
  else:
    print(m-2)
elif n ==1:
  print(1)
else:
  if m < 8:
    print((m+1)//2)
  else:
    print(4)
#출력하고자 하는 값을 조건에 따라서 분류
