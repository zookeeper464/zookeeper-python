n, m = int(input()), int(input())
start, end = 1, m

while start <= end:
  mid = (start + end) // 2
  temp = 0

  for i in range(1, n+1):
    temp += min(mid//i, n)
    
  if temp >= m:
    answer = mid
    end = mid - 1

  else:
    start = mid + 1
  print(start,mid,end,temp)
  
print(answer)
