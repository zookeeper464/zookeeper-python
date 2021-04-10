dic = {}
n = int(input())
for i in range(n):
  m = int(input())
  dic[m] = dic.get(m,0) + 1
#필요한 변수 입력

lst = []
for key, val in dic.items():
  lst.append([key,val])
#출력해야 하는 변수를 정렬하기 위한 변환

lst.sort(key = lambda x : (-x[1],x[0]))
#조건에 맞는 정렬

print(lst[0][0])
