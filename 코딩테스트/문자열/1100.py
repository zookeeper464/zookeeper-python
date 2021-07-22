lst = []
for i in range(8):
  lst.append(list(input()))

answer = 0
for i in range(8):
  for j in range(i%2,8,2):
    if lst[i][j] == 'F':
      answer += 1

print(answer)
