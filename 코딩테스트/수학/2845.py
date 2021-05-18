l,p = map(int,input().split())
lst = list(map(int,input().split()))
answer = []
num = l*p
for i in lst:
  answer.append(str(i-l*p))

print(" ".join(answer))
