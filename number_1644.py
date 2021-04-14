import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
plst = [1 for i in range(n+1)]
plst[0], plst[1] = 0, 0

lst = []
for i in range(2,n+1):
  if plst[i] == 1:
    lst.append(i)
    for j in range(2, (n)//i+1):
      plst[j * i] = 0
#소수들의 리스트를 생성하고 변수를 입력받는다.
      
answer = 0
temp = deque()
for i in lst:
  temp.append(i)
  if sum(temp) > n:
    while sum(temp) > n:
      temp.popleft()
  if sum(temp) == n:
    answer += 1
#연속된 소수들의 합을 n을 초과하지 않는 선에서 검색한다.

print(answer)
