n = int(input())
answer = []

for _ in range(n):
  s = input()
  num = 0
  for i in s:
    if i == "(":
      num += 1
    else:
      num -= 1
  
    if num < 0:
      break

  if num == 0:
    answer.append("YES")
  else:
    answer.append("NO")  

print("\n".join(answer))
