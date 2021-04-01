n = int(input())

answer = []
for i in range(n):
  s = list(input())
  s[0] = s[0].upper()
  answer.append("".join(s))
  #대문자로 변경 후 저장

for i in answer:
  print(i)
