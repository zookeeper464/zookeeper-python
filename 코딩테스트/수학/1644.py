from collections import deque

n = int(input())
plst = [1 for i in range(n+1)]
plst[0], plst[1] = 0, 0

lst = []
for i in range(2,n+1):
  if plst[i] == 1:
    lst.append(i)
    for j in range(2, (n)//i+1):
      plst[j * i] = 0

answer = 0
temp = deque()
for i in lst:
  temp.append(i)
  if sum(temp) > n:
    while sum(temp) > n:
      temp.popleft()
  if sum(temp) == n:
    answer += 1

print(answer)
