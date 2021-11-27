from collections import deque
import sys
input = sys.stdin.readline

def check(r,c):
    global answer,q
    if mat[r][c] == '.':
        q.append([r,c])
        mat[r][c] = '*'

    elif mat[r][c] == '$':
        answer += 1
        mat[r][c] = '*'
        q.append([r,c])

    elif mat[r][c] == '*':
        return False

    else:
        temp = ord(mat[r][c])
        mat[r][c] = '*'
        if temp<97:
            door[temp-65].append([r,c])
            return False
        else:
            lst[temp-97] = 1

    return True

t = int(input())
answers =[]
for _ in range(t):
    answer,q = 0,deque()
    h,w = map(int,input().split())
    mat = [list(input().rstrip()) for _ in range(h)]

    lst = [0] * 26
    key = input().rstrip()
    for k in key:
        if ord(k) < 90: 
            break
        lst[ord(k)-97] = 1
    
    door = [[] for _ in range(26)]
    for r in range(h):
        check(r,0)
        check(r,w-1)
    for c in range(1,w-1):
        check(0,c)
        check(h-1,c)
    
    dr,dc = [1,-1,0,0],[0,0,1,-1]
    while True:
        for i in range(26):
            if lst[i] == 0 or door == []:
                continue
            
            for _ in range(len(door[i])):
                r,c = door[i].pop()
                q.append([r,c])
                mat[r][c] = '*'

        for _ in range(len(q)):
            r,c = q.popleft()
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i]
                if 0<=nr<h and 0<=nc<w:
                    if check(nr,nc):
                        q.append([nr,nc])
        if q or sum([lst[i]*len(door[i]) for i in range(26)]):
            continue
        
        break

    answers.append(answer)

print(*answers,sep='\n')
