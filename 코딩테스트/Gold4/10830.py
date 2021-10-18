def matrix_mul(a, b):
  result = [[0]* n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      for k in range(n):
        result[i][j] += (a[i][k]*b[k][j])%1000

      result[i][j] %= 1000
                
  return result
    
n,b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
b = bin(b)[2:]


result = [[1 if i==j else 0 for i in range(n)] for j in range(n)]

for i in range(len(b)):
  if b[-i-1] == '1':
    temp = matrix[:]
    while i != 0:
      temp = matrix_mul(temp, temp)
      i -= 1
    result = matrix_mul(result, temp)

for row in result:
    print(*row)
