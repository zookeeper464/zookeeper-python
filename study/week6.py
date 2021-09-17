# 1008
# a,b = map(int,input().split())
# print(a/b)

# 9498
# n = int(input())
# if n//10>8: print('A')
# elif n//10==8: print('B')
# elif n//10==7: print('C')
# elif n//10==6: print('D')
# else: print('F')

# 1330
# a,b = map(int,input().split())
# if a>b: print('>')
# elif a<b: print('<')
# else: print('==')

# 2753
# n = int(input())
# if n%4==0:
#   if n%100==0:
#     if n%400==0:
#       print(1)
#     else:
#       print(0)
#   else:
#     print(1)
# else:
#   print(0)

# 2588
# a,b = int(input()), int(input())
# print(a*(b%10))
# print(a*((b//10)%10))
# print(a*(b//100))
# print(a*b)

# 14681
# a,b = int(input()),int(input())
# if a>0:
#   if b>0:
#     print(1)
#   else:
#     print(4)
# else:
#   if b>0:
#     print(2)
#   else:
#     print(3)

# 10039
# answer = 0
# for i in range(5):
#   answer += max(8,int(input())//5)
# print(answer)

# 5543
# ham = min([int(input()) for _ in range(3)])
# drink = min(int(input()),int(input()))
# print(ham+drink-50)

# 10797
# n = int(input())
# print(sum([1 for i in list(map(int,input().split())) if n==i%5]))

# 2525
# h,m = map(int,input().split())
# ti = int(input())
# print((h+(m+ti)//60)%24,(m+ti)%60)

# 2752
# print(*sorted(list(map(int,input().split()))))

# 10162
# n = int(input())
# if n%10==0:
#   print(n//300, (n%300)//60, (n%60)//10)
# else:
#   print(-1)

# 2480
# a,b,c = map(int,input().split())
# dic = {i:0 for i in range(1,7)}
# for i in (a,b,c):
#   dic[i]+=1
# lst = sorted(list(dic.items()), key = lambda x : (-x[1],-x[0]))
# if lst[0][1]>1:
#   print(lst[0][0]*(10**lst[0][1])+10**(lst[0][1]+1))
# else:
#   print(lst[0][0]*100)

# 10156
# a,b,c = map(int,input().split())
# print(max(a*b-c,0))

# 2420
# a,b = map(int,input().split())
# print(abs(a-b))

# 2525
# h,m,s = map(int,input().split())
# ti = int(input())
# n = 3600*h+60*m+s+ti
# print((n//3600)%24,(n//60)%60,n%60)

# 5532
# from math import ceil
# l,a,b,c,d = [int(input()) for _ in range(5)]
# print(l-max(ceil(a/c),ceil(b/d)))

# 10101
# a,b,c = [int(input()) for _ in range(3)]
# if a+b+c == 180:
#   if a==b==c:
#     print('Equilateral')
#   elif a==b or b==c or c==a:
#     print('Isosceles')
#   else:
#     print('Scalene')
# else:
#   print('Error')

# 5596
# s = sum(list(map(int,input().split())))
# t = sum(list(map(int,input().split())))
# print(max(s,t))

# 10707
# a,b,c,d,e = [int(input()) for _ in range(5)]
# if c<e:
#   b+=d*(e-c)
# print(min(a*e,b))
