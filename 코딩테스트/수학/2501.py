n, k = map(int,input().split())
cnt = 0
s = True
for i in range(1,n+1):
  if n%i==0:
    cnt += 1
  if cnt ==k:
    s = False
    break
if s:
  print(0)
else:
  print(i)
