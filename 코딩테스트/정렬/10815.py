n = int(input())
lst = list(map(int,input().split()))
m = int(input())
dic = dict()
temp = list(map(int,input().split()))
for i in temp:
  dic[i] = 0

for i in lst:
  if i in dic.keys():
    dic[i] += 1

for i in temp:
  print(dic[i], end = ' ')
