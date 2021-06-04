lst = [0] + [list(map(int,list(input()))) for _ in range(4)]
top = [0 for _ in range(5)]

def turn (a, b):
  global visited
  temp = False
  if a>1 and visited[a-1]==0 and lst[a][(top[a]+6)%8]+lst[a-1][(top[a]+2)%8]==1:
    print('왼쪽', a)
    visited[a] += b
    turn(a-1,(-1)*b)
    temp = True
  if a<4 and visited[a+1]==0 and lst[a][(top[a]+2)%8]+lst[a+1][(top[a]+6)%8]==1:
    print("오른쪽", a)
    visited[a] += b
    turn(a+1,(-1)*b)
    temp = True
  top[a] = (top[a]+8-b)%8
  if not temp:
    visited[a] += b
    
print([8]+[lst[i][(top[i]+2)%8] for i in range(1,5)])
print([lst[i][(top[i]+6)%8] for i in range(1,5)])

k = int(input())
for _ in range(k):
  a, b = map(int,input().split())
  visited = [0 for _ in range(5)]
  turn(a,b)
  print(visited)
  print(top)
  print([8]+[lst[i][(top[i]+2)%8] for i in range(1,5)])
  print([lst[i][(top[i]+6)%8] for i in range(1,5)])

answer = 0
for i in range(1,5):
  answer += lst[i][top[i]]*(2**(i-1))

for i in lst:
  print(i)
print(answer)
