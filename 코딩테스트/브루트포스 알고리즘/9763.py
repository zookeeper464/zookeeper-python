import sys
inf = sys.maxsize

def check(num):
    global a,b
    if num < a:
        a,b = num,b
    elif num < b:
        b = num

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
answer = inf

for i in range(n):
    a,b = inf,inf
    x,y,z = lst[i]
    for j in range(n):
        if i==j:
            continue
        x1,y1,z1 = lst[j]
        temp = abs(x-x1)+abs(y-y1)+abs(z-z1)
        if answer<temp:
            continue
        check(temp)

    if answer > a+b:
        answer = a+b

print(answer)