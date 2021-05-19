t = int(input())
answer = 0
for _ in range(t):
  a,b = map(int,input().split())
  answer += b%a
print(answer)
