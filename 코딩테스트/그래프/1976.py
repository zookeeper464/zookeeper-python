from collections import deque
# 라이브러리 호출

n,m = int(input()), int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
st = list(map(int,input().split()))
# 입력값 처리

dp = [[] for _ in range(n)]
for i in range(n):
  for j in range(i+1,n):
    if lst[i][j] == 1:
      dp[i].append(j)
      dp[j].append(i)
# 연결된 노드 처리
q = deque([st[0]-1])
visited = [False for _ in range(n)]
visited[st[0]-1] = True
# 방문해야 하는 지역에 대한 기본 설정 처리

while q:
  temp = q.popleft()
  for i in dp[temp]:
    if not  visited[i]:
      visited[i] = True
      q.append(i)
    # 연결된 노드 중에서 연결되지 않은 노드 탐색

def check(lst):
  for i in lst:
    if visited[i-1]:
      pass
    else:
      return 'NO'
  return 'YES'
  # 모든 부분이 연결되어 있는지 탐색

print(check(st))
