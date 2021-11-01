# R,C,M = map(int,input().split())
# lst = [[-1]*C for _ in range(R)]

# shark = []
# dr,dc = [-1,1,0,0], [0,0,1,-1]
# for i in range(M):
#   r,c,z,d,s = map(int,input().split())
#   r,c,d = r-1,c-1,d-1
#   if d < 2: z %= 2*R
#   else: z %= 2*C

#   shark.append([s,d,z])

#   if lst[r][c] != -1 and shark[lst[r][c]][0] < shark[i][0]:
#     lst[r][c] = i
#   elif lst[r][c] == -1:
#     lst[r][c] = i
# print(*list(zip(range(len(shark)),shark)),sep='\n')
# print(*lst,sep='\n')
# def move_shark(temp,r,c):
#   s,d,z = shark[temp]

#   if d == 0:
#     r -= z
#     if r < 0:
#       r = -r
#       if r >= R:
#         r = 2*(R-1)-r
        
#   elif d == 1:
#     r += z
#     if r >= R:
#       r = 2*(R-1)-r
#       if r < 0:
#         r = -r

#   elif d == 2:
#     c += z
#     if c >= C:
#       c = 2*(C-1)-c
#       if c < 0:
#         c = -c

#   elif d == 3:
#     c -= z
#     if c < 0:
#       c = -c
#       if c >= C:
#         c = 2*(C-1)-c

#   if lst[r][c] != -1 and shark[lst[r][c]][0] < s:
#     lst[r][c] = temp
#   elif lst[r][c] == -1:
#     lst[r][c] = temp

# def check():
#   for r in range(R):
#     for c in range(C):
#       if lst[r][c] != -1:
#         temp = lst[r][c]
#         lst[r][c] = -1
#         move_shark(temp,r,c)

# answer = 0
# for man in range(C):
#   for i in range(R):
#     if lst[i][man] !=-1:
#       answer += shark[lst[i][man]][0]
#       print(man,i,lst[i][man],shark[lst[i][man]])
#       lst[i][man] = -1
#       break
#   check()
#   print(*lst,sep='\n')

# print(answer)
############################################################### 입력받은 데이터는 맞는데 상어가 이동하는 부분에서 오류가 발생한다.
