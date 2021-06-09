s = input()
x = "aeiou"
answer = 0
for i in s:
  if i in x:
    answer += 1

print(answer)
