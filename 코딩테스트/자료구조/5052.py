import sys
input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
  n = int(input())
  lst = []

  for _ in range(n):
    lst.append(input().rstrip('\n'))
  lst.sort()

  temp = 'YES'
  for i in range(n-1):
    if lst[i] == lst[i+1][:len(lst[i])]:
      temp = 'NO'
      break
  answer.append(temp)

for ans in answer:
  print(ans)
