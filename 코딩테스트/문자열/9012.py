n = int(input())
answer = []
for _ in range(n):
  s = input()
  cnt = 0
  ans = 'YES'
  for i in s:
    if i == '(':
      cnt += 1
    else:
      cnt -= 1
      if cnt <0:
        ans = 'NO'
        break
  if cnt != 0:
    ans = 'NO'
  answer.append(ans)

for ans in answer:
  print(ans)
