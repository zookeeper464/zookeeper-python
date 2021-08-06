from collections import deque

n = int(input())
h_list = set([0])
lst = []
for _ in range(n):
  temp = list(map(int,input().split()))
  lst.append(temp)
  h_list = h_list|set(temp)

h_list = list(h_list)
h_list.sort()
dr,dc = [0,1,0,-1], [1,0,-1,0]

def bfs(num,answer):
  global visited, lst
  cnt = 0
  
  for r in range(n):
    for c in range(n):
      if lst[r][c] > num and not visited[r][c]:
        cnt += 1
        q = deque([[r,c]])
        visited[r][c] = True
        
        while q:
          tr, tc = q.popleft()
          for i in range(4):
            nr,nc = tr+dr[i], tc+dc[i]
            if 0<=nr<n and 0<=nc<n:
              if lst[nr][nc]>num and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append([nr,nc])
                
  if answer > cnt:
    return answer 
  return cnt

answer = 0
for i in h_list:
  visited = [[False for _ in range(n)] for _ in range(n)]
  answer = bfs(i,answer)

print(answer)
