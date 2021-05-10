count = 1
answer = 1
check = 0
n = int(input())
while check < n-1 and n!=1:
  check += 6*count
  count += 1
  answer += 1

print(answer)
