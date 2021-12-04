row,col,squ = [0]*9,[0]*9,[[0]*3 for _ in range(3)]
lst = [list(map(int,input().rstrip())) for _ in range(9)]
zeros = []

def dfs (cnt):
    global s,temp
    if s:
        return

    if cnt == z:
        s = True
        for idx,(r,c) in enumerate(zeros):
            lst[r][c] = temp[idx]

        return

    r,c = zeros[cnt]
    for i in range(1,10):
        if (row[r]>>(i-1))%2 or (col[c]>>(i-1))%2 or (squ[r//3][c//3]>>(i-1))%2:
            continue

        num = 1<<(i-1)
        row[r] += num
        col[c] += num
        squ[r//3][c//3] += num
        temp.append(i)
        dfs(cnt+1)
        temp.pop()
        row[r] -= num
        col[c] -= num
        squ[r//3][c//3] -= num

    return

for r in range(9):
    for c in range(9):
        temp = lst[r][c]
        if temp == 0:
            zeros.append([r,c])
            continue
    
        temp = 1<<(temp-1)
        row[r] += temp
        col[c] += temp
        squ[r//3][c//3] += temp

z,s = len(zeros), False
temp = []
dfs(0)

print()
for i in range(9):
    print(*lst[i],sep='')