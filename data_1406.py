import sys
from collections import deque
input = sys.stdin.readline

s, m = input(), int(input())
temp1 = list(s.strip())
temp2 = deque()
n = len(s)
#기본 변수 설정

for i in range(m):
  temp = input()
  #입력값 설정

  if temp[0] == "L" and temp1:
    x = temp1.pop()
    temp2.appendleft(x)
  #커서 좌측이동

  elif temp[0] == "D" and temp2:
    x = temp2.popleft()
    temp1.append(x)
  #커서 우측이동

  elif temp[0] == "B" and temp1:
    temp1.pop()
  #문자 제거

  elif temp[0] == "P":
    temp1.append(temp[2])
  #문자 추가

print("".join(temp1+list(temp2)))
