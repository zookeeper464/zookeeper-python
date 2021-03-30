t = int(input())
sol = []
for i in range(t):
  dic = {}
  n = int(input())
  for j in range(n):
    kinds, slot = input().split()
    #필요한 입력값 모두 입력

    try:
      dic[slot] += 1
    except:
      dic[slot] = 2
    #같은 저장소가 있다면 추가 아니면 새로 생성

  answer = 1
  for j in dic.keys():
    answer *= dic[j]
  #각 케이스별 경우의 수 계산
  
  sol.append(answer-1)

for i in sol:
  print(i)
