def dfs(idx,cnt,lst):
    global m 
    if cnt == m:
        check(lst)
        return

    for i in range(idx+1,c):
        lst.append(i)
        dfs(i,cnt+1,lst)
        lst.pop()

def check(lst):
    global answer
    temp = 0
    for i in range(h):
        temp += min(dp[j][i] for j in lst)

    if answer > temp:
        answer = temp


n,m = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
chicken,home = [],[]

for r in range(n):
    for c in range(n):
        if mat[r][c] == 1:
            home.append([r,c])
        elif mat[r][c] == 2:
            chicken.append([r,c])
c,h = len(chicken),len(home)
dp = [[] for _ in range(c)]

for i in range(c):
    a,b = chicken[i]
    for j in range(h):
        x,y = home[j]
        dp[i].append(abs(a-x)+abs(b-y))

answer = 4*(n**2)
for i in range(c):
    dfs(i,1,[i])

print(answer)