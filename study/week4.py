# 11654
# print(ord(input()))


# 11720
# input()
# print(sum(list(map(int,list(input())))))

# 10809
# s = input()
# lst = [-1]*26
# for idx,v in enumerate(s):
#   if lst[ord(v)-97] == -1:
#     lst[ord(v)-97] = idx

# for i in lst:
#   print(i, end= ' ')

# 2675
# t = int(input())
# answer = []
# for _ in range(t):
#   n, s = input().split()
#   n = int(n)
#   ans = ''
#   for i in s:
#     ans += i*n
#   answer.append(ans)

# for ans in answer:
#   print(ans)

# 1157
# s = input().upper()
# lst = [[0,i] for i in range(65,91)]
# for i in s:
#   lst[ord(i)-65][0] += 1

# lst.sort(reverse=True)
# if lst[0][0] == lst[1][0]:
#   print('?')
# else:
#   print(chr(lst[0][1]))

# 1152
# print(len(input().split()))

# 2908
# a,b = input().split()
# a, b = int(a[::-1]), int(b[::-1])
# print(max(a,b))

# 5622
# s = input()
# answer = 0

# for i in s:
#   if i in 'ABC':
#     answer += 3
#   elif i in 'DEF':
#     answer += 4
#   elif i in 'GHI':
#     answer += 5
#   elif i in 'JKL':
#     answer += 6
#   elif i in "MNO":
#     answer += 7
#   elif i in 'PQRS':
#     answer += 8
#   elif i in 'TUV':
#     answer += 9
#   elif i in 'WXYZ':
#     answer += 10

# print(answer)

# 2941
# s = input()
# n = len(s)
# for i in range(1,n):
#   if s[i] == '-' and s[i-1] in 'cd':
#     n -= 1
#   elif s[i] == '=' and s[i-1] in 'czs':
#     if s[i-1] == 'z' and i>1 and s[i-2]=='d':
#       n-= 1
#     n-=1
#   elif s[i] == 'j' and s[i-1] in 'ln':
#     n -= 1

# print(n)

# 1316
# def check (s):
#   st = set()
#   temp = s[0]
#   for i in s:
#     if i not in st:
#       st.add(i)
#       temp = i
#     elif temp == i:
#       pass
#     else:
#       return 0
#   return 1

# n = int(input())
# answer = 0

# for _ in range(n):
#   s = input()
#   answer += check(s)

# print(answer)
