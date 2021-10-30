# from bisect import bisect_left

# n = input()
# lst = list(map(int, input().split()))
# dp = []

# for i in lst:
#   idx = bisect_left(dp, i)
  
#   if len(dp) <= idx:
#     dp.append(i)
  
#   else:
#     dp[idx] = i

# print(len(dp))

n = int(input())
lst = list(map(int,input().split()))
dp, cnt = [lst[0]], 1

def bi_check(mn,mx,temp):
  while mx>=mn:
    mid = (mn+mx)//2

    if dp[mid]>=temp:
      mx = mid-1
    else:
      mn = mid+1

  return mn

for i in range(1,n):
  temp = lst[i]

  if dp[-1]<temp:
    dp.append(temp)
    cnt += 1
  elif dp[-1] == temp:
    pass
  
  else:
    if dp[0]>temp:
      dp[0] = temp
    else:
      t = bi_check(0,cnt-1,temp)
      if dp[t-1] != temp:
        dp[t] = temp

print(len(dp))
