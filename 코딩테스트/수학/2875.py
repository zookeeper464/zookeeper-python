n,m,k = map(int,input().split())
num = min(n//2,m)
cnt = (k-(n+m-num*3)+2)//3
print(num-cnt)
