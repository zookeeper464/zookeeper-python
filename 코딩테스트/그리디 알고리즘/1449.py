n,l = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

last = 0
answer = 0
for i in lst:
  if last =< i:
    answer += 1
    last = i+l

print(answer)
