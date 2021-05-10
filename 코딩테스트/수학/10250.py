t = int(input())
answer = []
for i in range(t):
  h,w,n = map(int,input().split())
  a= str((n-1)%h+1)
  if n//h+1>9:
    b = str(n//h+1)
  else:
    b = "0"+str(n//h+1)
  answer.append(a+b)

for i in answer:
  print(i)
