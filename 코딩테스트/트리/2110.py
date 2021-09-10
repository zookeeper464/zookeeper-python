n,m = map(int,input().split())
lst = sorted([int(input()) for _ in range(n)])
mx,mn = max(lst),0

while mx>=mn:
  cnt = 1
  temp = lst[0]
  num = (mx+mn)//2
  for i in range(1,n):
    if lst[i] - temp >= num:
      cnt += 1
      temp = lst[i]
      if cnt == m:
        break
  
  if cnt < m:
    mx = num-1
  else:
    mn = num+1

print(mx)
