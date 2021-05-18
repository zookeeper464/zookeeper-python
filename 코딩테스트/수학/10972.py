#입력값 입력
n = int(input())
lst = list(map(int,input().split()))
s = False

#숫자를 키우기 위한 자리가 있는지 탐색
for i in range(n-1,0,-1):
  if lst[i-1]<lst[i]:
    s = True
    break
    
#숫자가 존재하는지 판별
if s:
  #숫자가 존재한다면 그 자리 다음에 나오는 수 중에서 그 수 다음으로 큰 수 탐색
  for j in range(n-1,i-1,-1):
    if lst[i-1]<lst[j]:
      break
  # 두 수의 자리를 바꾼다.
  lst[i-1], lst[j] = lst[j], lst[i-1]
  
  #바꾼뒤, 올라간 자리 이후를 오름차순으로 정렬한다.
  lst = lst[:i]+sorted(lst[i:])
  print(" ".join(list(map(str,lst))))
else:
  #숫자가 없다면 -1을 출력한다.
  print(-1)
