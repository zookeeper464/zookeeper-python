cnt = 0
num = 101
for i in range(7):
  a = int(input())
  if a%2==1:
    cnt += a
    num = min(a,num)

if cnt == 0:
  print(-1)
else:
  print(cnt)
  print(num)
