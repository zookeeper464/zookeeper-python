s = input()
n = len(s)
s = int(s)
answer =0
#필요한 변수 입력

for i in range(max(0,s-54), s+1):
  lst = list(str(i))
  temp = i
  for j in lst:
    temp += int(j)
  #i로 생성되는 분해합 계산
  
  if temp == int(s):
    answer = i
    break
  #분해합이 존재한다면 탈출

print(answer)
