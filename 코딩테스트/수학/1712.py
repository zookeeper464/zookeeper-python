n,a,b = map(int,input().split())
coin = -n
answer = 0
if b-a>0:
  while coin<=0:
    answer += 1
    coin += (b-a)
  print(answer)
else:
  print(-1)
