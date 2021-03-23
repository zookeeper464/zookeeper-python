dp = [[[0] * 21 for i in range(21)] for i in range(21)]
for i in range(21):
  for j in range(21):
    dp[0][i][j], dp[i][0][j], dp[i][j][0] = 1, 1, 1
# 주어진 조건에 대해 변형

def w (a,b,c):
  global dp
  if a * b * c < 0:
    return 1
  if dp[a][b][c] != 0:
    pass
  else:
    if a<b and b<c:
      dp[a][b][c] = w(a,b-1,c) - w(a,b,c-1) + w(a,b-1,c-1)
    else:
      dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
  return dp[a][b][c]
#주어진 함수를 dp에 맞게 계산도록 변형

lst = []
while True:
  a,b,c = map(int,input().split())
  if (a,b,c) ==(-1,-1,-1):
    break
  if a <= 0 or b <= 0 or c <= 0:
    lst.append([a,b,c,w(-1,-1,-1)])
  elif a > 20 or b > 20 or c > 20:
    lst.append([a,b,c,w(20,20,20)])
  else:
    lst.append([a,b,c, w(a,b,c)])
#입력값을 조건에 맞게 받기


for i in lst:
  print(f"w({i[0]}, {i[1]}, {i[2]}) = {i[3]}")
