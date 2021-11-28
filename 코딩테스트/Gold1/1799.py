# from collections import deque

# n = int(input())
# chess = [list(map(int,input().split())) for _ in range(n)]
# rr = 0
# ll = 0
# x_list,y_list = [],[]
# for r in range(n):
#     for c in range(n):
#         if chess[r][c]:
#             x_list.append(c)
#             y_list.append(r)

# l = len(x_list)
# q = deque([[rr,ll,-1]])

# def check(q):
#     cnt = 0
#     while q:
#         temp = 0
#         for _ in range(len(q)):
#             tr,tl,num = q.popleft()
#             for i in range(num+1,l):
#                 idx1,idx2 = x_list[i]+y_list[i],(n-1)+x_list[i]-y_list[i]
#                 if (tr>>idx1)%2 or (tl>>idx2)%2:
#                     continue

#                 q.append([tr|(1<<idx1),tl|(1<<idx2),i])
#                 temp = 1

#         cnt += temp

#     return cnt

# print(check(q))

# n = int(input())
# chess = [list(map(int,input().split())) for _ in range(n)]
# x_list,y_list = [],[]
# for r in range(n):
#     for c in range(n):
#         if chess[r][c]:
#             x_list.append(c)
#             y_list.append(r)

# l = len(x_list)
# answer = 0
# def dfs(idx,rr,ll,cnt):
#     global answer

#     for i in range(idx+1,l):
#         idx1,idx2 = x_list[i]+y_list[i],(n-1)+x_list[i]-y_list[i]
#         if (rr>>idx1)%2 or (ll>>idx2)%2:
#             continue

#         dfs(i,rr|(1<<idx1),ll|(1<<idx2),cnt+1)
    
#     if cnt>answer:
#         answer = cnt

# dfs(-1,0,0,0)
# print(answer)
######################################################################## 틀린 코드들

n = int(input())
chess = [list(map(int,input().split())) for _ in range(n)]
white,black = [], []
for r in range(n):
    for c in range(n):
        if chess[r][c] == 1:
            if (r+c)%2:
                black.append([r,c])
            else:
                white.append([r,c])

def check(idx,rr,ll,cnt,lst):
    global temp
    l = len(lst)

    for i in range(idx+1,l):
        idx1,idx2 = lst[i][0]+lst[i][1],lst[i][0]+(l-1)-lst[i][1]
        if (rr>>idx1)%2 or (ll>>idx2)%2:
            continue

        check(i,rr|(1<<idx1),ll|(1<<idx2),cnt+1,lst)
    
    if cnt>temp:
        temp = cnt

answer = 0
temp = 0
check(-1,0,0,0,white)
answer += temp
temp = 0
check(-1,0,0,0,black)
answer += temp
print(answer)