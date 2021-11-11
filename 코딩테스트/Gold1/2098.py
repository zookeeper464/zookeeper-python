# import sys
# inf = sys.maxsize

# def dfs(s,start,num,cnt):
#   global answer
#   if num > answer:
#     return

#   if cnt == N:
#     if num+lst[start][s] < answer:
#       answer = num+lst[start][s]
#     return

#   for i in range(N):
#     if visited[i]:
#       continue
    
#     visited[i] = 1
#     dfs(s,i,num+lst[start][i],cnt+1)
#     visited[i] = 0

# N = int(input())
# lst = [list(map(int,input().split())) for _ in range(N)]
# answer = inf

# for i in range(N):
#   visited = [0 if i!=j else 1 for j in range(N)]
#   dfs(i,i,0,1)

# print(answer)
########################################################### dfs를 활용한 알고리즘 시간초과
# dp를 활용하지 않았기 때문에 시간초과가 발생했다. dp를 활용하기 위해서 가장 좋은 방식은 index에 해당한는 값을 이진수로 나타내어 visited를 설정하고
# 해당 값 마다 dp를 설정하여 저장할 수 있도록 한다.

import sys
inf = sys.maxsize

def dfs(idx, visited):
  if visited == end:
    return lst[idx][0] if lst[idx][0] > 0 else inf

  if dp[idx][visited] > 0:
    return dp[idx][visited]

  tmp = inf
  for i in range(1, n):
    # 현재 위치와 이미 탐색한 위치는 넘어간다.
    # visited >> i 는 2~n까지 자리를 탐색하며 1인 부분을 찾는 과정이다.
    if (visited >> i)%2 == 1 or idx == i:
      continue

    # 현재 저정된 dp값과 지금 탐색한 비용에 대한 최솟값
    # visited|(1<<i)는 visited와 (1<<i) 중에서 탐색된 곳만 1로 설정하여 새롭게 이진수를 만드는 과정이다.
    # |는 or &는 and로써 활용할 수 있다.
    tmp = min(tmp, lst[idx][i] + dfs(i, visited|(1<<i)))

  # 탐색이 완료되었다면 갱신
  dp[idx][visited] = tmp
  return tmp

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(1<<n) for _ in range(n)] # 1 << n == 2*n
end = (1<<n)-1 # 2진수로 표현할 수 있는 경우의 수 - 1

print(dfs(0, 1))
