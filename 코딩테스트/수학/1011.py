t = int(input())
answer = []

for i in range(t):
  n, m = map(int,input().split())
  c = m-n
  count = 0
  num = 1
  while num<=c:
    num += 2**(count//2)
    count += 1
  answer.append(count)

for i in answer:
  print(i)
