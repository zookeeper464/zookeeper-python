#입력값 입력
lst = []
while True:
  n = int(input())
  if n == 0:
    break
  lst.append(n)
m = max(lst)
#소수 판별 리스트 생성
plst = [True for _ in range(m+1)]
plst[0], plst[1] = False, False
for i in range(2,m+1):
  if plst:
    j = 2
    while i*j<=m:
      plst[i*j] = False
      j += 1

for i in lst:
  for j in range(2,i):
    if plst[j] and plst[i-j]:
      print(f"{i} = {j} + {i-j}")
      break
