dic = {}
n = int(input())
temp = map(int,input().split())
for i in temp:
  try:
    dic[i] += 1
  except:
    dic[i] = 1

m = int(input())
lst = map(int,input().split())
for i in lst:
  try:
    print(dic[i], end = " ")
  except:
    print(0, end = " ")
