n = int(input())

answer = []
for i in range(n):
  a, s = input().split()
  s = list(s)
  del s[int(a)-1]
  answer.append("".join(s))
  #입력 받은 값에서 원하는 부분 제거

for i in answer:
  print(i)
