n, l = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
#주어진 입력값 입력

temp = lst[0]
answer = 1
for i in range(len(lst)):
  if temp + l > lst[i]:
    pass
  else:
    answer += 1
    temp = lst[i]
#순서대로 정렬된 상태에서 테이프의 최대 길이 이내의 구멍은 하나로 막고 다른 구멍들은 새 테이프로 막는다.

print(answer)
