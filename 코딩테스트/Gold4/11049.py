n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
table = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1,n):
  table[i-1][i] = mat[i-1][0]*mat[i][0]*mat[i][1]

for d in range(2,n):
  for start in range(n-d):
    end = start+d
    table[start][end] = min([table[start][k]+table[k+1][end]+(mat[start][0]*mat[k][1]*mat[end][1]) for k in range(start,end)])

print(table[0][-1])
