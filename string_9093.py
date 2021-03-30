n = int(input())
answer = []
for i in range(n):
  l = input().split()
  for i in range(len(l)):
    l[i] = l[i][::-1]
  answer.append(" ".join(l))
#입력과 처리를 동시에

for i in answer:
  print(i)
