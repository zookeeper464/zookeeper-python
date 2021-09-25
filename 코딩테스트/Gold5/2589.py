# from collections import deque 

# N,M = map(int,input().split())
# lst = [list(input()) for _ in range(N)]
# dr,dc = [1,-1,0,0],[0,0,1,-1]
# answer = 1

# def count1 (q):
#   cnt = -1
#   visited = [[False for _ in range(M)] for _ in range(N)]
#   r,c = q[0]
#   visited[r][c] = True

#   while q:
#     cnt += 1
#     for _ in range(len(q)):
#       r,c = q.popleft()
#       for i in range(4):
#         nr,nc = r+dr[i],c+dc[i]
#         if 0<=nr<N and 0<=nc<M and lst[nr][nc] == 'L' and not visited[nr][nc]:
#           q.append([nr,nc])
#           visited[nr][nc] = True
          
#   return cnt

# def check1():
#   global answer
#   for r in range(N):
#     for c in range(M):
#       if lst[r][c] == 'L':
#         num = 0
#         for i in range(4):
#           nr,nc = r+dr[i],c+dc[i]
#           if 0<=nr<N and 0<=nc<M and lst[nr][nc] == 'L':
#             num += 1
#         if num == 1:
#           cnt = count1(deque([[r,c]]))
#           answer = max(answer,cnt)

# def count2 (q,visited):
#   cnt = -1
#   r,c = q[0]
#   visited[r][c] = True

#   while q:
#     cnt += 1
#     for _ in range(len(q)):
#       r,c = q.popleft()
#       for i in range(4):
#         nr,nc = r+dr[i],c+dc[i]
#         if 0<=nr<N and 0<=nc<M and lst[nr][nc] == 'L' and not visited[nr][nc]:
#           q.append([nr,nc])
#           visited[nr][nc] = True

#   return [cnt, visited]

# def check2 ():
#   global answer
#   visited = [[False for _ in range(M)] for _ in range(N)]
#   for r in range(N):
#     for c in range(M):
#       if lst[r][c] == 'L' and not visited[r][c]:
#         num = 0
#         for i in range(4):
#           nr,nc = r+dr[i],c+dc[i]
#           if 0<=nr<N and 0<=nc<M and lst[nr][nc] == 'L':
#             num += 1
#         if num == 2:
#           cnt,visited = count2(deque([[r,c]]),visited)
#           answer = max(answer,cnt)

# check1()
# check2()
# print(answer)

################################################ 2인 경우또한 모두 탐색해야 한다.
from collections import deque 

N,M = map(int,input().split())
lst = [list(input()) for _ in range(N)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
answer = 0

def count1 (q):
  cnt = -1
  visited = [[False for _ in range(M)] for _ in range(N)]
  r,c = q[0]
  visited[r][c] = True

  while q:
    cnt += 1
    for _ in range(len(q)):
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<N and 0<=nc<M and lst[nr][nc] == 'L' and not visited[nr][nc]:
          q.append([nr,nc])
          visited[nr][nc] = True
          
  return cnt

def check1():
  global answer
  for r in range(N):
    for c in range(M):
      if lst[r][c] == 'L':
        num = 0
        for i in range(4):
          nr,nc = r+dr[i],c+dc[i]
          if 0<=nr<N and 0<=nc<M and lst[nr][nc] == 'L':
            num += 1
        if 0<num<=2 :
          cnt = count1(deque([[r,c]]))
          answer = max(answer,cnt)

check1()
print(answer)
