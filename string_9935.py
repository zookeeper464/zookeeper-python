import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()
lst = list(bomb)
m = len(bomb)
stack = []
#필요한 입력값 입력

for i in word:
  stack.append(i)
  if i == bomb[-1] and stack[-m:] == lst:
    del stack[-m:]
  #문자들을 더하면서 bomb과 같다면 제거 아니면 pass

if stack:
  print("".join(stack))
else:
  print("FRULA")
#word의 모든 문자가 제거되었으면 FRULA 출력
