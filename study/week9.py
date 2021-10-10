# 10996
# n = int(input())

# print(f'{"* "*((n+1)//2)}\n{" *"*(n//2)}\n'*n)

# 1100
# lst = [list(input()) for _ in range(8)]
# answer = 0

# for r in range(8):
#   for c in range(8):
#     if (r+c)%2==0 and lst[r][c]=='F':
#       answer += 1

# print(answer)

# 2902
# lst =input().split('-')
# print(*[lst[i][0] for i in range(len(lst))], sep='')

# 1076
# colors = 'black,brown,red,orange,yellow,green,blue,violet,grey,white'.split(',')
# dic = {colors[i]:f'{i}' for i in range(10)}

# lst = [input() for _ in range(3)]
# answer = dic[lst[0]]+dic[lst[1]]+'0'*int(dic[lst[2]])
# print(answer)

# 10820
# import sys

# lst = sys.stdin.readlines()
# answer = []

# for s in lst:
#   temp = [0]*4
#   string = s.rstrip('\n')
#   for j in string:
#     o = (ord(j)-1)//10
#     if o == 3:
#       temp[3] += 1
#     elif o<6:
#       temp[2] += 1
#     elif o<9:
#       temp[1] += 1
#     else:
#       temp[0] += 1
#   answer.append(temp)

# for ans in answer:
#   print(*ans)

# def op (lst):
#   for s in lst:
#     print(s, ord(s))
# op(list(' 09AZaz'))

# 2750
# n = int(input())
# lst = sorted([int(input()) for _ in range(n)])
# print(*lst,sep='\n')

# 1924
# month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# x,y = map(int,input().split())
# num = y+sum(month[:x])
# print(day[(num)%7])

# 11719
# import sys

# s = sys.stdin.readlines()
# print(*s,sep='')

# 2748
# n = int(input())
# pibo = [0,1]
# for _ in range(1,n):
#   pibo.append(pibo[-1]+pibo[-2])
# print(pibo[n])

# 11050
# from math import comb
# n,k = map(int,input().split())
# print(comb(n,k))

# 위클리 챌린지2
# def check(num):
#   if num >= 90:
#     return 'A'
#   elif num >= 80:
#     return 'B'
#   elif num >= 70:
#     return 'C'
#   elif num >= 50:
#     return 'D'
#   else:
#     return 'F'

# def solution(scores):
#   answer = ''
#   n = len(scores)
#   for i in range(n):
#     num = [0,0]
#     min_score = max_score = scores[i][i]
#     score = 0

#     for j in range(n):
#       if j == i:
#         continue
#       score += scores[j][i]

#       if num[0] == 0 and scores[j][i]<=min_score:
#         num[0] = 1
#       if num[1] == 0 and scores[j][i]>=max_score:
#         num[1] = 1

#     if all(num):
#       score += scores[i][i]
#       score /= n
#     else:
#       score /= (n-1)
#     answer += check(score)

#   return answer

# scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
# '''
# [100,90,98 ,88,65],
# [50 ,45,99 ,85,77],
# [47 ,88,95 ,80,67],
# [61 ,57,100,80,65],
# [24 ,90,94 ,75,65]
# '''
# print(solution(scores))
