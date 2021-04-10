n = int(input())
lst = list(set(map(int, input().split())))
lst.sort()
#리스트를 받아 정렬

for i in lst:
  print(i, end = " ")
