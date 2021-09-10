n = int(input())
lst = list(map(int,input().split()))
m = int(input())
mx,mn = max(lst),0

while mx>=mn:
  mid = (mx+mn)//2
  num = 0
  for i in lst:
    if i>mid:
      num += mid
    else:
      num += i
  
  if num>m:
    mx = mid-1
  else:
    mn = mid+1

print(mx)
