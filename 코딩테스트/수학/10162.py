n = int(input())
lst = ["0" for _ in range(3)]
if n%10==0:
  if n>=300:
    lst[0] = str(n//300)
    n %= 300
  if n>=60:
    lst[1] = str(n//60)
    n %= 60
  lst[2] = str(n//10)
  print(" ".join(lst))
else:
  print(-1)
