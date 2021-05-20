n,m = map(int,input().split())
mat1, mat2 = [], []
for i in range(n):
  mat1.append(list(map(int,input().split())))

m,k = map(int,input().split())
for i in range(m):
  mat2.append(list(map(int,input().split())))

answer = []
for i in range(n):
  answer.append([0 for _ in range(k)])
  for j in range(k):
    for l in range(m):
      answer[-1][j] += mat1[i][l]*mat2[l][j]

for i in answer:
  for j in i:
    print(j, end=" ")
  print()
