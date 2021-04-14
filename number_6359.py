import sys
input = sys.stdin.readline

answer =[]
t = int(input())
#필요한 변수 입력

for i in range(t):
  n = int(input())
  lst = [1 for i in range(n+1)]
  lst[0] = 0
  #주어진 방의 갯수와 상황 입력
  
  for j in range(2,n+1):
    for k in range(1,n//j + 1):
      temp =j*k
      if lst[temp] == 1:
        lst[temp] = 0
      else:
        lst[temp] = 1
  #방을 열고 닫는 상황 입력
  
  answer.append(sum(lst))

for i in answer:
  print(i)
