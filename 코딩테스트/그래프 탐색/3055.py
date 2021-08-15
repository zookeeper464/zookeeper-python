  from collections import deque

n,m = map(int,input().split())
lst = [list(input()) for _ in range(n)]
water_q = deque()
q = deque()
for i in range(n):
  for j in range(m):
    if lst[i][j] == "*":
      water_q.append([i,j])
    elif lst[i][j] == "S":
      q.append([i,j])
dr,dc = [1,0,-1,0],[0,1,0,-1]

def time_rule (water_q,q,answer):
  while q:
    answer += 1
    for _ in range(len(water_q)):
      r,c = water_q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m:
          if lst[nr][nc] =="." or lst[nr][nc] =="S":
            water_q.append([nr,nc])
            lst[nr][nc] = "*"

    for _ in range(len(q)):
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m:
          if lst[nr][nc] ==".":
            q.append([nr,nc])
            lst[nr][nc] = "S"
          elif lst[nr][nc] =="D":
            return answer
  return "KAKTUS"

print(time_rule(water_q,q,0))

# from collections import deque

# r,c = map(int,input().split())
# lst = [list(input()) for _ in range(r)]

# hog = []
# water = []
# for i in range(r):
#   for j in range(c):
#     if lst[i][j] == 'S':
#       hog.append([i,j])
#       lst[i][j] = '.'
#     elif lst[i][j] == '*':
#       water.append([i,j])
      
# hog = deque(hog)
# water = deque(water)
# dr,dc = [1,-1,0,0],[0,0,1,-1]

# def water_move (water):
#   global lst
#   for _ in range(len(water)):
#     tr,tc = water.popleft()

#     for i in range(4):
#       nr,nc = tr+dr[i],tc+dc[i]
    
#       if 0<=nr<r and 0<=nc<c:
#         if lst[nr][nc] == '.':
#           lst[nr][nc] = '*'
#           water.append([nr,nc])

#   return water

# def hog_move (hog):
#   global answer
#   for _ in range(len(hog)):
#     tr,tc = hog.popleft()

#     for i in range(4):
#       nr,nc = tr+dr[i],tc+dc[i]
    
#       if 0<=nr<r and 0<=nc<c:
#         if lst[nr][nc] == '.':
#           hog.append([nr,nc])
#         elif lst[nr][nc] == 'D':
#           answer = cnt
#           return False

#   return hog

# answer = 'KAKTUS'
# cnt = 0
# while hog and water:
#   cnt += 1
#   water = water_move(water)
#   hog = hog_move(hog)

#   if answer != 'KAKTUS':
#     print(answer)
#     break

# if answer == 'KAKTUS':
#   print(answer)
