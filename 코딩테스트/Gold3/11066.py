# import sys
# inf = sys.maxsize

# answer = []
# t = int(input())

# for _ in range(t):
#   k = int(input())
#   f = list(map(int,input().split()))
  
#   dp = [[0]*k for _ in range(k)]
#   total = [f[0]]
#   for i in range(1,k):
#     total.append(f[i] + total[-1])
    
#   dp[0][1] = total[1]
#   for i in range(1,k-1):
#     dp[i][i+1] = total[i+1]-total[i-1]
    
#   for gap in range(2, k):
#     for i in range(k-gap):
#       dp[i][i + gap] = min([dp[i][j] + dp[j+1][i+gap] for j in range(i,i+gap)]) + total[i+gap]
#       if i != 0:
#         dp[i][i+gap] -= total[i-1]

#   answer.append(dp[0][k - 1])

# print(*answer, sep='\n')

############################################################################## 같은 내용 더 짧은 코드
answer = []
t = int(input())

for __ in range(t):
  k = int(input())
  page = list(map(int, input().split()))
  table=[[sum(page[i:j+1]) if i<j else 0 for j in range(k)] for i in range(k)]
  
  for d in range(2, k):
    for i in range(k-d):
      j = i+d
      minimum = [table[i][k] + table[k+1][j] for k in range(i, j)]
      table[i][j] += min(minimum)
      
  answer.append(table[0][k-1])

print(*answer,sep='\n')
