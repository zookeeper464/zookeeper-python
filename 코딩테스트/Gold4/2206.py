from collections import deque

n,m = map(int,input().split())
lst = [list(map(int,list(input()))) for _ in range(n)]
q = deque([[0,0,0]])
dr,dc = [1,-1,0,0],[0,0,1,-1]
visited = [[(0,2) for _ in range(m)] for _ in range(n)]
visited[0][0]= (1,0)

def check (q):
  cnt = 1

  if n==1 and m==1:
    return 1
  
  while q:
    cnt += 1
    for _ in range(len(q)):
      r,c,v = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m:
          temp = v+lst[nr][nc]
          if temp<visited[nr][nc][1]:
            visited[nr][nc] = (cnt,temp)
            q.append([nr,nc,temp])
            if (nr,nc) == (n-1,m-1):
              return cnt
  return -1

print(check(q))
