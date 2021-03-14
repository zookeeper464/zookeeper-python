n=int(input())
lst=list(map(int,input().split()))
answer=[lst[0]]
for i in range(1,n):
  temp=lst[i]
  for j in range(i):
    if temp<lst[j]+answer[-j-1]:
      temp=lst[j]+answer[-j-1]
  answer.append(temp)

print(answer[-1])
