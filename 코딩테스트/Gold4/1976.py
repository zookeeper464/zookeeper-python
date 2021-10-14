n,m = int(input()), int(input())
lst = [[] for _ in range(n+1)]
for i in range(1,n+1):
  temp = [0]+list(map(int,input().split()))
  for j in range(1,n+1):
    if temp[j]:
      lst[i].append(j)

city = list(map(int,input().split()))

q = [city[0]]
visited = set([city[0]])

while q:
  visit_city = q.pop()
  for next_city in lst[visit_city]:
    if next_city not in visited:
      q.append(next_city)
      visited.add(next_city)

if set(city) - visited:
  print('NO')
else:
  print('YES')
