import sys
input = sys.stdin.readline

t = int(input())
answer = []

for i in range(t):
  n = int(input())
  dp = [0] * (n+1)
  #각 케이스에서 필요로 하는 요구 조건 입력

  for j in range(n):
    a, b = map(int, input().split())
    dp[a] = b
  #각 케이스에서 필요한 순위 입력

  min_n = dp[1]
  cnt = 1
  for k in range(2, n + 1):
    if dp[k] < min_n:
      min_n = dp[k]
      cnt += 1
    #각 케이스에서 자신보다 인덱스 또는 값이 작다면 더하기
  
  answer.append(cnt)

for i in answer:
  print(i)
