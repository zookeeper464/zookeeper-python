n = int(input())
lst = list(map(int,input().split()))
st = set(lst)
temp = list(st)
temp.sort()
dic = dict()
for idx,v in enumerate(temp):
  dic[v] = idx

for i in lst:
  print(dic[i], end = ' ')
