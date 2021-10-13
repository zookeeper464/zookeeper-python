# n,m,h = map(int,input().split())
# lst = [[0]*(n-1) for _ in range(h)]
# visited = [[False]*(n-1) for _ in range(h)]
# answer = 300

# for _ in range(m):
#   a,b = map(int,input().split())
#   lst[a-1][b-1] = 1
#   if b<n-1:
#     lst[a-1][b] -= 1
#   if 1<b:
#     lst[a-1][b-2] -= 1

# print(*lst,sep='\n')

# def answer_check(lst,cnt):
#   global answer
#   if answer < cnt:
#     print('초과')
#     return True

#   temp = list(range(n))
#   for r in range(h):
#     for c in range(n-1):
#       if lst[r][c] == 1:
#         temp[c],temp[c+1] = temp[c+1],temp[c]
  
#   if temp == list(range(n)):
#     answer = cnt
#     print('성공')
#     return True
#   else:
#     print('실패')
#     return False

# def find_list(lst,cnt):
#   for r in range(h):
#     for c in range(n-1):
#       if lst[r][c] == 0 and not visited[r][c]:
#         lst[r][c] = 1
#         if c<n-2: lst[r][c+1] -= 1
#         if 0<c: lst[r][c-1] -= 1

#         visited[r][c] = True
        
#         if not answer_check(lst,cnt+1):
#           find_list(lst,cnt+1)

#         if cnt != 0:
#           visited[r][c] = False

#         lst[r][c] = 0
#         if c<n-2: lst[r][c+1] += 1
#         if 0<c: lst[r][c-1] += 1

# answer_check(lst,0)
# find_list(lst,0)

# print(answer if answer != 300 else -1)
########################################### 매우 틀린 테스트 코드 어디가 틀렸는지 확실히 모르지만 재귀함수 부분이 틀렸다.

n,m,h = map(int,input().split())
lst = [[0]*(n-1) for _ in range(h)]
visited = [[False]*(n-1) for _ in range(h)]
answer = 300

for _ in range(m):
  a,b = map(int,input().split())
  lst[a-1][b-1] = 1
  if b<n-1:
    lst[a-1][b] -= 1
  if 1<b:
    lst[a-1][b-2] -= 1


def answer_check(lst,cnt):
  global answer
  if answer < cnt:
    return True

  temp = list(range(n))
  for r in range(h):
    for c in range(n-1):
      if lst[r][c] == 1:
        temp[c],temp[c+1] = temp[c+1],temp[c]
  
  if temp == list(range(n)):
    answer = cnt
    return True
  else:
    return False

def find_list(sr,sc,lst,cnt):
  if cnt > 2:
    return
    
  for c in range(sc+1,n-1):
    if lst[sr][c] == 0:
      lst[sr][c] = 1
      if c<n-2: lst[sr][c+1] -= 1
      if 0<c: lst[sr][c-1] -= 1

      if not answer_check(lst,cnt+1):
        find_list(sr,c,lst,cnt+1)

      lst[sr][c] = 0
      if c<n-2: lst[sr][c+1] += 1
      if 0<c: lst[sr][c-1] += 1


  for r in range(sr+1,h):
    for c in range(n-1):
      if lst[r][c] == 0:
        lst[r][c] = 1
        if c<n-2: lst[r][c+1] -= 1
        if 0<c: lst[r][c-1] -= 1

        if not answer_check(lst,cnt+1):
          find_list(r,c,lst,cnt+1)

        lst[r][c] = 0
        if c<n-2: lst[r][c+1] += 1
        if 0<c: lst[r][c-1] += 1

answer_check(lst,0)
find_list(0,-1,lst,0)

print(answer if answer != 300 else -1)
