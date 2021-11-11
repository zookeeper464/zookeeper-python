import sys
inf = sys.maxsize

def dfs(s,start,num,cnt):
  global answer
  if num > answer:
    return

  if cnt == N:
    if num+lst[start][s] < answer:
      answer = num+lst[start][s]
    return

  for i in range(N):
    if visited[i]:
      continue
    
    visited[i] = 1
    dfs(s,i,num+lst[start][i],cnt+1)
    visited[i] = 0

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
answer = inf

for i in range(N):
  visited = [0 if i!=j else 1 for j in range(N)]
  dfs(i,i,0,1)

print(answer)
########################################################### dfs를 활용한 알고리즘 시간초과
