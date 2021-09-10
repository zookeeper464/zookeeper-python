k,n = map(int,input().split())
lst = [int(input()) for _ in range(k)]
mx,mn = max(lst),1

while mx>=mn:
  temp = (mx+mn)//2
  num = sum([i//temp for i in lst])
  
  if num > n-1:
    mn = temp+1
  elif num <= n-1:
    mx = temp-1
print(mx)
