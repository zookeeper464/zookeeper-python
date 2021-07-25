n,m = map(int,input().split())
lst = []
for i in range(n):
  temp = int(input())
  if temp <= m:
    lst.append(temp)

answer = 0
while m != 0:
  coin = lst.pop()
  num = m//coin
  answer += num
  m -= coin*num
  
print(answer)
