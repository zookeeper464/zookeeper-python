n = int(input())
lst = list(map(int,input().split()))
ky = sorted(list(set(lst)))
dic = {}
for idx, i in enumerate(ky):
  dic[i] = idx

for i in lst:
  print(dic[i],end = ' ') 
