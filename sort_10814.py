n = int(input())
dic = {}
# 변수 입력

for i in range(n):
  a,b = input().split()
  a = int(a)
  try:
    dic[a].append(b)
  except:
    dic[a] = [b]
#넣어야하는 변수들 딕셔너리에 처리해서 입력
    
temp = list(dic.keys())
temp.sort()
#출력해야 하는 나이 정렬

for age in temp:
  for i in dic[age]:
    print(age, i)
