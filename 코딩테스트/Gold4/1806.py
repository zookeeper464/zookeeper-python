n,s = map(int,input().split())
lst = list(map(int,input().split()))

def check (num,start,end,result):
  if num == s:
    return 1
  switch = 0

  while start != n:
    if num < s and end < n:
      num += lst[end]
      end += 1
    else:
      num -= lst[start]
      start += 1

    if num >= s:
      result = min(result, end-start)
      switch = 1
  
  if switch:
    return result
  else:
    return 0

print(check(lst[0],0,1,n))
