n,m = map(int,input().split())
answer = 1
while n < m:
  if m%2 == 0:
    m //= 2
    answer += 1
  else:
    if m%10 == 1:
      m //= 10
      answer += 1
    else:
      answer = -1
      break

if n==m:
  print(answer)
else:
  print(-1)
