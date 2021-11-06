n = int(input())
lst = list(map(int,input().split()))
dp = [lst[0]]

for i in range(1,n):
  temp = lst[i]
  if dp[-1] < temp:
    dp.append(temp)
    continue
  elif dp[-1] == temp:
    continue

  start, end = 0, len(dp)-1
  while start<=end:
    mid = (start+end)//2
    
    if dp[mid]>=temp:
      end = mid - 1
    else:
      start = mid + 1

  dp[start] = temp
  
print(len(dp))

#########################################
# from bisect import bisect_left

# n = int(input())
# lst = list(map(int, input().split()))
# dp = [lst[0]]

# for i in range(1,n):
#   temp = lst[i]
#   if dp[-1] < temp:
#     dp.append(temp)
#     continue
#   elif dp[-1] == temp:
#     continue

#   idx = bisect_left(dp,temp)
#   dp[idx] = temp
  
# print(len(dp))
