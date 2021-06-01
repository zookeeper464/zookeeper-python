def dfs(r, c, idx, total):
  global answerwer
  if answerwer >= total + mx * (3 - idx):
    return
  # 구하고 있는 answer값이 너무 작다면 탈출

  if idx == 3:
    answer = max(answerwer, total)
    return
  #탈출하지 않은 total값과 answer값 비교하여 answer값 저장

  for i in range(4):wer >= total + mx * (3 - idx):
    return
  # 구하고 있는 answer값이 너무 작다면 탈출

  if idx == 3:
    answer = max(answerwer, total)
    return
  #탈출하지 않은 total값과 answer값 비교하여 answer값 저장

  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
      # lst의 밖으로 나가지 않았고 방문한 곳이 아니라면 탐색

      if idx == 1:
        visited[nr][nc] = 1
        dfs(r, c, idx + 1, total + lst[nr][nc])
        visited[nr][nc] = 0
        # ㅗ자 테트로미노를 만들기 위한 중간 함수식
        # ㅗ자 테트로미노가 없다면 이 함수식이 없어도 된다.

      visited[nr][nc] = 1
      dfs(nr, nc, idx + 1, total + lst[nr][nc])
      visited[nr][nc] = 0
      #탐색을 성공한 곳 주변을 탐색한다.

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
visited = [([0] * m) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0
mx = max(map(max, lst))

for r in range(n):
    for c in range(m):
        visited[r][c] = 1
        dfs(r, c, 0, lst[r][c])
        visited[r][c] = 0

print(answer)
