n = 1000 - int(input())
lst = [500,100,50,10,5,1]
answer = 0

for i in lst:
  if n == 0:
    break
  if i <= n:
    answer += n//i
    n %= i

print(answer)
