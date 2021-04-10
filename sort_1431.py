n = int(input())
lst = []
#필요한 변수 입력

for i in range(n):
  temp = input()
  m = len(temp)
  #문자의 길이 입력
  
  num = 0
  for j in temp:
    try:
      num += int(j)
    except:
      pass
  #문자에 포함된 숫자 입력
  
  lst.append([m,num,temp])

lst.sort(key = lambda x : (x[0],x[1],x[2]))
#조건에 해당하는 정렬

for i in lst:
  print(i[2])
