n = int(input())%5
lst = list(map(int,input().split()))
answer = 0

for i in lst:
  if n == i%5:
    answer += 1

print(answer)
