n = int(input())
dic = dict()
for _ in range(n):
  t = int(input())
  try: dic[t] += 1
  except: dic[t] = 1

lst = list(dic.items())
lst.sort(key = lambda x : (-x[1],x[0]))
print(lst[0][0])
