n,m,y,x,k = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
klst = list(map(int,input().split()))
dx, dy = [1,-1,0,0],[0,0,-1,1]
dice = [0 for _ in range(7)]

def switch (move):
  if move == 1:
    dice[1],dice[3],dice[4],dice[6] = dice[3],dice[6],dice[1],dice[4]
  elif move == 2:
    dice[1],dice[3],dice[4],dice[6] = dice[4],dice[1],dice[6],dice[3]
  elif move == 3:
    dice[1],dice[2],dice[5],dice[6] = dice[2],dice[6],dice[1],dice[5]
  else:
    dice[1],dice[2],dice[5],dice[6] = dice[5],dice[1],dice[6],dice[2]

for i in range(k):
  nx,ny = x+dx[klst[i]-1], y+dy[klst[i]-1]
  if 0<=ny<n and 0<=nx<m:
    x,y = nx,ny
    switch(klst[i])
    if lst[y][x] == 0:
      lst[y][x] = dice[1]
    else:
      dice[1], lst[y][x] = lst[y][x], 0
    print(dice[6])
