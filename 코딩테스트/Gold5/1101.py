t = int(input())
answer = []

for _ in range(t):
  x,y = map(int,input().split())
  dist = y-x
  day = 0
  while dist>0:
    day += 1
    dist -= (day+1)//2
  
  answer.append(day)

print(*answer,sep='\n')
