import sys
import heapq

input = sys.stdin.readline
#시간 절약

q = []
answer = []
n = int(input())
for i in range(n):
  a = int(input())
  if a == 0:
  #입력 값이 0일때
    if q:
      answer.append(heapq.heappop(q))
      #저장값이 존재한다면 가장 작은 입력값 출력

    else:
      answer.append(0)
      #저장값이 없다면 0출력

  else:
    heapq.heappush(q, a)
    #입력값이 0이 아니면 새롭게 저장
    
for i in answer:
  print(i)
