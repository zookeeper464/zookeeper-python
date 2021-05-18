h,m,s = map(int,input().split())
t = int(input())
temp = (s+t)//60
s = (s+t)%60
t = (m+temp)//60
m = (m+temp)%60
h = (h+t)%24
print(h, end=" ")
print(m, end=" ")
print(s)
