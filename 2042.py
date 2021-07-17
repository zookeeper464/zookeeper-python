n,m,k = map(int,input().split())
lst = [0]
answer = []

for _ in range(n):
  t = int(input())
  lst.append(t)

print(lst)
for _ in range(m+k):
  a,b,c = map(int,input().split())
  if a == 1:
    lst[b] = c

  else:
    temp = 0
    for i in range(b,c+1):
      temp += lst[i]
    answer.append(temp)
  print(lst)

for ans in answer:
  print(ans)
