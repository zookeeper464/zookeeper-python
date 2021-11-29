from math import comb

def check(n,m,k):
    global answer
    if k<=0:
        return
    if n+m==1:
        answer += 'a'*n+'z'*m
        return
    temp = comb(n+m-1,m)
    if temp<k:
        answer += 'z'
        check(n,m-1,k-temp)
    else:
        answer += 'a'
        check(n-1,m,k)

n,m,k = map(int,input().split())
if comb(m+n,n)<k:
    print(-1)

else:
    answer = ''
    check(n,m,k)
    print(answer)