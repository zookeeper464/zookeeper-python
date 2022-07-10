from sys import stdin

def input():
  return stdin.readline().rstrip('\n')

N = int(input())
mat = [list(input()) for _ in range(N)]

def search_2_mat(i,j):
  global one, zero
  temp = {mat[i][j],mat[i][j+1],mat[i+1][j],mat[i+1][j+1]}
  if temp == {"1"}:
    return "1"
  elif temp == {"0"}:
    return "0"
  else:
    return f"({mat[i][j]}{mat[i][j+1]}{mat[i+1][j]}{mat[i+1][j+1]})"

while (N>1):
  temp_mat = []
  for row in range(0,N,2):
    temp_list = []
    for col in range(0,N,2):
      temp_list.append(search_2_mat(row,col))
    temp_mat.append(temp_list)
  N = N>>1
  mat = [temp_mat[i][:] for i in range(N)]

print(mat[0][0])
