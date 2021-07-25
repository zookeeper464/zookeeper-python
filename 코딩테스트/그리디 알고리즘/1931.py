n = int(input())
lst = []

for _ in range(n):
  a, b = map(int,input().split())
  lst.append((a,b))

lst.sort(key = lambda x : (x[1],x[0]))
temp = 0
answer = 0

for i in lst:
  if i[0] >= temp:
    temp = i[1]
    answer += 1

print(answer)
