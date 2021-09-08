n = int(input())
lst = sorted([int(input()) for _ in range(n)],reverse=True)
answer = 0
for i in range(n):
  answer = max(answer,(i+1)*lst[i])

print(answer)
