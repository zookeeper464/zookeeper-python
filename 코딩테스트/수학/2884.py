h,m = map(int,input().split())

h, m = (h+24-1+m//45)%24, (15+m)%60
print(h,m)
