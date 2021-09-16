r,c = map(int,input().split())
n,m,d = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(r)]
answer = 1
lst[n][m] = 2
dr,dc = [-1,0,1,0],[0,1,0,-1]

def check(rr,cc,d):
  global answer
  for i in range(4):
    d = (d+3)%4
    nr,nc = rr+dr[d],cc+dc[d]
    if 0<=nr<r and 0<=nc<c and lst[nr][nc] == 0:
      lst[nr][nc] = 2
      return True, (nr,nc,d)
  
  return False, (rr-dr[d],cc-dc[d],d)

rr,cc = n,m
while 1:
  temp,t = check(rr,cc,d)
  rr,cc,d = t
  if temp:
    answer += 1
  if lst[rr][cc] == 1:
    break
    
print(answer)
