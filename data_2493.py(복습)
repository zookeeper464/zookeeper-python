import sys

input = sys.stdin.readline
n = int(input())
tower = list(map(int, input().split()))
stack = []
answer = ["0"] * n

for i in range(n):
  t = tower[i]
  while stack and tower[stack[-1]] < t:
    stack.pop()
    #새로운 건물이 이전 스택들과 비교하여 크다면 이전 스택 제거

  if stack:
    answer[i] = str(stack[-1] + 1)
    #새로운 건물보다 큰 건물이 존재한다면 해당 건물의 인덱스 선택
  stack.append(i)
  #새로운 건물을 stack에 추가

print(' '.join(answer))
