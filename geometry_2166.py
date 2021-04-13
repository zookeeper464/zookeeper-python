import sys
input = sys.stdin.readline

n = int(input())
lst = []
answer = 0
for i in range(n):
  x, y = map(int,input().split())
  lst.append([x,y])
  #필요한 변수 입력

def tra (m):
  global lst, answer
  x1 = lst[m][0] - lst[0][0]
  x2 = lst[m+1][0] - lst[0][0]
  y1 = lst[m][1] - lst[0][1]
  y2 = lst[m+1][1] - lst[0][1]
  temp = 0.5 * (x1 * y2 - x2 * y1)
  answer += temp
  #오목함과 볼록함을 따지면서 삼각형으로 나누어 넓이 계산
  
for i in range(1,n-1):
  tra(i)
  #나누어진 삼각형들의 넓이 합계산
  
answer = abs(answer)
#최종적으로 절댓값처리

print(answer)
