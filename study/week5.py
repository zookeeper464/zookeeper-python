# 1712
# a,b,c = map(int,input().split())
# if b<c: print(a//(c-b)+1)
# else: print(-1)

# 2292
# n = int(input())-1
# temp = 6
# answer = 1

# while n >0:
#   n -= temp
#   temp += 6
#   answer += 1
  
# print(answer)

# 1193
# n=int(input())
# i=1

# while n>i:
#   n-=i
#   i+=1

# if i%2==0:
#   print(f"{n}/{i+1-n}")
# else:
#   print(f"{i-n+1}/{n}")

# 2869
# a,b,v = map(int,input().split())
# print((v-b+-1)//(a-b)+1)

# 시간 초과 알고리즘
# a,b,v = map(int,input().split())
# answer = 0
# while True:
#   answer += 1 
#   v -= a
#   if v<=0:
#     break
#   v += b
# print(answer)

# 10250
# t = int(input())
# answer = []
# for _ in range(t):
#   r,c,n = map(int,input().split())
#   s1, s2 = (n-1)%r+1, (n-1)//r+1
#   answer.append(s1*100+s2)

# for a in answer:
#   print(a)

# 2775
# t = int(input())
# answer = []
# for _ in range(t):
#   n,k = int(input()), int(input())
#   lst = [i for i in range(k+1)]
#   for i in range(n):
#     temp = [0]
#     for i in range(1,k+1):
#       temp.append(temp[-1]+lst[i])
#     lst = temp
#   answer.append(lst[-1])

# for ans in answer:
#   print(ans)

# 2839
# n = int(input())
# for i in range(5):
#   if (n-3*i)%5==0:
#     print(i+(n-3*i)//5)
#     break
#   elif (n-3*i)<0:
#     print(-1)
#     break

# 10757
# print(sum(map(int,input().split())))

# 1011
# t = int(input())
# answer = []

# for _ in range(t):
#   x,y = map(int,input().split())
#   dist = (y-x)
#   day = 0

#   while dist>0:
#     day += 1
#     dist -= (day+1)//2

#   answer.append(day)

# for ans in answer:
#   print(ans)
