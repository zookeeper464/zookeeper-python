# import sys
# inf = sys.maxsize

# n, m, b = map(int, input().split())
# table = [list(map(int, input().split())) for _ in range(n)]
# height = 0
# ans = inf
# start,end =inf,0
# for i in range(n):
#     for j in range(m):
#         if table[i][j] < start:
#             start = table[i][j]
#         if table[i][j] > end:
#             end = table[i][j]

# for i in range(start,end+1):
#     pl,mi = 0,0
#     for j in range(n):
#         for k in range(m):
#             if table[j][k] < i:
#                 mi += i-table[j][k]
#             else:
#                 pl += table[j][k]-i

#     if pl+b < mi:
#         continue
    
#     t = 2*pl+mi
#     if t <= ans:
#         ans = t
#         height = i

# print(ans, height)
#################################### pypy 밖에 통과 안됨