import sys
input = sys.stdin.readline

def check(num):
    start,end = 0,len(dp)
    while start<=end:
        mid = (start+end)>>1
        if dp[mid]<num:
            start = mid+1
        else:
            end = mid -1
            
    return start

n = int(input())
lst = list(map(int, input().split()))
record = [0] * n
dp = [lst[0]]
record[0] = 1

for i in range(1, n):
    if dp[-1] < lst[i]:
        dp.append(lst[i])
        record[i] = len(dp)
    else:
        idx = check(lst[i])
        dp[idx] = lst[i]
        record[i] = idx + 1

ans = []
l = len(dp)
for i in range(len(record)-1,-1,-1):
    if record[i] == l:
        ans.append(lst[i])
        l -= 1

    if l < 1:
        break

print(len(ans))
print(*ans[::-1])