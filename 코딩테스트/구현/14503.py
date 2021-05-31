n,m =map(int,input().split())
r,c,look = map(int,input().split())
dx, dy = [0,1,0,-1], [-1,0,1,0]
dp = [list(map(int, input().split())) for _ in range(n)]
#기본 설정값 입력

count = 1
dp[r][c] = 2

roll = 0
while True:
  if dp[r+dy[(look+3)%4]][c+dx[(look+3)%4]] != 0:
    look = (look+3)%4
    roll += 1
  #회전 관련 코드

    if roll == 4:
      if dp[r-dy[look]][c-dx[look]] != 1:
        r, c = r-dy[look], c-dx[look]
        roll = 0
      #회전이 끝나고 뒷쪽이 벽이 아니라면 후진
      else:
        break
      #벽이라면 탈출
  else:
    roll = 0
    look = (look+3)%4
    r, c = r + dy[look], c + dx[look]
    dp[r][c] = 2
    count += 1
  #왼쪽에 빈 공간이 있다면 왼쪽으로 전진, 청소

print(count)
