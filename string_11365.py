import sys
input = sys.stdin.readline

answer = []
while True:
  s = input().rstrip()
  if s == "END":
    break
  answer.append(s[::-1])
#END를 입력하면 탈출 아니면 거꾸로 출력

for a in answer:
  print(a)
