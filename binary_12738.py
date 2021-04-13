import sys
from bisect import bisect_left as bil
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
dp = [-1000000000]
#필요한 변수 입력

for i in lst:
  if dp[-1] < i:
    dp.append(i)
  else:
    dp[bil(dp,i)] = i
  #조건에 맞는 증가 수열 찾기
  
print(len(dp)-1)
