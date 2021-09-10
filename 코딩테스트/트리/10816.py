n = int(input())
dic = {}
for i in input().split():
  try:
    dic[int(i)] += 1
  except:
    dic[int(i)] = 1
m = int(input())
print(*[dic[i] if i in dic else 0 for i in list(map(int,input().split()))])
