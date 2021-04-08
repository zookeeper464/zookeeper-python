temp = -100
lst = []
answer = []
#변수 입력

for i in range(9):
  n = int(input())
  lst.append(n)
  temp += n
  #모든 값 입력, 초과된 키 입력
  
x = True
for i in range(8):
  for j in range(i+1,9):
    if temp == lst[i]+lst[j]:
      for k in range(9):
        if k!=i and k!=j:
          answer.append(lst[k])
      x = False
      break
    #계산을 통해 스파이를 발견하면 탈출
    
  if not x:
    break

answer.sort()
#키순으로 정렬

for i in answer:
  print(i)
