n,a,b = map(int,input().split())
a,b = a-1,b-1
answer = 0

while a!=b:
  answer += 1
  a,b = a//2,b//2

print(answer)
