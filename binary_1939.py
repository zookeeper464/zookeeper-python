# from collections import deque
# import sys
# inf = sys.maxsize

# n,m = map(int,input().split())
# lst = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     lst[a].append([c,b])
#     lst[b].append([c,a])

# dp = [0]*(n+1)
# start,end = map(int,input().split())
# dp[start] = inf
# q = deque(lst[start])
# while q:
#     v,e = q.popleft()
#     if dp[e] >= v:
#         continue

#     dp[e] = v
#     for c,b in lst[e]:
#         if dp[b] >= min(v,c):
#             continue
#         q.append([min(c,v),b])
# print(dp[end])
################################## 메모리 초과
# 데이터를 q를 활용하여 메모리 초과가 된 모양, dp를 활용해서 그런 것이기 때문에 이를 사용하지 않는 방법을 찾아보면 좋겠다.
from collections import deque
import sys
input = sys.stdin.readline

def bfs(mid):
    visit[i1] = 1
    q = deque()
    q.append(i1)
    while q:
        start = q.popleft()
        if start == i2: return True
        for nx, nc in s[start]:
            if visit[nx] == 0 and mid <= nc:
                q.append(nx)
                visit[nx] = 1
    return False

n, m = map(int, input().split())
s = [[] for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])

i1, i2 = map(int, input().split())
low, high = 1, 1000000000

while low <= high:
    visit = [0 for i in range(n + 1)]
    mid = (low + high) // 2
    if bfs(mid): low = mid + 1
    else: high = mid - 1
    
print(high)
# 답을 찾아낸 풀이법 단순하게 bfs를 통해 통과되는 중량을 찾아내는 방식
# 길이가 제한되어 있는 것을 이용하여 제한된 길이의 길을 계속해서 찾아내는 방식이다.
# 무게를 찾아야 하므로 이를 이분탐색을 활용하여 탐색한다.
