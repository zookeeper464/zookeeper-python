answer = []
while True:
  s = input()
  if s == '0':
    break
  n = len(s)//2
  ans = 'yes'
  for i in range(n):
    if s[i] != s[-i-1]:
      ans = 'no'
      break
  answer.append(ans)

for ans in answer:
  print(ans)
