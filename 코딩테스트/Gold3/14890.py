n,l = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
answer = 0

def check (temp,dp):
  c,num,cnt = 1,1,1
  while c<n:
    if temp == dp[c]:
      num = min(num+1,l)

    elif temp == dp[c]-1:
      if num == l:
        num = 1
        temp += 1
      else:
        return 0

    elif temp == dp[c]+1:
      if num >=0:
        num = 1-l
        temp -= 1
      else:
        return 0

    else:
      return 0
    c += 1

  if num >= 0:
    return 1
  else:
    return 0

for r in range(n):
  answer += check(lst[r][0],lst[r])
  
lst1 = list(zip(*lst))
for r in range(n):
  answer += check(lst1[r][0],lst1[r])
  
print(answer)
