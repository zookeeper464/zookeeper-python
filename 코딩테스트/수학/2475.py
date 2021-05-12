lst = list(map(int,input().split()))
answer = 0
for i in lst:
  answer += i**2
  answer%=10

print(answer)
