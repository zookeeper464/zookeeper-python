# 15552
# import sys
# input = sys.stdin.readline

# n = int(input())
# answer = []
# for _ in range(n):
#   a,b = map(int,input().split())
#   answer.append(a+b)
  
# print(*answer, sep= '\n')

# 2798
# n,m = map(int,input().split())
# lst = list(map(int,input().split()))
# answer = 0

# for i in range(n-2):
#   for j in range(i+1,n-1):
#     for k in range(j+1,n):
#       card = lst[i]+lst[j]+lst[k]
#       answer = max(answer,card)

# print(answer)

# 2920
# lst = list(map(int,input().split()))

# if lst == list(range(1,9)):
#   print('ascending')
# elif lst == list(range(8,0,-1)):
#   print('descending')
# else:
#   print('mixed')

# 11721
# s = input()
# for i in range(0,len(s),10):
#   print(s[i:i+10])

# 10870
# n = int(input())
# lst = [0,1]
# for _ in range(1,n):
#   lst.append(lst[-1]+lst[-2])

# print(lst[n])

# 2231-1
# n = int(input())

# def check():
#   for a1 in range(10):
#     for a2 in range(10):
#       for a3 in range(10):
#         for a4 in range(10):
#           for a5 in range(10):
#             for a6 in range(10):
#               temp = a1*100001+a2*10001+a3*1001+a4*101+a5*11+a6*2
#               if temp == n:
#                 return a1*100000+a2*10000+a3*1000+a4*100+a5*10+a6*1
#   return 0

# print(check())

# 2231-2
# s = input()
# l = len(s)
# n = int(s)
# answer =0

# for i in range(max(0,n-54), n+1):
#   num = i+sum(map(int,str(i)))
#   if num == n:
#     answer = i
#     break

# print(answer)

# 2775
# t = int(input())
# answer = []

# for _ in range(t):
#   k,n = int(input()), int(input())
#   lst = list(range(1,n+1))

#   for _ in range(k):
#     for i in range(1,n):
#       lst[i] += lst[i-1]

#   answer.append(lst[-1])

# print(*answer,sep='\n')

# 2309
# lst = [int(input()) for _ in range(9)]
# num = sum(lst) - 100

# def check ():
#   for i in range(8):
#     for j in range(i+1,9):
#       if lst[i]+lst[j] == num:
#         llst = [lst[k] for k in range(9) if k not in (i,j)]
#         return sorted(llst)

# print(*check(),sep='\n')

# 10953
# t = int(input())
# answer = []

# for _ in range(t):
#   a,b = map(int,input().split(','))
#   answer.append(a+b)

# print(*answer,sep='\n')

# 5585
# coin = [500,100,50,10,5,1]
# n = 1000-int(input())
# answer = 0

# for c in coin:
#   answer += n//c
#   n %= c

# print(answer)

# 15719
# 정렬되지 않은 상태로 입력받을 수 있는 경우가 없다.

# 10093
# m,M = sorted(list(map(int,input().split())))

# if m == M:
#   print(0, '\n')
# else:
#   print(M-m-1)
#   print(*list(range(m+1,M)))

# 13458
# from math import ceil

# n = int(input())
# a_list = list(map(int,input().split()))
# b,c = map(int,input().split())
# answer = 0

# for i in range(n):
#   main = 1
#   sub = max(0,ceil((a_list[i]-b)/c))
#   answer += main+sub

# print(answer)

# 1673
# import sys

# def check (n,k):
#   num = n
#   while True:
#     temp = num//k
#     n += temp
#     num = (num%k)+temp
#     if temp == 0:
#       break
#   return n

# lst = sys.stdin.readlines()
# for l in lst:
#   n,k = map(int,l.split())
#   print(check(n,k))

# 1173
# N,m,M,T,R = map(int,input().split())
# answer,pulse = 0,m

# while N>0:
#     if m + T > M:
#         break
#     if pulse + T <= M:
#         pulse += T
#         N -= 1
#     else:
#         pulse = max(pulse - R, m)

#     answer += 1

# print(answer if 0 == N else -1)

# 위클 1주차
# def solution(price, money, count):
#     total = price*(count*(count+1)//2)
#     remain = money - total
#     answer =  -min(0,remain)
    
#     return answer
