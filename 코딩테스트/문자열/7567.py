s = input()
temp = ''
answer = 0
for i in s:
  if i == temp:
    answer += 5
  else:
    answer += 10
  temp = i

print(answer)
