n = input()
l = len(n)
n = int(n)
m = int(input())
st = set(map(str,list(range(10)))) - set(input().split())
answer = abs(n-100)

for i in range(1000001):
  if not set(str(i))-st:
    answer = min(answer,len(str(i))+abs(n-i))

print(answer)
