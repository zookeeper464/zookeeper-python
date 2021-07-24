n = int(input())
answer = 0
for i in range(5):
  if n%5==0:
    print(answer+n//5)
    break
  if n<0:
    print(-1)
    break
  answer += 1
  n -= 3
