import sys
input = sys.stdin.readline

def check (x, y, r):
  global x1, y1, x2, y2
  temp = 0
  if (x-x1)**2 +(y-y1)**2 < r**2:
    temp = 1
  if (x-x2)**2 +(y-y2)**2 < r**2:
    if temp == 1:
      temp = 0
    else:
      temp = 1
  return temp
#두 점과 원의 관계가 동일하면 1 아니면 0으로 리턴

t = int(input())
sol = []
#변수 입력

for i in range(t):
  answer = 0
  x1, y1, x2, y2 = map(int,input().split())
  #두 점의 위치 입력
  
  
  n = int(input())
  for j in range(n):
    x, y, r = map(int,input().split())
    answer += check(x, y, r)
  sol.append(answer)
  #원들과 점들사이의 관계 확인과정 실행
  
for i in sol:
  print(i)
