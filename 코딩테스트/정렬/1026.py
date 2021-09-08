n = int(input())
a,b = sorted(list(map(int,input().split()))),sorted(list(map(int,input().split())), reverse=True)
answer = 0

for i in range(n):
  answer += a[i]*b[i]

print(answer)
