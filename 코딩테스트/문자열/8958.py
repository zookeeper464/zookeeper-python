n = int(input())
answer = []
for _ in range(n):
  s = input()
  temp = 0
  num = 0
  for i in s:
    if i == "O":
      temp += 1
      num += temp
    else:
      temp = 0
  answer.append(num)

for ans in answer:
  print(ans)
