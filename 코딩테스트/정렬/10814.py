n = int(input())
dic = dict()
for _ in range(n):
  a,b = input().rstrip().split()
  a = int(a)
  if a in dic.keys():
    dic[a].append(b)
  else:
    dic[a] = [b]

lst = sorted(list(dic.keys()))
for i in lst:
  for j in dic[i]:
    print(i,j)
