# import sys
# inf = sys.maxsize

# def check():
#   global dp
#   for r in range(1,n-1):
#     for c in range(m):
#       dt = 0
#       for k in range(m-c):
#         dt += mat[r][c+k]
#         if dp[r][c] < dp[r-1][c+k]+dt:
#           dp[r][c] = dp[r-1][c+k]+dt
      
#       dt = 0
#       for k in range(c,-1,-1):
#         dt += mat[r][k]
#         if dp[r][c] < dp[r-1][k]+dt:
#           dp[r][c] = dp[r-1][k]+dt
          
#   answer = -inf
#   dt = 0
#   for i in range(m-1,-1,-1):
#     dt += mat[-1][i]
#     if answer < dp[-1][i]+dt:
#       answer = dp[-1][i]+dt

#   return answer

# n,m = map(int,input().split())
# mat = [list(map(int,input().split())) for _ in range(n)]
# dr,dc = [1,0,0],[0,1,-1]
# dp = [[sum(mat[0][:i])for i in range(1,n+1)]]+[[0]*m for _ in range(n-2)]
# print(check())
############################################################################## dp에 대한 구조를 짜는 방법에도 여러가지 필요한 방식이 있다.
# 아래 방식은 시간이 훨씬 단축된다. 이유는 바로 옆의 데이터만 탐색하게끔 구조를 구축했기 때문이다. 위의 코드는 한줄의 데이터를 모두 탐색해야 하는 방법으로 비효율적이다.
import sys
inf = sys.maxsize

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-inf]*(m+2) for _ in range(n+1)] for _ in range(3)]
dp[0][1][0], dp[1][1][0], dp[2][1][0] = 0, 0, 0

for i in range(1, m+1):
  for k in range(3):
    dp[k][1][i] = dp[k][1][i-1] + mat[0][i-1]

for i in range(2, n+1):
  for j in range(1, m+1):
    dp[0][i][j] = max(dp[0][i][j], dp[0][i-1][j] + mat[i-1][j-1], dp[0][i][j-1] + mat[i-1][j-1])
    
  for j in range(m, -1, -1):
    dp[1][i][j] = max(dp[1][i][j], dp[1][i-1][j] + mat[i-1][j-1], dp[1][i][j+1] + mat[i-1][j-1])

  for j in range(1, m+1):
    dp[2][i][j] = max(dp[0][i][j], dp[1][i][j])
  
  dp[0][i] = dp[2][i]
  dp[1][i] = dp[2][i]

print(dp[2][n][m])
