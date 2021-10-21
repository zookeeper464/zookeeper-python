answer = []
n = int(input())
lst = list(map(int,input().split()))

table = [[1 if r==c else 0 for c in range(n)] for r in range(n)]
for i in range(n-1):
  if lst[i]==lst[i+1]:
    table[i][i+1] = 1

for d in range(2,n):
  for start in range(n-d):
    end = start+d
    if lst[start] == lst[end] and table[start+1][end-1]:
      table[start][end] = 1

m = int(input())
for _ in range(m):
  a,b = map(int,input().split())
  answer.append(table[a-1][b-1])

print(*answer,sep='\n')
