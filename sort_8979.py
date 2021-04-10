n, m = map(int,input().split())
lst = []
for i in range(n):
  temp = list(map(int,input().split()))
  le = temp[1:]
  if temp[0] == m:
    answer = le
  lst.append(le)
#필요한 변수 입력
  
sol = 0
for le in lst:
  if le[0] > answer[0]:
    sol += 1
  elif le[0] == answer[0]:
    if le[1] > answer[1]:
      sol += 1
    elif le[1] == answer[1]:
      if le[2] > answer[2]:
        sol += 1
#조건에 맞는 더 많은 메달을 가진 사람 수
        
print(sol+1)
