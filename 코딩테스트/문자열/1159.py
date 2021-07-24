n = int(input())
lst = [0] * 26
for _ in range(n):
  s = input()[0]
  lst[ord(s)-97] += 1

answer = ''
for i in range(26):
  if lst[i] >= 5:
    answer += chr(i+97)

if answer:
  print(answer)
else:
  print('PREDAJA')
