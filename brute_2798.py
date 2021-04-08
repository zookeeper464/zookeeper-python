n, m  = map(int,input().split())
lst = list(map(int,input().split()))
answer = 0
#변수 입력

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      temp = lst[i]+lst[j]+lst[k]
      #모든 경우의 수 계산

      if answer < temp and m >= temp:
        answer = temp
      #조건에 맞다면 최댓값 갱신

print(answer)
