n,m = map(int,input().split())
lst = list(map(int,input().split()))
mx,mn = max(lst),0
dic = {}
for i in lst:
  try: dic[i] += 1
  except: dic[i] = 1

while mx>=mn:
  temp = (mx+mn)//2
  num = 0
  for i,v in dic.items():
    if i>temp:
      num += v*(i-temp)
  
  if num>m:
    mn = temp+1
  elif num<m:
    mx = temp-1
  else:
    break

print((mx+mn)//2)
