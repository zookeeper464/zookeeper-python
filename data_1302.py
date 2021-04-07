n = int(input())
dic = {}
for i in range(n):
  s = input()
  try:
    dic[s] += 1
  except:
    dic[s] = 1
#필요한 변수 입력

temp = 0
answer = []
for book,num in dic.items():
  if temp < num:
    answer = []
    temp = num
    answer.append(book)
  #검사한 책들보다 판매량이 높은 책이 있다면 답 변경

  elif temp == num:
    answer.append(book)
  #검사한 책들 가운데 판매량이 높은 책과 판매량이 같은 책이 있다면 답에 추가
  
#모든 책들에 대해 가장 판매량이 높은 책 검색

answer.sort()
print(answer[0])
