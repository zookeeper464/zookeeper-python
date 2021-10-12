n = int(input())
lst = [[0]*101 for i in range(101)]
dr,dc = [0,-1,0,1],[1,0,-1,0]

def draw (r,c,d,g):
  lst[r][c] = 1
  temp = [d]
  q = [d]
  for _ in range(g + 1):
    for k in q:
      r += dr[k]
      c += dc[k]
      lst[r][c] = 1
    q = [(i + 1) % 4 for i in temp]
    q.reverse()
    temp = temp + q


for i in range(n):
  x, y, d, g = map(int, input().split())
  draw(y,x,d,g)

result = 0
for i in range(100):
  for j in range(100):
    if all([lst[i][j],lst[i][j+1],lst[i+1][j],lst[i+1][j+1]]):
      result += 1

print(result)
