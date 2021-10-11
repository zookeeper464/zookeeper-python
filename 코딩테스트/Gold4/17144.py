n,m,t = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]

def find_machine ():
  global up,down
  for r in range(2,n-2):
    for c in range(m):
      if lst[r][c] == -1:
        up,down = [r,c],[r+1,c]
        return

up,down = None,None
find_machine()

def dust_move(r,c):
  temp = lst[r][c]
  num = temp//5

  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]
    if 0<=nr<n and 0<=nc<m and lst[nr][nc] != -1:
      temp -= num
      move_list[nr][nc] += num
  lst[r][c] = temp

def find_dust():
  for r in range(n):
    for c in range(m):
      if lst[r][c]>0:
        dust_move(r,c)

def rotation (r,c,looks,updown):
  mr = r
  for i in looks:
    while True:
      nr,nc = r+dr[i],c+dc[i]
      if updown:
        if 0<=nr<=mr and 0<=nc<m:
          if lst[nr][nc] != -1:
            if lst[r][c] != -1:
              lst[r][c] = lst[nr][nc]
              r,c = nr,nc
            else:
              r,c = nr,nc
          else:
            lst[r][c] = 0
            return
        else:
          break
      else:
        if mr<=nr<n and 0<=nc<m:
          if lst[nr][nc] != -1:
            if lst[r][c] != -1:
              lst[r][c] = lst[nr][nc]
              r,c = nr,nc
            else:
              r,c = nr,nc
          else:
            lst[r][c] = 0
            return
        else:
          break


def machine_work():
  global lst
  lst = [[lst[r][c]+ move_list[r][c] for c in range(m)] for r in range(n)]

  rotation(up[0],up[1],[1,2,0,3],True)
  rotation(down[0],down[1],[0,2,1,3],False)

for _ in range(t):
  move_list = [[0 for _ in range(m)] for _ in range(n)]
  find_dust()
  machine_work()
  
answer = 2
for r in range(n):
  answer += sum(lst[r])

print(answer)
