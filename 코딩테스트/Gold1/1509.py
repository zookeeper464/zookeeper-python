import sys
sys.setrecursionlimit(10**6)
inf = sys.maxsize

s = input()
n = len(s)
mat = [[] for _ in range(n)]

def check(start,end):
    if start < 0 or end > n-1:
        return
    
    if s[start] == s[end]:
        mat[end].append(start)
        check(start-1,end+1)

def nums(idx):
    global dp
    if idx == -1:
        return 1

    if dp[idx] != inf:
        return dp[idx]+1
    
    for i in mat[idx]:
        dp[idx] = min(dp[idx],nums(i-1))

    return dp[idx]+1

for i in range(n):
    check(i,i+1)
    check(i,i)

dp = [inf]*n
nums(n-1)
print(dp[-1])