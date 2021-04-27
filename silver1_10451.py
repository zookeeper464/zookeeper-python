t = int(input())
answer = []
for _ in range(t):
  n = int(input())
  lst = list(map(int,input().split()))
  # 입력값 설정완료

  lst = [0] + lst
  visited = [False for i in range(n+1)]
  visited[0] = True
  cnt = 0
  #설정하기 좋은 변수로 변환

  for i in range(1,n+1):
    if not visited[i]:
    #순환마디가 만들어지지 않은 수에 대한 순환마디 탐색 시작
      cnt += 1
      temp = i
      while not visited[temp]:
        visited[temp] = True
        temp = lst[temp]
        #순환마디 탐색
        
  answer.append(cnt)

for i in answer:
  print(i)
