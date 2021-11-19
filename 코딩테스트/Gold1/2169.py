# import sys
# inf = sys.maxsize

# def check():
#   global dp
#   for r in range(1,n-1):
#     temp = [-inf]*m
#     for c in range(m):
#       dt = 0
#       for k in range(m-c):
#         dt += mat[r][c+k]
#         if temp[c] < dp[c+k]+dt:
#           temp[c] = dp[c+k]+dt
      
#       dt = 0
#       for k in range(c,-1,-1):
#         dt += mat[r][k]
#         if temp[c] < dp[k]+dt:
#           temp[c] = dp[k]+dt
          
#     dp = temp[:]

#   answer = -inf
#   dt = 0
#   for i in range(m-1,-1,-1):
#     dt += mat[-1][i]
#     if answer < dp[i]+dt:
#       answer = dp[i]+dt

#   return answer

# n,m = map(int,input().split())
# mat = [list(map(int,input().split())) for _ in range(n)]
# dr,dc = [1,0,0],[0,1,-1]
# dp = [sum(mat[0][:i])for i in range(1,n+1)]
# print(check())
############################################################################## 완전탐색 -> 실패(시간초과)
