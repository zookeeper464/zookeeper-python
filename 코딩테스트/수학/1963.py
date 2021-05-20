from collections import deque
import sys
input = sys.stdin.readline

e = [True for i in range(10000)]
for i in range(2, 10000):
  if e[i]:
    j = i * 2
    while j < 10000:
      e[j] = False
      j += i
#소수 리스트 생성[소수면 true 아니면 false]
      
def bfs(a, b):
  q = deque()
  q.append([a, 0])
  #처음 시작 소수와 변환하기 위해 필요한 값을 입력
  visit = [0 for i in range(10000)]
  visit[a] = 1
  #bfs를 실행하는데 처음 수를 1로 하여 시작한다.

  while q:
    num, cnt = q.popleft()
    #q중에서 가장 처음 받은 값과 변환하기 위해 필요한 수를 꺼낸다.

    if num == b:
      return cnt
    #꺼낸 값이 최종 값과 같으면 꺼낸 수를 출력

    if num < 1000:
      continue
    #꺼낸 값이 1000보다 작으면 넘김

    for i in [1, 10, 100, 1000]:
      n = num - num % (i * 10) // i * i
      #num의 각 자릿수를 0으로 만든 값은 하나씩 n으로 받는다.

      for j in range(10):
        if visit[n] == 0 and e[n]:
          visit[n] = 1
          q.append([n, cnt + 1])
        n += i
        #각 자릿수를 0~9까지 바꿔가면서 소수인지 확인하고 확인한 곳임을 체크, q에 얼마나 걸려서 도착했는지 입력

answer = []
t = int(input())
# 시험 횟수 입력

for i in range(t):
  a, b = map(int, input().split())
  #필요한 입력값 입력
  result = bfs(a, b)
  answer.append(result)

for i in answer:
  print(i)
