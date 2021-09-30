n,m,r,c,k = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
move = list(map(int,input().split()))
dr,dc = [0,0,-1,1],[1,-1,0,0]
dice = [0 for _ in range(7)]

def switch (move):
  if move == 1:
    dice[1],dice[3],dice[4],dice[6] = dice[4],dice[1],dice[6],dice[3]
  elif move == 2:
    dice[1],dice[3],dice[4],dice[6] = dice[3],dice[6],dice[1],dice[4]
  elif move == 3:
    dice[1],dice[2],dice[5],dice[6] = dice[2],dice[6],dice[1],dice[5]
  else:
    dice[1],dice[2],dice[5],dice[6] = dice[5],dice[1],dice[6],dice[2]

for i in range(k):
  nr,nc = r+dr[move[i]-1], c+dc[move[i]-1]
  if 0<=nr<n and 0<=nc<m:
    r,c = nr,nc
    switch(move[i])
    if lst[r][c] == 0:
      lst[r][c] = dice[1]
    else:
      dice[1], lst[r][c] = lst[r][c], 0
    print(dice[6])
