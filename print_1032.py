n = int(input())
answer = list(input())
l = len(answer)
for i in range(n-1):
  temp = list(input())
  for j in range(l):
    if temp[j] == answer[j] or answer[j] == "?":
      pass
    else:
      answer[j] = "?"

print("".join(answer))
