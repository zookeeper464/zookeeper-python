N=int(input())
lst=list(map(int,input().split()))
answer=[0]+[-1]*(N-1)
x=False

for i in range(N):
  if x:
    break
  for j in range(1,lst[i]+1):
    if i+j>=N:
      x=True
      break
    if answer[i] == (-1):
      break
    elif answer[i+j] == (-1) or answer[i+j]>answer[i]+1:
      answer[i+j]=answer[i]+1
      

print(answer[-1])
