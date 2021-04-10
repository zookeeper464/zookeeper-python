n = int(input())
answer = []
#필요한 변수 입력

for i in range(n):
  lst = list(map(int,input().split()))
  lst.sort()
  answer.append(lst[-3])
#정렬후 3번째 큰 수 입력

for i in answer:
  print(i)
