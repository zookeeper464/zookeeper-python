#입력값을 받는다.
lst = []
while True:
  n = int(input())
  if n == 0:
    break
  lst.append(n)

#소수를 판별하기 위한 도구를 준비한다.
m = max(lst)
plst = [True for _ in range(2*m+1)]
plst[0], plst[1] = False, False
for i in range(2,2*m+1):
  if plst[i]:
    j = 2
    while i*j<=2*m:
      plst[i*j]=False
      j+=1

#출력부분 계산
for i in lst:
  temp = 0
  for j in range(i+1,2*i+1):
    if plst[j]:
      temp += 1
  print(temp)
