import sys
inf = sys.maxsize

n = int(input())
lst = sorted(list(map(int,input().split())))
answer = inf
for idx in range(n-2):
    start,end = idx+1,n-1

    while start<end:
        temp = lst[idx]+lst[start]+lst[end]
        if abs(temp) < answer:
            ans = [idx,start,end]
            answer = abs(temp)
        if temp > 0:
            end -= 1
        else:
            start += 1
    
    if answer == 0:
        break

for i in ans:
    print(lst[i],end=' ')