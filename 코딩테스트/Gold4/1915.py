# 2x2개씩 탐색하고 정사각형이면 1 아니면 0 으로 도출 새로운 행렬 생성 이후 반복 1이 없어지면 탐색 종료

# n,m = map(int,input().split())
# lst = [list(map(int,input())) for _ in range(n)]

# def check (n,m,lst):
#   cnt = 0
  
#   while True:
#     num = 0
#     temp_list = [[] for _ in range(n-1)]
#     for r in range(n-1):
#       for c in range(m-1):
#         if lst[r][c] == 1:
#           if lst[r][c]+lst[r+1][c]+lst[r][c+1]+lst[r+1][c+1] == 4:
#             temp_list[r].append(1)
#             num = 1
#           else:
#             temp_list[r].append(0)
#         else:
#           temp_list[r].append(0) 
    
#     if num == 0:
#       break

#     cnt += 1
#     m -= 1
#     n -= 1

#   return cnt**2

# print(check(n,m,lst))

################################# dp를 쓸 생각을 하지 못하고 모든 사각형에 대해서 탐색하려고 했다.

n,m = map(int,input().split())
lst = [[0]*(m+1)]
lst += [[0]+list(map(int,input())) for _ in range(n)]

def check (n,m,lst):
  cnt = 0
  for r in range(1,n+1):
    for c in range(1,m+1):
      if lst[r][c] == 1:
        lst[r][c] = min(lst[r][c-1],lst[r-1][c],lst[r-1][c-1]) + 1
        if cnt < lst[r][c]:
          cnt = lst[r][c]
  
  return cnt**2

print(check(n,m,lst))
