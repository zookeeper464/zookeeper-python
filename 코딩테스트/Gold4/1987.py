# n,m = map(int,input().split())
# lst = [list(input()) for _ in range(n)]
# data = [0 for _ in range(26)]
# dr,dc = [1,-1,0,0],[0,0,1,-1]
# answer, data[ord(lst[0][0])-65] = 1, 1

# def dfs(r,c,temp):
#   global answer
#   s = 0
#   for i in range(4):
#     nr,nc=r+dr[i],c+dc[i]
#     if 0<=nr<n and 0<=nc<m and data[ord(lst[nr][nc])-65] == 0:
#       data[ord(lst[nr][nc])-65] = 1
#       dfs(nr,nc,temp+1)
#       data[ord(lst[nr][nc])-65] = 0
#       s = 1
#   if s==0:
#     answer = max(answer,temp)

# dfs(0,0,1)
# print(answer)
#####################################################################

n,m = map(int,input().split())
lst = [list(input().rstrip('\n')) for _ in range(n)]

answer = 1
dr,dc = [1,-1,0,0],[0,0,1,-1]

def bfs(r, c):
  global answer
  q = set([(r,c,lst[r][c])])

  while q:
    r,c,ans = q.pop()
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<m and lst[nr][nc] not in ans:
        q.add((nr,nc,ans + lst[nr][nc]))
        answer = max(answer,len(ans)+1)

bfs(0,0)
print(answer)
