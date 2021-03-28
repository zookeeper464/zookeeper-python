n = int(input())
lst = []
for i in range(n):
  lst.append(int(input()))
lst.reverse()
#주어진 입력값과 마지막 스테이지 부터 입력된 리스트 생성

answer = 0
for i in range(1,n):
  if lst[i-1] > lst[i]:
    pass
  else:
    answer += lst[i] - lst[i-1] + 1
    lst[i] = lst[i-1] -1
#앞에 숫자가 더 크면 더 작은 수 중 가장 큰수로 변경

print(answer)
