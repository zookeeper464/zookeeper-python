n = int(input())
lst = [300,60,10]
if n%10 == 0:
  answer = [0] * 3
  for i in range(3):
    if n>=lst[i]:
      answer[i] = n//lst[i]
      n %= lst[i]
  print(' '.join(list(map(str,answer))))
else:
  print(-1)
