n,m = map(int,input().split())
answer = []

dic = dict()
for _ in range(n):
  s = input()
  dic[s] = 1

for _ in range(m):
  s = input()
  if s in dic:
    answer.append(s)

answer.sort()
print(len(answer))
for ans in answer:
  print(ans)
