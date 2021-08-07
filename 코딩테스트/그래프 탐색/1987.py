r,c = map(int,input().split())
alpa = [0] * 26

def ord0(s):
  return ord(s)-ord("A")

mat = []
for _ in range(r):
  mat.append([ord0(x) for x in input()])

answer = 1
alpa[mat[0][0]] = 1
dr,dc = [0,0,1,-1], [1,-1,0,0]

neighbors = [[[] for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        for k in range(4):
            pr,pc = i + dr[k],j + dc[k]
            if pc in range(c) and pr in range(r):
                neighbors[i][j].append((pr,pc))

def dfs (tr,tc,d):
  global answer, alpa
  answer = max(answer,d)
  if answer == 26:
    pass
    
  for nr,nc in neighbors[tr][tc]:
    if alpa[mat[nr][nc]] == 0:
      alpa[mat[nr][nc]] = 1
      dfs(nr,nc,d+1)
      alpa[mat[nr][nc]] = 0



dfs(0,0,1)
print(answer)

# 현재 쓰여진 코드는 아직 많이 미숙하고 맨 마지막 과정이 빠져있다.
