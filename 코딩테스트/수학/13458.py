n = int(input())
lst = list(map(int,input().split()))
b,c = map(int,input().split())
answer = 0

for i in lst:
  count = 1
  temp = i-b-1
  if temp <0:
    pass
  else:
    count += temp//c+1
  answer += count
  
print(answer)
