import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
answer = []
dic = {}
#기본 입력 변수 입력

for i in range(n):
  m = int(input())
  if m == 0:
    if h:
      temp = heapq.heappop(h)
      if dic[abs(temp)] == 0:
        answer.append(temp)
      else:
        answer.append(temp * (-1))
        dic[abs(temp)] -= 1
    #m이 0이고 h가 null이 아닐때, 출력 메커니즘

    else:
      answer.append(0)
    #m이 0이고 h가 null일때, 출력 메커니즘

  elif m > 0:
    heapq.heappush(h,m)
    try:
      dic[abs(m)] += 0
    except:
      dic[abs(m)] = 0
    #양수일때 입력 메커니즘

  else:
    heapq.heappush(h,abs(m))
    try:
      dic[abs(m)] += 1
    except:
      dic[abs(m)] = 1
    #음수일때 입력 메커니즘

for i in answer:
  print(i)
