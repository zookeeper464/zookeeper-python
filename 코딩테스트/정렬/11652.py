n = int(input())
dic = {}
for _ in range(n):
  i = int(input())
  try:
    dic[i] += 1
  except:
    dic[i] = 1

print(sorted(list(dic.items()), key = lambda x : (-x[1],x[0]))[0][0])
