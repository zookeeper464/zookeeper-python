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
  s = 0
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
